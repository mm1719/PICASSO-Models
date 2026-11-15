# R3S2: 20-Target Training Results

This report publishes all four completed 20-target lines, A0-A3. **Only A2
weights are distributed**; A0, A1 and A3 are result summaries, not additional
model downloads. Earlier label spaces, failed startup attempts, and the
separate two-class living/non-living experiment are outside this comparison.

These are preserved historical results, not a new training or inference run.
Run IDs and hashes of the original evidence are in [provenance.json](provenance.json).
The full original checkpoints, optimizer/resume artifacts where available,
per-image predictions, and datasets remain local.

## Shared Configuration

- Backbone: pretrained `convnextv2_large.fcmae_ft_in22k_in1k`, fine-tuned end to
  end; RGB 128 x 128; 20 output targets, not 20 biological species.
- Same mapped dataset and split: 3,309,950 training, 413,735 validation and
  413,764 test images. Target-stratified image-row 80/10/10 allocation, split
  seed 20260421; not source/site-held-out. The original split manifest SHA-256
  is `51639823de20d7587137eabdc3255786a8ab4512319988b5345ae363b376828f`.
- Same label order, mapping and split hashes across all four source records.
  Main-source and additional EcoTaxa data are included; the current mutable
  manifest is not a substitute for these historical inputs.
- Training seed 42; 40 epochs; batch size 192; AdamW; initial LR 0.0001;
  weight decay 0.08; cosine schedule with 6 warmup epochs.
- Label smoothing 0.08; `panaiotis_relative` class weights, exponent 0.22;
  drop path 0.15; EMA decay 0.9998. Best EMA checkpoint selected by validation
  macro F1, not by the final test results.
- AMP enabled; `torch.compile(mode="reduce-overhead")`; training workers 8,
  test workers 0. These are recorded settings, not a portable speed claim.
- Training transform: timm ImageNet-style random resized crop (RRC), aspect
  ratio 0.75-1.3333, color jitter 0.4, horizontal flip probability 0.5.
  The crop area and RandAugment settings differ below.
- Single-view evaluation: bicubic shorter-edge resize to 146, center crop
  128 x 128, ImageNet mean/std normalization. No multicrop or test-time augmentation.

[configurations.json](configurations.json) contains shared settings once and
per-line changes separately. A0's omitted crop fields are resolved using the
training transform defaults. These are descriptive historical settings, not
runnable configurations containing private dataset paths or monitoring credentials.
The original historical dependency environment is not independently pinned.

