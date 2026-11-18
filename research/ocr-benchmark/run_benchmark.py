#!/usr/bin/env python3
"""Compare Tesseract and PaddleOCR against a receipt manifest."""
from __future__ import annotations
import argparse, json, re, resource, statistics, subprocess, tempfile, time
import cv2
import numpy as np
from pathlib import Path
from typing import Any

def compact(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().casefold()

def words(value: str) -> list[str]:
    return re.findall(r"\w+", compact(value), flags=re.UNICODE)

def edit_distance(a: list[Any], b: list[Any]) -> int:
    row = list(range(len(b) + 1))
    for i, left in enumerate(a, 1):
        nxt = [i]
        for j, right in enumerate(b, 1):
            nxt.append(min(nxt[-1] + 1, row[j] + 1, row[j - 1] + (left != right)))
        row = nxt
    return row[-1]

def rate(distance: int, denominator: int) -> float | None:
    return distance / denominator if denominator else None

def normalize_total(value: Any) -> int | None:
    if value is None: return None
    digits = re.sub(r"[^0-9]", "", str(value))
    return int(digits) if digits else None

def normalize_field(name: str, value: Any) -> Any:
    return normalize_total(value) if name == "total" else compact(value)

def field_guess(text: str, name: str) -> str | int | None:
    if name == "date":
        match = re.search(r"\b(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})\b", text)
        return "-".join(match.groups()) if match else None
    if name == "total":
        # Prefer the amount on a total-labelled line; never select receipt IDs/items.
        lines = text.splitlines()
        anchors = re.compile(r"\b(?:grand\s+total|total|jumlah|amount\s+due)\b", re.I)
        candidates = []
        for line in lines:
            if anchors.search(line):
                candidates.extend(re.findall(r"(?:rp\s*)?([0-9][0-9.,]*)", line, re.I))
        # OCR engines may emit the label and amount on adjacent lines.
        for offset in (0, 1, 2):
            for index, line in enumerate(lines):
                if not anchors.search(line):
                    continue
                if index + offset < len(lines):
                    candidates.extend(re.findall(r"(?:rp\s*)?([0-9][0-9.,]*)", lines[index + offset], re.I))
            if candidates:
                return normalize_total(candidates[-1])
        return None
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines[0] if lines else None

def preprocess(image: Path) -> Path:
    source = cv2.imread(str(image), cv2.IMREAD_GRAYSCALE)
    if source is None: raise ValueError(f"cannot read {image}")
    # Symmetric crop/contrast/deskew preprocessing for both engines.
    points = cv2.findNonZero(cv2.threshold(source, 245, 255, cv2.THRESH_BINARY_INV)[1])
    if points is not None:
        x, y, w, h = cv2.boundingRect(points); source = source[max(0, y-8):y+h+8, max(0, x-8):x+w+8]
    source = cv2.normalize(source, None, 0, 255, cv2.NORM_MINMAX)
    coords = np.column_stack(np.where(source < 220))
    if len(coords) > 20:
        angle = cv2.minAreaRect(coords[:, ::-1].astype(np.float32))[-1]
        angle = angle + 90 if angle < -45 else angle
        if abs(angle) < 15:
            h, w = source.shape; matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, 1.0)
            source = cv2.warpAffine(source, matrix, (w, h), borderValue=255)
    output = Path(tempfile.mkstemp(suffix=".png")[1]); cv2.imwrite(str(output), source); return output

def run_tesseract(image: Path, lang: str, timeout: int) -> tuple[str, int | None]:
    with tempfile.NamedTemporaryFile() as rss_file:
        result = subprocess.run(["/usr/bin/time", "-f", "%M", "-o", rss_file.name, "tesseract", str(image), "stdout", "-l", lang, "--psm", "6"], check=True, text=True, capture_output=True, timeout=timeout)
        try: rss = int(Path(rss_file.name).read_text().strip())
        except (ValueError, OSError): rss = None
    return result.stdout, rss

def run_paddle(image: Path) -> str:
    from paddleocr import PaddleOCR  # type: ignore
    if run_paddle.ocr is None:
        run_paddle.ocr = PaddleOCR(lang="en", use_doc_orientation_classify=False, use_doc_unwarping=False, use_textline_orientation=False)
    result = run_paddle.ocr.predict(str(image))
    lines = []
    for page in result:
        data = page.json if hasattr(page, "json") else page
        if isinstance(data, str): data = json.loads(data)
        data = data.get("res", data) if isinstance(data, dict) else {}
        texts = [str(x) for x in data.get("rec_texts", []) if x]
        boxes = data.get("rec_boxes", data.get("rec_polys", []))
        items = []
        for index, text in enumerate(texts):
            box = np.asarray(boxes[index]) if index < len(boxes) else np.array([0, index * 20, 0, index * 20])
            if box.ndim == 1 and box.size == 4: x1, y1, x2, y2 = box
            else:
                x1, y1 = box.min(axis=0); x2, y2 = box.max(axis=0)
            items.append((float((y1+y2)/2), float(x1), float(y2-y1), text))
        items.sort()
        rows = []
        for item in items:
            if not rows or abs(item[0] - rows[-1][0]) > max(8, item[2] * 0.6): rows.append([item[0], [item]])
            else: rows[-1][1].append(item)
        lines.extend(" ".join(item[3] for item in sorted(row[1], key=lambda x: x[1])) for row in rows)
    return "\n".join(lines)
run_paddle.ocr = None  # type: ignore[attr-defined]

