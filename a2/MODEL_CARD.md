# PICASSO 20-Class Plankton Classifier

Architecture: **ConvNeXt V2-L**. Internal experiment trace: **R3S2-A2** (round 03, stage 02); EMA epoch 40. The public display name does not change the checkpoint, class map, or experiment records.

**Release: `a2-20-target-v1`. A2's 20-target EMA epoch-40 classifier, the only downloadable PICASSO-Models checkpoint. Noncommercial, tensor-only safetensors package. Source-rights uncertainty is disclosed below; this is not a claim of universal rights clearance.**

## Model identity

- Project: PICASSO / mm1719.
- Task: classification of FlowCAM plankton/particle image crops into 20 saved target categories. These are mixed coarse taxonomic and non-taxonomic targets, not 20 species.
- Backbone: `convnextv2_large.fcmae_ft_in22k_in1k` from [timm](https://huggingface.co/timm/convnextv2_large.fcmae_ft_in22k_in1k), initialized from upstream pretrained weights and fine-tuned for this task.
- Input size recorded by the training run: RGB, 128 × 128.
- Saved checkpoint: EMA weights, selected by validation macro F1, epoch 40.
- Research run identifier: `2026-08-16_114723_r03s02_convnextv2_l_ra_m4_img128_b192`.
- Original checkpoint byte count: 785,953,421.
- Original checkpoint SHA-256: `32f4689c4894900bc2ae440bb17b553df10bd0444ad67b294652901a3b616430`.
- Exported weight SHA-256: `0865ff896cfd9f72509a819f19388dd8c3dc0da3e6befe84ce9ffede19334394`.
- Export size: 785,841,008 bytes; 380 float32 tensors (196,450,580 values).

## Intended use and boundaries

Intended use is noncommercial research, reproducibility, and evaluation of this particular classifier. Outputs require domain review. The saved category scheme is not a universal or current biological taxonomy, and model confidence is not an expert identification. No cross-instrument, geographic, temporal, or clinical reliability claim is made. No hosted service, commercial-use grant, or institutional endorsement is implied.

## Data and provenance

The input manifests contain 4,246,130 main-source rows plus 57,210 additional EcoTaxa rows. After mapping and exclusions, 4,137,449 rows are eligible. The additional data spans 48 EcoTaxa projects: 47 contribute training rows; project 18222 contributes one validation row only. Private/public access settings are not a substitute for project-specific reuse terms.

| Source | Train | Validation | Test |
|---|---:|---:|---:|
| LifeWatch training set | 261,733 | 32,373 | 32,595 |
| LifeWatch full image library | 1,214,986 | 152,174 | 151,768 |
| FlowCAMNet | 240,761 | 30,098 | 30,122 |
| Tara Pacific Deck Net | 1,258,776 | 157,490 | 157,651 |
| Tara Pacific Bongo Net | 284,225 | 35,410 | 35,455 |
| Ifremer SRN | 3,735 | 449 | 438 |
| Additional EcoTaxa projects | 45,734 | 5,741 | 5,735 |

Counts above were recomputed from the preserved split manifest. Its SHA-256 matched the value saved with this run: `51639823de20d7587137eabdc3255786a8ab4512319988b5345ae363b376828f`. The current global manifest has changed since the historical runs; it must not be substituted for a run's recorded snapshot.

The split is an image-row, target-stratified 80/10/10 allocation, seed 20260421, not a held-out-source or held-out-site experiment. Source-aware stratification is false. Shared acquisition conditions or source dependencies across splits have not been ruled out by this review. Original images, per-image paths, private exports, annotation caches, and source datasets are not part of this weight package.

## Training configuration

- Optimizer: AdamW; initial learning rate 0.0001; weight decay 0.08.
- Scheduled epochs: 40; batch size: 192; cosine schedule with 6 warmup epochs.
- Training seed: 42; label smoothing: 0.08.
- Class weighting: `panaiotis_relative`, exponent 0.22.
- Drop-path rate: 0.15; EMA decay: 0.9998.
- Recorded augmentation: `rand-m4-mstd0.5-inc1` with color jitter and horizontal flip.
- Evaluation uses the run's timm evaluation-transform path at 128 pixels; no test-time augmentation is recorded.

Frozen inference preprocessing: RGB conversion, bicubic resize of the shorter edge to 146 with antialiasing, center crop to 128 × 128, scale to [0, 1], then normalization with mean [0.485, 0.456, 0.406] and standard deviation [0.229, 0.224, 0.225]. Use the supplied `config.json` and `infer.py`, not the upstream ImageNet model's 288-pixel test transform.

The release-verification environment is pinned in `requirements.txt`. Those package versions are not asserted to be the historical training environment. The completed equivalence results and preprocessing check are recorded separately in `VALIDATION.md`.

## Recorded evaluation

These are existing saved experiment results, not newly reproduced measurements:

| Metric | Value |
|---|---:|
| Test image rows | 413,764 |
| Top-1 accuracy | 93.9927% |
| Macro F1 | 0.789876 |
| Balanced accuracy | 0.833754 |
| Weighted F1 | 0.940289 |

Class imbalance is substantial and some test classes have very few examples. Aggregate accuracy should not replace class-level performance. No independent external benchmark was rerun for this release review.

[Same-cohort A0-A3 summaries](https://github.com/mm1719/PICASSO-Models/blob/main/experiments/round03_stage02/README.md) report all four completed 20-target lines, not only the released model. A1 has the highest observed test macro F1; A2 was selected using the original joint validation point-estimate gate. A later class-stratified paired validation bootstrap found A2-minus-A0 macro F1 gain 0.006882 (95% CI -0.005235 to 0.018831) and balanced-accuracy gain 0.007964 (95% CI -0.008977 to 0.024990). Both intervals include zero; second-seed replication and final research promotion remain deferred. Public weight selection does not establish a reproducible global gain.

## Output-label order

This order matches both the actual checkpoint metadata and its saved class index. Preserve it exactly; do not infer a new alphabetical order.

| Index | Target ID | Saved display label | Test support |
|---:|---|---|---:|
| 0 | 11 | Ciliophora | 2768 |
| 1 | 51 | Mollusca | 148 |
| 2 | 558 | Porifera | 37 |
| 3 | 799 | Nematoda | 14 |
| 4 | 801 | Chlorophyta | 2089 |
| 5 | 882 | Annelida | 59 |
| 6 | 1065 | Arthropoda | 3010 |
| 7 | 1267 | Cnidaria | 26 |
| 8 | 1806 | Echinodermata | 2 |
| 9 | 1821 | Chordata | 225 |
| 10 | 14260 | Rotifera | 2061 |
| 11 | 146537 | Cyanobacteria | 9766 |
| 12 | 345465 | Ochrophyta | 126 |
| 13 | 368664 | Charophyta | 150 |
| 14 | 369190 | Haptophyta | 254 |
| 15 | 370437 | Heterokontophyta | 121528 |
| 16 | 450030 | Myzozoa | 7393 |
| 17 | 582420 | Rhizaria | 2792 |
| 18 | ntc_028 | egg/cyst | 3181 |
| 19 | ntc_082 | detritus | 258135 |

## Rights, provenance, and unresolved terms

The fine-tuned weights are distributed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), preserving upstream ConvNeXt V2-L weight terms, attribution, and modification notices. This noncommercial condition exists independently of training-data licenses. Free downloads do not grant commercial-use permission. The license applies only to rights the distributor can grant; it cannot override third-party rights or contracts. See [LICENSE.md](LICENSE.md) and [ATTRIBUTION.md](ATTRIBUTION.md).

The six principal data sources have identified public rights statements. A2 additionally used 48 EcoTaxa projects, of which 47 contributed training rows and one contributed only a validation row. A precise CC BY 4.0 image-dataset statement was located for project 6015; all 3,183 rows used from that project matched its saved source metadata and published geographic/temporal/instrument scope. For the other 47 projects, a source-specific image license or agreement covering the exact used snapshot was not independently established in this review. Public access, an associated article's license, and a related data table's license were not treated as blanket authorization for those images.

The research unit has consented to release the locally trained model. That consent is not represented as a grant from every external data provider. Missing source-specific terms do not establish that the weights are prohibited, and source-data licenses do not automatically become licenses on learned parameters. This package documents the evidence and remaining uncertainty rather than claiming either all rights are cleared or that every source necessarily requires a new individual permission. Any contractual restrictions in agreements not available to this review remain unverified.

[DATA_PROVENANCE.md](DATA_PROVENANCE.md) lists the exact projects, row counts, located evidence, and qualifications. No original images, per-image manifests, annotation exports, source-access credentials, personal contacts, or acquisition scripts are included. No data-provider or upstream-author endorsement is implied. A bounded membership-inference check has now been completed; it does not establish absence of memorization or image-extraction risk. See the results below.

## Packaging and validation boundaries

The original checkpoint is not distributed: it contains training configuration with a machine-local path. Packaging uses a non-executing static interpretation of its metadata and direct tensor-byte extraction, without invoking pickle callables or `torch.load`. The classifier head is [20, 1536] plus bias. The original model and source data remain unchanged.

Completed checks, exact package versions, tensor hashes, safe-format checksum, and synthetic CPU equivalence results are in [VALIDATION.md](VALIDATION.md) and `validation.json`. Conversion checks are not a rerun of the 413,764-row historical test set, a full dataset-deduplication or privacy audit, or independent evidence of generalization. Echinodermata has only two saved test examples. The split is image-level rather than acquisition-, source-, or site-held-out; dependencies between splits have not been ruled out.

This safe-format package contains all inference tensors but no optimizer/scheduler state. It is not a resumable training checkpoint or a promise of drop-in compatibility with an application expecting the original PyTorch checkpoint container. Use the bundled label order and preprocessing, and evaluate any application integration explicitly.

## Bounded membership-inference check

A separate CPU audit used 6,748 source × target matched images, split into 2,562 calibration, 4,090 independent attack-evaluation, and 96 rare-stratum descriptive images. Primary negative-NLL AUROC was **0.5171** (conditional 95% interval **0.5071–0.5265**): a weak membership-discrimination signal, not zero leakage. Within-stratum AUROC was **0.5071** (0.4888–0.5248); these are different estimands and neither is a privacy guarantee.

At calibration-selected low-FPR thresholds, negative NLL detected 24/2,045 members with 24/2,045 false positives (both 1.17%); logistic detected 33/2,045 (1.61%) with 17/2,045 false positives (0.83%). These percentages are attack outcomes, not original-image reconstruction probabilities.

The sample covered 20 targets and 33 additional EcoTaxa projects; primary analysis covered 19 targets and 24 projects. Quota sampling was not population-weighted. Full-manifest textual-path overlap was zero; sampled exact RGB/model-input duplicates were zero, but full training-content duplicates, aliases, and acquisition correlations were not excluded.

No image reconstruction, gradient/white-box attack, LiRA, shadow models, or differential-privacy analysis was performed. Conditional image-level intervals may be optimistic for correlated data. Historical membership and test independence have the limitations described in [PRIVACY_EVALUATION.md](PRIVACY_EVALUATION.md). Full-weight distribution permits stronger attacks. Source-rights uncertainty remains separate and unchanged.
