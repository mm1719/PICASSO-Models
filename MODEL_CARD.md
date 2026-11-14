# PICASSO R1 historical baseline: 23-target ConvNeXt V2-L

**Release: `r1-historical-baseline-v1`. A separately labeled historical R1 baseline, not the current 20-target A2 application model. Tensor-only safetensors export, 23 targets, noncommercial weight license.**

## Model identity

- Project: PICASSO / mm1719.
- Task: classification of FlowCAM plankton/particle image crops into 23 saved target categories. These are mixed coarse taxonomic and non-taxonomic targets, not 23 species.
- Backbone: `convnextv2_large.fcmae_ft_in22k_in1k` from [timm](https://huggingface.co/timm/convnextv2_large.fcmae_ft_in22k_in1k), initialized from upstream pretrained weights and fine-tuned for this task.
- Input size recorded by the training run: RGB, 128 × 128.
- Saved checkpoint: EMA weights, selected by validation macro F1, epoch 27.
- Research run identifier: `2026-06-21_212913_r01s02_cw022_macroselect_b192_img128_e30_compile`.
- Original checkpoint byte count: 785,971,725.
- Original checkpoint SHA-256: `28d6281d91fad07a0e63aef69b893beba0dd8c7d1cafe955e154bfdaffc10891`.
- Exported weight SHA-256: `553573b91469b2029ac72612ae473251208e629545ecce234095cdaed381ff34`.
- Export size: 785,859,452 bytes; 380 float32 tensors (196,455,191 values).

## Intended use and boundaries

Intended use is noncommercial research, reproducibility, and evaluation of this particular classifier. Outputs require domain review. The saved category scheme is not a universal or current biological taxonomy, and model confidence is not an expert identification. No cross-instrument, geographic, temporal, or clinical reliability claim is made. No hosted service, commercial-use grant, or institutional endorsement is implied.

## Data and provenance

The historical input manifest contains 4,241,651 rows; 4,075,731 remain eligible after the saved mapping and exclusions. The preserved split contains only the six named principal sources, with no additional EcoTaxa expansion manifest. This does not mean the Tara/FlowCAM datasets themselves never originated in EcoTaxa. Their published source records remain the relevant provenance.

| Source | Train | Validation | Test |
|---|---:|---:|---:|
| LifeWatch training set | 261,755 | 32,359 | 32,591 |
| LifeWatch full image library | 1,215,465 | 152,359 | 151,836 |
| FlowCAMNet | 240,999 | 29,983 | 30,000 |
| Tara Pacific Deck Net | 1,258,380 | 157,723 | 157,772 |
| Tara Pacific Bongo Net | 280,279 | 34,660 | 34,948 |
| Ifremer SRN | 3,696 | 477 | 449 |

Counts above were recomputed from the preserved split manifest. Its SHA-256 matched the value saved with this run: `f58513fe4f7a0dbede10efd4b6e2366ee24c1060bb900df31416e267ecdbaf8d`. The current global manifest has changed since the historical runs; it must not be substituted for a run's recorded snapshot.

The split is an image-row, target-stratified 80/10/10 allocation, seed 20260421, not a held-out-source or held-out-site experiment. Source-aware stratification is false. Shared acquisition conditions or source dependencies across splits have not been ruled out by this review. Original images, per-image paths, private exports, annotation caches, and source datasets are not part of this weight release.

## Training configuration

- Optimizer: AdamW; initial learning rate 0.00015; weight decay 0.08.
- Scheduled epochs: 30; batch size: 192; cosine schedule with 5 warmup epochs.
- Training seed: 42; label smoothing: 0.08.
- Class weighting: `panaiotis_relative`, exponent 0.22.
- Drop-path rate: 0.15; EMA decay: 0.9998.
- Recorded augmentation: `rand-m9-mstd0.5-inc1` with color jitter and horizontal flip.
- Evaluation uses the run's timm evaluation-transform path at 128 pixels; no test-time augmentation is recorded.

Frozen inference preprocessing: convert to RGB, resize the shorter edge to 146 with bicubic interpolation and antialiasing, center-crop to 128 × 128, scale to [0, 1], then normalize with mean [0.485, 0.456, 0.406] and standard deviation [0.229, 0.224, 0.225]. Use the supplied `config.json` and `infer.py`, not the pretrained ImageNet model's 288-pixel test transform.

The explicit transform was bitwise checked against the source training-code factory on four synthetic images in the pinned release-verification environment. Those current library versions are not asserted to be the original training environment.

## Recorded evaluation

These are existing saved experiment results, not newly reproduced measurements:

| Metric | Value |
|---|---:|
| Test image rows | 407,596 |
| Top-1 accuracy | 93.0622% |
| Macro F1 | 0.683153 |
| Balanced accuracy | 0.733799 |
| Weighted F1 | 0.931467 |

Class imbalance is substantial and some test classes have very few examples. Aggregate accuracy should not replace class-level performance. A2 and R1 use different data, label spaces, and evaluation cohorts; their scores are not a controlled head-to-head comparison. No independent external benchmark was rerun for this release review.

## Output-label order

This order matches both the actual checkpoint metadata and its saved class index. Preserve it exactly; do not infer a new alphabetical order.

| Index | Target ID | Saved display label | Test support |
|---:|---|---|---:|
| 0 | 9 | Sarcomastigophora | 105 |
| 1 | 11 | Ciliophora | 2768 |
| 2 | 51 | Mollusca | 148 |
| 3 | 558 | Porifera | 30 |
| 4 | 799 | Nematoda | 12 |
| 5 | 801 | Chlorophyta | 3 |
| 6 | 882 | Annelida | 35 |
| 7 | 1065 | Arthropoda | 3010 |
| 8 | 1267 | Cnidaria | 16 |
| 9 | 1410 | Foraminifera | 83 |
| 10 | 1806 | Echinodermata | 2 |
| 11 | 1821 | Chordata | 41 |
| 12 | 14260 | Rotifera | 40 |
| 13 | 146537 | Cyanobacteria | 9766 |
| 14 | 148898 | Bacillariophyta | 11066 |
| 15 | 345465 | Ochrophyta | 126 |
| 16 | 369190 | Haptophyta | 254 |
| 17 | 370437 | Heterokontophyta | 110470 |
| 18 | 450030 | Myzozoa | 7393 |
| 19 | 582420 | Rhizaria | 594 |
| 20 | 582421 | Radiozoa | 777 |
| 21 | ntc_028 | egg/cyst | 3182 |
| 22 | ntc_082 | detritus | 257675 |

## Rights and attribution

The weights are distributed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), retaining the pretrained ConvNeXt V2-L weight conditions and attribution. Sharing and adaptation for noncommercial purposes are permitted subject to that license. Free download does not mean unrestricted commercial use. Intended research use above is guidance, not an additional academic-only restriction.