def evaluate(engine: str, samples: list[dict[str, Any]], root: Path, timeout: int) -> dict[str, Any]:
    rows = []
    for sample in samples:
        image = root / sample["file"]
        started, error, text, child_rss = time.perf_counter(), None, "", None
        prepared = None
        try:
            prepared = preprocess(image)
            if engine == "tesseract": text, child_rss = run_tesseract(prepared, "eng+ind", timeout)
            else: text = run_paddle(prepared)
        except subprocess.TimeoutExpired: error = "timeout"
        except Exception as exc: error = f"{type(exc).__name__}: {exc}"
        finally:
            if prepared: prepared.unlink(missing_ok=True)
        truth = sample.get("ground_truth", {})
        raw_truth = sample.get("raw_text") or truth.get("raw_text")
        cer = wer = cer_bounded = wer_bounded = None
        if raw_truth is not None:
            # Compare the structured proxy with OCR lines likely to contain items/totals;
            # bounded scores remain interpretable when OCR emits extra receipt metadata.
            digit_text = " ".join(line for line in text.splitlines() if re.search(r"\d", line))
            ref, hyp = compact(raw_truth), compact(digit_text)
            cer_distance = edit_distance(list(hyp), list(ref))
            wer_distance = edit_distance(words(hyp), words(ref))
            cer = rate(cer_distance, len(ref))
            wer = rate(wer_distance, len(words(ref)))
            cer_bounded = 1 - rate(cer_distance, max(len(ref), len(hyp))) if max(len(ref), len(hyp)) else None
            wer_bounded = 1 - rate(wer_distance, max(len(words(ref)), len(words(hyp)))) if max(len(words(ref)), len(words(hyp))) else None
        fields = {}
        for name in ("merchant", "date", "total"):
            expected, actual = truth.get(name), field_guess(text, name)
            fields[name] = {"expected": expected, "actual": actual,
                "exact": (compact(actual) == compact(expected)) if expected is not None else None,
                "normalized": normalize_field(name, actual) == normalize_field(name, expected) if expected is not None else None}
        rows.append({"file": sample["file"], "category": sample.get("category"), "synthetic": sample.get("synthetic", False), "text": text, "cer": cer, "wer": wer, "cer_bounded": cer_bounded, "wer_bounded": wer_bounded, "fields": fields, "latency_ms": (time.perf_counter() - started) * 1000, "rss_kb": child_rss, "error": error})
    latencies = [r["latency_ms"] for r in rows if not r["error"]]
    def percentile(p: float):
        return statistics.quantiles(latencies, n=100)[int(p)-1] if len(latencies) > 1 else (latencies[0] if latencies else None)
    scores = [v["normalized"] for r in rows for v in r["fields"].values() if v["normalized"] is not None]
    exact = [v["exact"] for r in rows for v in r["fields"].values() if v["exact"] is not None]
    rss = [r["rss_kb"] for r in rows if r["rss_kb"] is not None]
    return {"engine": engine, "samples": rows, "summary": {"count": len(rows), "failures": sum(bool(r["error"]) for r in rows), "cer": statistics.mean([r["cer"] for r in rows if r["cer"] is not None]) if any(r["cer"] is not None for r in rows) else None, "wer": statistics.mean([r["wer"] for r in rows if r["wer"] is not None]) if any(r["wer"] is not None for r in rows) else None, "cer_bounded": statistics.mean([r["cer_bounded"] for r in rows if r["cer_bounded"] is not None]) if any(r["cer_bounded"] is not None for r in rows) else None, "wer_bounded": statistics.mean([r["wer_bounded"] for r in rows if r["wer_bounded"] is not None]) if any(r["wer_bounded"] is not None for r in rows) else None, "field_exact_accuracy": statistics.mean(exact) if exact else None, "field_normalized_accuracy": statistics.mean(scores) if scores else None, "latency_p50_ms": percentile(50), "latency_p95_ms": percentile(95), "peak_rss_kb": max(rss) if rss else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "rss_scope": "tesseract child process" if engine == "tesseract" else "parent process (includes PaddleOCR)"}}

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--root", type=Path, default=Path(".")); p.add_argument("--manifest", type=Path, default=Path("research/receipt-samples/manifest.json")); p.add_argument("--output", type=Path, default=Path("research/ocr-benchmark/results.json")); p.add_argument("--report", type=Path, default=Path("research/ocr-benchmark/report.md")); p.add_argument("--timeout", type=int, default=60); args = p.parse_args()
    samples = json.loads(args.manifest.read_text(encoding="utf-8")); results = {"manifest": str(args.manifest), "engines": [evaluate(e, samples, args.root, args.timeout) for e in ("tesseract", "paddleocr")]}
    args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# OCR benchmark", "", "| Engine | Samples | Failures | CER ratio (proxy) | WER ratio (proxy) | CER bounded | WER bounded | Exact field accuracy | Normalized field accuracy | p50 ms | p95 ms | Peak RSS KB |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for result in results["engines"]:
        s = result["summary"]; lines.append("| {engine} | {count} | {failures} | {cer} | {wer} | {cer_bounded} | {wer_bounded} | {field_exact_accuracy} | {field_normalized_accuracy} | {latency_p50_ms} | {latency_p95_ms} | {peak_rss_kb} |".format(engine=result["engine"], **s))
    lines += ["", "CER/WER are proxy metrics from CORD structured ground truth, not literal transcript ground truth."]
    for result in results["engines"]:
        for row in result["samples"]:
            lines.append(f"\n## {result['engine']} — {row['file']}\n\n- Error: `{row['error']}`; latency: `{row['latency_ms']:.1f} ms`; RSS: `{row['rss_kb']}` KB\n- CER ratio: `{row['cer']}`; WER ratio: `{row['wer']}`; CER bounded: `{row['cer_bounded']}`; WER bounded: `{row['wer_bounded']}`\n- Fields: `{json.dumps(row['fields'], ensure_ascii=False)}`")
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8"); return 0
if __name__ == "__main__": raise SystemExit(main())
