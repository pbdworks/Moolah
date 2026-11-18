#!/usr/bin/env python3
"""Materialize a small, deterministic CORD v2 evaluation slice in CI."""
import argparse, json
from pathlib import Path
from datasets import load_dataset

REVISION = "7f0115a4b758a71d6473b8d085751692da2fef98"

def scalar(value):
    if isinstance(value, list):
        return scalar(value[0]) if value else None
    if isinstance(value, dict):
        for key in ("text", "value", "total_price"):
            if key in value: return scalar(value[key])
    return value

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, default=Path("research/receipt-samples/cord"))
    p.add_argument("--limit", type=int, default=20)
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    ds = load_dataset("naver-clova-ix/cord-v2", split="test", revision=REVISION, streaming=True)
    manifest = []
    for index, row in enumerate(ds):
        if index >= args.limit: break
        image = row["image"]
        path = args.output / f"cord-test-{index:03d}.png"
        image.save(path)
        gt = row.get("ground_truth") or row.get("ground_truths") or row.get("gt_parse")
        if isinstance(gt, str): gt = json.loads(gt)
        gt = gt.get("gt_parse", gt) if isinstance(gt, dict) else {}
        total = scalar(gt.get("total", {}).get("total_price") if isinstance(gt.get("total"), dict) else gt.get("total"))
        manifest.append({"file": str(path), "category": "cord-v2", "source_url": "https://huggingface.co/datasets/naver-clova-ix/cord-v2", "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/", "author": "NAVER CLOVA", "synthetic": False, "ground_truth": {"merchant": None, "date": None, "total": total, "currency": "unknown", "items": gt.get("menu", [])}})
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    if len(manifest) < args.limit: raise RuntimeError(f"Only materialized {len(manifest)} CORD samples")

if __name__ == "__main__": main()