See [ATTRIBUTION.md](ATTRIBUTION.md), [LICENSE.md](LICENSE.md), and the bundled notices. The weight license is scoped to the weights, not a blanket license for this repository. Data-source licenses describe their source releases, not an assertion that every trained model automatically inherits every dataset license. Original datasets are not redistributed here. No endorsement by upstream authors or data providers is implied.

The six recorded principal sources have public source-rights statements. The Deck Net SEANOE and IPT records differ (BY versus BY-NC); both are retained in the attribution ledger, and this release uses a noncommercial scope. This documented review is not a warranty about all downstream uses or jurisdictions.

## Release validation and limitations

The source checkpoint was statically inspected without executing its pickle metadata. Its embedded configuration matched the saved run configuration. The classifier head is [23, 1536] plus bias. The raw source checkpoint, which contains a machine-local training path, is not distributed.

The export directly copies the original raw float32 tensor storage into safetensors. All 380 per-tensor byte hashes match. Both original raw tensor values and the exported tensors load strictly into the same model architecture. Four synthetic-image CPU forward passes produced bitwise-identical logits (maximum absolute difference 0). The explicit preprocessing also matched the source-code factory bitwise. See [VALIDATION.md](VALIDATION.md) and [validation.json](validation.json).

These are conversion-equivalence checks, not a test-set rerun, data-leakage audit, privacy/memorization audit, or new generalization benchmark. Some labels have only 2 or 3 historical test examples. No commercial, ecological-decision, safety-critical, or cross-instrument suitability is established by this release. Model predictions should be reviewed by a qualified domain user.

R1 and A2 use different label spaces, training manifests, and test cohorts. Do not pair this weight file with A2's labels or metrics or substitute it in the existing application without explicitly adapting and evaluating that integration.
