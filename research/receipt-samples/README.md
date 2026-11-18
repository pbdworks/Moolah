# Receipt samples

This fixture set is for reproducible OCR benchmarking. One generic digital-receipt example is included under CC BY 4.0; the remaining entries are self-created synthetic fixtures under CC0 1.0. It is not an Indonesian receipt. Synthetic results must be reported separately and must not be used to claim Indonesian receipt accuracy.

| File | Category | Origin | License | Author | Synthetic | Attribution |
|---|---|---|---|---|---:|---|
| `images/03_pan.webp` | generic digital receipt example (PAN truncation) | [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Example_of_PAN_truncation_in_digital_receipt.webp) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Mborb | no | Mborb / Wikimedia Commons / CC BY 4.0 |
| `images/04_minimarket_synthetic.svg` | minimarket | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/05_minimarket_synthetic.svg` | minimarket | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/08_minimarket_synthetic.svg` | minimarket | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/10_minimarket_synthetic.svg` | minimarket | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/06_restaurant_synthetic.svg` | restaurant | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/09_restaurant_synthetic.svg` | restaurant | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/07_qris_synthetic.svg` | e-wallet/QRIS | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/10_qris_synthetic.svg` | e-wallet/QRIS | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |
| `images/11_qris_synthetic.svg` | e-wallet/QRIS | self-created | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Moolah contributors | yes | none required |

## Limitations

Only one non-synthetic generic digital-receipt example was found with a clear redistribution license during this collection pass. It is not evidence of Indonesian receipt accuracy. CORD v2 provides the primary real-Indonesian dataset for the benchmark: [dataset](https://huggingface.co/datasets/naver-clova-ix/cord-v2), licensed CC BY 4.0. The target composition is represented by synthetic fixtures, but this does not close the requirement for 10 real Indonesian receipts. The duplicate visual fixtures are deliberate placeholders and should not be treated as independent real-world examples. Ground truth in `manifest.json` was entered from the fixture content, not OCR output.

## Dataset search: minimarket and e-wallet/QRIS

A search was performed for reusable Indonesian receipt datasets with real images, field/box annotations or manually verified ground truth, and an explicit redistribution license. No qualifying minimarket-specific or e-wallet/QRIS-specific dataset was found in the checked sources. CORD v2 is the qualifying primary dataset for the benchmark, but its published description covers shops/restaurants and the released sample slice used here is restaurant-oriented; it should not be used to infer minimarket or e-wallet accuracy.

Checked sources:

- [CORD repository](https://github.com/clovaai/cord) — Indonesian receipts with box/text and semantic annotations, CC BY 4.0; no category guarantee for minimarket/e-wallet.
- [CORD v2 on Hugging Face](https://huggingface.co/datasets/naver-clova-ix/cord-v2) — 1,000 rows, `ground_truth` field, CC BY 4.0; published examples are restaurant/shop receipts, not a documented minimarket/e-wallet split.
- [Mendeley OCR Invoice](https://data.mendeley.com/datasets/5n3jwggcjk) — Indonesian mixed receipt sources and manually verified JSON, CC BY 4.0; no documented minimarket/e-wallet subset in the public description.
- [Kaggle Indonesian OCR image data](https://www.kaggle.com/datasets/appenlimited/ocr-image-data-of-indonesian-language-documents) — broad Indonesian document OCR dataset; receipt category/field ground truth and redistribution terms were not established from the checked page, so it is excluded.

Therefore minimarket and e-wallet/QRIS accuracy remains **not measured**, rather than being filled with synthetic or restaurant-derived claims.
