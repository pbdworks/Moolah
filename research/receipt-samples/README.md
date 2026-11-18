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
