# OCR benchmark

GitHub Actions compares Tesseract 5 (`tesseract-ocr` + Indonesian language data) and PaddleOCR `3.2.0`/PaddlePaddle `3.2.0` against a pinned 20-sample slice of CORD v2. CORD is downloaded only in CI at revision `7f0115a4b758a71d6473b8d085751692da2fef98`, under CC BY 4.0; images are not committed. The workflow is intentionally the execution environment: do not install OCR engines on the development VPS.

## Input contract

Each manifest item contains `file`, `category`, provenance fields, `synthetic`, and `ground_truth` (`merchant`, ISO `date`, integer `total`, `currency`). Add `ground_truth.raw_text` when CER/WER is required; structured fields alone cannot provide a valid raw-text reference. Samples without raw text still contribute field accuracy and latency.

## Run

```bash
python research/ocr-benchmark/run_benchmark.py
```

The workflow runs on `workflow_dispatch`, or on pushes changing the samples/workflow. It publishes `results.json`, `report.md`, and the generated manifest as an artifact and appends the aggregate table to the job summary. CER/WER use a clearly labelled proxy reference assembled from CORD item names/prices/total, not a literal transcript. Tesseract RSS is measured for its child process; PaddleOCR RSS is the parent process including its model. CORD has structured totals/items but no reliable public merchant/date fields, so those fields are N/A rather than guessed. Synthetic fixtures, if present, are smoke tests and are not combined with CORD results.

Metrics are per sample and aggregate: proxy CER/WER, exact and normalized field matching, p50/p95 latency, peak RSS, and failures. Rupiah normalization removes formatting punctuation and non-digits. Tesseract and PaddleOCR are both best-effort per sample so one engine failure does not hide the other results.

## Limitations and rollback

This is a measurement harness, not a production OCR implementation. Merchant extraction is a transparent first-line heuristic and must be replaced by a layout-aware extractor if field accuracy is misleading. If a dependency/API breaks, pin a known-good PaddleOCR/PaddlePaddle pair in this file and rerun via manual dispatch; prior artifacts remain available for comparison.