| Line | Variant | RRC area fraction | RandAugment | Selected EMA epoch | Public weights |
|---|---|---|---|---:|---|
| A0 | clean-CE anchor | 0.08-1.00 | `rand-m9-mstd0.5-inc1` | 32 | No |
| A1 | `rrc_scale50` | 0.50-1.00 | `rand-m9-mstd0.5-inc1` | 40 | No |
| A2 | `ra_m4` | 0.08-1.00 | `rand-m4-mstd0.5-inc1` | 40 | [Download](https://github.com/mm1719/PICASSO-Models/releases/tag/a2-20-target-v1) |
| A3 | `ra_off` | 0.08-1.00 | Off | 36 | No |

A1's saved training config disabled automatic test evaluation. Its final test
was recovered separately after correcting launcher configuration; the preserved
test metrics and packaged class/group tables are present and included here.
This is not an untested line, and its original config has not been rewritten.

## Validation at the Selected Checkpoint

These values come from each original training-loop epoch log. Accuracy is a
percentage below; other metrics are fractions. The later deterministic paired
audit uses a different evaluation export and is reported separately, not
silently substituted for this table.

| Line | Accuracy (%) | Balanced accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|---:|
| A0 | 93.9369 | 0.841732 | 0.811410 | 0.939759 |
| A1 | 93.8739 | 0.824383 | 0.816188 | 0.938777 |
| A2 | 94.0696 | 0.851781 | 0.819759 | 0.941046 |
| A3 | 93.9546 | 0.817184 | 0.781874 | 0.939907 |

Exact saved values: [validation_metrics.csv](validation_metrics.csv).

## Final Test

All four use the same 413,764-row, 20-target test cohort and their selected EMA
checkpoint. No test results were recomputed for this publication.

| Line | Accuracy (%) | Balanced accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|---:|
| A0 | 93.8494 | 0.833975 | 0.786894 | 0.938899 |
| A1 | 93.8136 | 0.825647 | **0.820985** | 0.938183 |
| A2 | **93.9927** | 0.833754 | 0.789876 | **0.940289** |
| A3 | 93.8719 | 0.823805 | 0.788522 | 0.939079 |

[test_metrics.csv](test_metrics.csv) retains unrounded top-1 through top-5,
balanced accuracy, macro/weighted precision, recall and F1. Balanced accuracy
is macro recall. Macro F1 gives each of the 20 targets equal weight; weighted
F1 weights by true test support. Neither is an average across training seeds.

[classwise_test_metrics.csv](classwise_test_metrics.csv) contains 80 rows
(20 targets x 4 lines), with exact label indices, train/validation/test support,
precision, recall and F1. A target's recall is accuracy conditional on its true
label; we do not duplicate binary one-vs-rest accuracy as per-class accuracy.

[grouped_test_accuracy.csv](grouped_test_accuracy.csv) contains top-1/3/5
accuracy by target support group. `sample_range` uses each target's **whole
mapped dataset count**, not its training count or test count. `num_samples` is
the number of test images whose true labels belong to that group. Group
accuracy is image-weighted exact-label accuracy within that subset, not
accuracy after collapsing predictions into support groups. Values ending in
`_pct` are percentages; empty support bins are omitted. Each line's groups
sum to 20 targets and 413,764 test rows.

## Why A2 Is the Public Model

The original promotion gate required improvements in both validation macro F1
and balanced accuracy over A0. A1 improved validation macro F1 but reduced
balanced accuracy; A3 reduced both. A2 improved both point estimates, and was
selected as the provisional candidate. The higher A1 test macro F1 is disclosed
above; test ranking did not replace the precommitted validation gate.

A later audit aligned 413,735 deterministic validation predictions from A0 and
A2, then ran 1,000 paired, class-stratified bootstrap replicates (seed 20260820):

| Metric | A0 | A2 | A2 minus A0 | 95% bootstrap interval for difference |
|---|---:|---:|---:|---|
| Macro F1 | 0.812881 | 0.819764 | +0.006882 | [-0.005235, +0.018831] |
| Balanced accuracy | 0.843816 | 0.851780 | +0.007964 | [-0.008977, +0.024990] |

Both intervals include zero. The four high-support targets (at least 5,000
validation images: Cyanobacteria, Heterokontophyta, Myzozoa and detritus) have
nonnegative F1 point differences, but that is not a proof of improvement for
every target or every seed. Exact global/high-support results are in
[paired_validation_audit.json](paired_validation_audit.json); all 20 target
differences and intervals are in [paired_validation_classwise.csv](paired_validation_classwise.csv).

These intervals are conditional on this cohort and do not model training-seed
or acquisition/source uncertainty. Tiny classes limit inference; Echinodermata
has only two validation and two test images. Second-seed A0/A2 replication,
final scientific promotion, and a combined A4 experiment remain deferred.
Choosing one public download does not claim A2 is conclusively superior.

## Publication Boundaries

Only compact aggregate results, configuration summaries, run identifiers and
source hashes are published. No images, individual prediction rows, input
paths, W&B payloads, or non-A2 weights are included. Provenance hashes identify
preserved local evidence; they do not make private datasets publicly reproducible.
`SHA256SUMS` covers this report and its data files, excluding itself.

The same [data-source limitations](../../a2/DATA_PROVENANCE.md),
[weight terms](../../a2/LICENSE.md), and
[bounded privacy-audit caveats](../../a2/PRIVACY_EVALUATION.md) still apply.
Neither publication nor aggregate test performance resolves source-rights
uncertainty, image-level split dependence, or cross-instrument generalization.
