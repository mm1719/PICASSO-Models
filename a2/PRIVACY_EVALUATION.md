# PICASSO 20-Class Plankton Classifier: bounded membership-inference evaluation

Architecture: ConvNeXt V2-L. Internal experiment trace: R3S2-A2.

**2026-11-15. A weak membership-discrimination signal was measured. This is not a zero-leakage certificate, an image-reconstruction test, or a data-rights determination.** Full-weight publication enables stronger white-box attacks than the ones tested here.

## Sampling and separation

The hash-matched historical split contains 4,137,449 rows: 3,309,950 train, 413,735 validation, and 413,764 test. Identical textual image paths have zero cross-split overlap. This does not rule out aliases or identical/near-duplicate image contents.

A deterministic seed-20261115, path-hash-priority sample matched members and test nonmembers within **target × dataset**; each additional EcoTaxa project was a separate dataset. Each main-source stratum was capped at 64 images per side, each additional-project stratum at 32, with smaller strata limited by shared support. Selection did not use model scores.

All **6,748** images decoded: 3,374 members and 3,374 nonmembers. No identical RGB pixels or fixed model inputs were found within this sample, and rehashed image files were unchanged. This was not a search of all training image contents.

- Calibration: 2,562 images.
- Independent attack evaluation: 4,090 images, 2,045 per side, 93 matched strata and 19 targets.
- Rare strata: 96 images, described separately and not used to fit/evaluate primary thresholds.
- Total sample: 20 targets, all six principal sources, 33 of 48 additional EcoTaxa projects. Only 24 additional projects contributed to the main calibrated evaluation.
- Of 170 source × target strata, 49 lacked matched support; their available population comprised 158 train and 2 test rows. Quota sampling emphasizes smaller sources/classes and **is not a population-frequency-weighted overall risk estimate**.

## Attacks and results

Only the checksum-verified safetensors model was loaded, on CPU with four threads and the frozen A2 preprocessing. No pickle execution or pretrained-weight download was used. The preregistered primary endpoint was held-out AUROC of negative true-label NLL; 0.5 indicates no ranking discrimination, not 50% training-image leakage.

Other scores were maximum softmax, negative entropy, negative modified entropy, and correctness. A fixed L2 logistic attack (C=1) used these scores plus class/dataset one-hot features; it was fit on calibration only, with no evaluation-based tuning. Thresholds were selected using calibration, weighted to the predefined evaluation stratum proportions. Calibration selected negative NLL from the five score attacks; the best evaluation score was not retrospectively selected.

| Attack / statistic | Evaluation AUROC | 95% interval |
|---|---:|---:|
| Negative NLL, primary | 0.5171 | 0.5071–0.5265 |
| Maximum softmax | 0.5166 | Not estimated |
| Negative entropy | 0.5158 | Not estimated |
| Negative modified entropy | 0.5172 | Not estimated |
| Correctness baseline | 0.5098 | Not estimated |
| Fixed logistic attack | 0.5163 | 0.5022–0.5300 |
| Within-stratum negative-NLL AUROC, pair-count weighted | 0.5071 | 0.4888–0.5248 |

The pooled primary estimate is slightly above chance under its conditional interval, with a small effect. The within-stratum interval includes 0.5; it estimates a different quantity. Neither result establishes overall safety or reconstructability of training images.

For independently calibration-selected low-false-positive thresholds:

| Attack | True member detections | Test nonmembers falsely called members |
|---|---:|---:|
| Negative NLL | 24/2,045 = 1.17% | 24/2,045 = 1.17% |
| Logistic | 33/2,045 = 1.61% | 17/2,045 = 0.83% |

A calibration FPR of at most 1% does not guarantee at most 1% evaluation FPR. With 2,045 images per side, 1% is only about 20 cases. These are membership-attack rates, **not probabilities of leaking or reconstructing an original image**.

Matched evaluation classification accuracy was 93.01% for members versus 91.05% for nonmembers; mean NLL was 0.3603 versus 0.4202. This is not a rerun of the entire historical test set. Descriptive negative-NLL AUROCs were 0.5042 for pooled additional EcoTaxa (481 per side) and 0.5202 for main sources (1,564 per side). The LifeWatch full-image-library slice was 0.5626 (222 per side), a follow-up signal rather than a corrected multiple-comparison finding or proof of that source's leakage.

## Limitations that remain

1. No image reconstruction/inversion, full white-box/gradient attack, LiRA, or shadow-model training was performed. Weak output-score attacks do not demonstrate resistance to stronger attacks. There is no differential-privacy guarantee.
2. Intervals use 1,000 independent image resamples within source × target × membership strata, conditional on the sampled sources/quotas. Specimen/acquisition correlation or near duplicates can make intervals too narrow. The logistic interval conditions on the fitted attack and excludes calibration refitting/threshold uncertainty.
3. Full training-set exact/near-duplicate content was not searched. Unseen duplicates could contaminate test nonmembers and weaken measured discrimination.
4. Membership follows the preserved fine-tuning split and untruncated 40-epoch training log, not per-image historical ingestion records or historical content hashes. Upstream pretraining overlap is unknown. The test set had been inspected in historical model comparisons; it is not a new external blind set.
5. Rare targets, unmatchable projects, outliers, and individual sensitive examples are not protected by an aggregate average. Dataset-use and distribution rights remain a separate question.

[Machine-readable aggregate results](privacy_evaluation.json) contain no original images, individual sample paths, or per-image logits. Private audit inputs remain on the research host. Original checkpoint, safetensors, split, and sampled image hashes were rechecked unchanged. Methods/results received independent review.

Method references: [Song and Mittal, USENIX Security 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/song) for modified entropy; [Carlini et al.](https://arxiv.org/abs/2112.03570) for stronger attacks and low-FPR evaluation. LiRA from the latter was **not** implemented.
