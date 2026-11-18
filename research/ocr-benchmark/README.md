# OCR benchmark

GitHub Actions compares Tesseract 5 (`tesseract-ocr` + Indonesian language data) and PaddleOCR `3.2.0`/PaddlePaddle `3.2.0` against `research/receipt-samples/manifest.json`. The workflow is intentionally the execution environment: do not install OCR engines on the development VPS.

## Input contract

Each manifest item contains `file`, `category`, provenance fields, `synthetic`, and `ground_truth` (`merchant`, ISO `date`, integer `total`, `currency`). Add `ground_truth.raw_text` when CER/WER is required; structured fields alone cannot provide a valid raw-text reference. Samples without raw text still contribute field accuracy and latency.

## Run

```bash
python research/ocr-benchmark/run_benchmark.py
```

The workflow runs on `workflow_dispatch`, or on pushes changing the samples/workflow. It publishes `results.json` and `report.md` as an artifact and appends the aggregate table to the job summary. PaddleOCR downloads its model on the GitHub runner; the resulting model footprint should be recorded in the report in the next measurement pass.

Metrics are per sample and aggregate: CER/WER where raw text exists, exact and normalized field matching, p50/p95 latency, peak process RSS, and failures. Rupiah normalization removes formatting punctuation and non-digits. Tesseract and PaddleOCR are both best-effort per sample so one engine failure does not hide the other results.

## Limitations and rollback

This is a measurement harness, not a production OCR implementation. Merchant extraction is a transparent first-line heuristic and must be replaced by a layout-aware extractor if field accuracy is misleading. If a dependency/API breaks, pin a known-good PaddleOCR/PaddlePaddle pair in this file and rerun via manual dispatch; prior artifacts remain available for comparison.
