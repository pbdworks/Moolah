#!/usr/bin/env python3
"""Compare Tesseract and PaddleOCR against the receipt manifest.

The harness deliberately treats missing raw_text as unavailable rather than
inventing a text ground truth from structured fields.
"""
from __future__ import annotations

import argparse
import json
import re
import resource
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


def compact(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().casefold()


def words(value: str) -> list[str]:
    return re.findall(r"\w+", compact(value), flags=re.UNICODE)


def edit_distance(a: list[Any], b: list[Any]) -> int:
    row = list(range(len(b) + 1))
    for i, left in enumerate(a, 1):
        next_row = [i]
        for j, right in enumerate(b, 1):
            next_row.append(min(next_row[-1] + 1, row[j] + 1, row[j - 1] + (left != right)))
        row = next_row
    return row[-1]


def rate(distance: int, denominator: int) -> float | None:
    return distance / denominator if denominator else None


def normalize_total(value: Any) -> int | None:
    if value is None:
        return None
    digits = re.sub(r"[^0-9]", "", str(value))
    return int(digits) if digits else None


def normalize_field(name: str, value: Any) -> Any:
    if name == "total":
        return normalize_total(value)
    return compact(value)


def field_guess(text: str, name: str) -> str | int | None:
    if name == "date":
        match = re.search(r"\b(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})\b", text)
        return "-".join(match.groups()) if match else None
    if name == "total":
        candidates = re.findall(r"(?:rp\s*)?([0-9][0-9.,]*)", text, re.I)
        return max((normalize_total(x) for x in candidates), default=None)
    # Merchant extraction is inherently layout-specific; use the first non-empty line.
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines[0] if lines else None


def run_tesseract(image: Path, lang: str, timeout: int) -> str:
    result = subprocess.run(["tesseract", str(image), "stdout", "-l", lang], check=True, text=True, capture_output=True, timeout=timeout)
    return result.stdout


def run_paddle(image: Path) -> str:
    from paddleocr import PaddleOCR  # type: ignore
    ocr = run_paddle.ocr
    if ocr is None:
        run_paddle.ocr = PaddleOCR(lang="en", use_doc_orientation_classify=False, use_doc_unwarping=False, use_textline_orientation=False)
    result = run_paddle.ocr.predict(str(image))
    lines: list[str] = []
    for page in result:
        data = page.json if hasattr(page, "json") else page
        if isinstance(data, str):
            data = json.loads(data)
        data = data.get("res", data) if isinstance(data, dict) else {}
        lines.extend(str(x) for x in data.get("rec_texts", []) if x)
    return "\n".join(lines)


run_paddle.ocr = None  # type: ignore[attr-defined]


def evaluate(engine: str, samples: list[dict[str, Any]], root: Path, timeout: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for sample in samples:
        image = root / sample["file"]
        started = time.perf_counter()
        error = None
        text = ""
        try:
            if engine == "tesseract":
                text = run_tesseract(image, "eng+ind", timeout)
            else:
                text = run_paddle(image)
        except subprocess.TimeoutExpired:
            error = "timeout"
        except Exception as exc:  # keep one bad image from hiding other results
            error = f"{type(exc).__name__}: {exc}"
        latency_ms = (time.perf_counter() - started) * 1000
        truth = sample.get("ground_truth", {})
        raw_truth = sample.get("raw_text") or truth.get("raw_text")
        cer = wer = None
        if raw_truth is not None:
            cer = rate(edit_distance(list(compact(text)), list(compact(raw_truth))), len(compact(raw_truth)))
            wer = rate(edit_distance(words(text), words(raw_truth)), len(words(raw_truth)))
        fields = {}
        for name in ("merchant", "date", "total"):
            expected = truth.get(name)
            actual = field_guess(text, name)
            fields[name] = {
                "expected": expected,
                "actual": actual,
                "exact": actual == expected if expected is not None else None,
                "normalized": normalize_field(name, actual) == normalize_field(name, expected) if expected is not None else None,
            }
        rows.append({"file": sample["file"], "category": sample.get("category"), "synthetic": sample.get("synthetic", False), "text": text, "cer": cer, "wer": wer, "fields": fields, "latency_ms": latency_ms, "error": error})
    latencies = [row["latency_ms"] for row in rows if not row["error"]]
    def percentile(p: float) -> float | None:
        return statistics.quantiles(latencies, n=100)[int(p) - 1] if len(latencies) > 1 else (latencies[0] if latencies else None)
    field_scores = [v["normalized"] for row in rows for v in row["fields"].values() if v["normalized"] is not None]
    return {"engine": engine, "samples": rows, "summary": {"count": len(rows), "failures": sum(bool(x["error"]) for x in rows), "cer": statistics.mean([x["cer"] for x in rows if x["cer"] is not None]) if any(x["cer"] is not None for x in rows) else None, "wer": statistics.mean([x["wer"] for x in rows if x["wer"] is not None]) if any(x["wer"] is not None for x in rows) else None, "field_normalized_accuracy": statistics.mean(field_scores) if field_scores else None, "latency_p50_ms": percentile(50), "latency_p95_ms": percentile(95), "peak_rss_kb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--manifest", type=Path, default=Path("research/receipt-samples/manifest.json"))
    parser.add_argument("--output", type=Path, default=Path("research/ocr-benchmark/results.json"))
    parser.add_argument("--report", type=Path, default=Path("research/ocr-benchmark/report.md"))
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    results = {"manifest": str(args.manifest), "engines": []}
    for engine in ("tesseract", "paddleocr"):
        results["engines"].append(evaluate(engine, manifest, args.root, args.timeout))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# OCR benchmark", "", "| Engine | Samples | Failures | CER | WER | Field normalized accuracy | p50 ms | p95 ms | Peak RSS KB |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for result in results["engines"]:
        s = result["summary"]
        lines.append("| {engine} | {count} | {failures} | {cer} | {wer} | {field_normalized_accuracy} | {latency_p50_ms} | {latency_p95_ms} | {peak_rss_kb} |".format(engine=result["engine"], **s))
        for row in result["samples"]:
            lines.append(f"\n## {result['engine']} — {row['file']}\n\n- Error: `{row['error']}`\n- CER: `{row['cer']}`; WER: `{row['wer']}`; latency: `{row['latency_ms']:.1f} ms`\n- Fields: `{json.dumps(row['fields'], ensure_ascii=False)}`")
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
