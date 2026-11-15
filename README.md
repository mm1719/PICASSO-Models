# PICASSO Models

**PICASSO 20-Class Plankton Classifier (A2)** is the only downloadable model in
this repository. It is a noncommercial ConvNeXt V2-L classifier for FlowCAM
plankton and particle image crops, with 20 mixed taxonomic/particle targets,
not 20 species.

**What A2 means:** `R3S2` identifies Round 3, Stage 2, and `A2` identifies its
second augmentation-ablation variant after the A0 baseline. It keeps A0's
ConvNeXt V2-L architecture, 20-target label space and crop settings, while
reducing RandAugment magnitude from 9 to 4 (`ra_m4`). This is an experiment
identifier, not a second-generation architecture, release version or performance
rank. The public model name remains **PICASSO 20-Class Plankton Classifier**.

## Download A2

From the [A2 release](https://github.com/mm1719/PICASSO-Models/releases/tag/a2-20-target-v1),
download `model.safetensors` and
`PICASSO-20-Class-Plankton-Classifier-metadata.zip`. Extract the metadata ZIP,
put the weight in its `PICASSO-20-Class-Plankton-Classifier/` folder, and run
`sha256sum -c SHA256SUMS` there. Follow [the inference guide](a2/README.md).
Use this metadata ZIP rather than the historical automatic source archive.

- Architecture: ConvNeXt V2-L; internal experiment R3S2-A2, EMA epoch 40.
- Weight: 785,841,008 bytes; all 380 float32 tensors, not a reduced classifier head.
- SHA-256: `0865ff896cfd9f72509a819f19388dd8c3dc0da3e6befe84ce9ffede19334394`.
- Frozen RGB evaluation: bicubic shorter-edge resize to 146, center crop 128,
  ImageNet normalization; no test-time augmentation.
- [Model card](a2/MODEL_CARD.md), [labels](a2/labels.json),
  [saved test metrics](a2/metrics.json), [conversion validation](a2/VALIDATION.md).

This is a complete inference weight export in safetensors, **not a resumable
training checkpoint**. Optimizer/scheduler state, local configuration, original
checkpoints, and other models remain local. The old 23-target release and its
download tag are retired. Git history is preserved, not erased; historical
snapshots can still contain obsolete files.

## Training Results

[R3S2 A0-A3 results](experiments/round03_stage02/README.md) publish the four
completed 20-target experiments: shared/differing configurations, validation
and test metrics, per-class and support-group results, and the A2-versus-A0
paired validation audit. These summaries do not add model downloads.

A2 is the selected public model, not the winner of every test metric: A1 has
the highest observed test macro F1. A2 passed the original joint validation
point-estimate gate, but both global gain intervals include zero and second-seed
replication remains deferred. No new training or test inference was run for
this publication.

## Terms and Limits

Weights are **CC BY-NC 4.0**; no separate software/documentation license is
selected. Read [license scope](a2/LICENSE.md) and [attribution](a2/ATTRIBUTION.md).
Exact image-source terms for 47 additional EcoTaxa projects were not independently
established: [provenance and unresolved terms](a2/DATA_PROVENANCE.md).
Research-unit consent is not a grant from every external data provider.

The image-row split does not establish source/site generalization. A bounded
membership-inference audit measured a weak signal, not zero leakage:
[methods and limits](a2/PRIVACY_EVALUATION.md). No original images, per-image
predictions, credentials, or executable pickle checkpoints are distributed.

Related: [PICASSO application](https://github.com/mm1719/PICASSO),
[training workflow](https://github.com/mm1719/PICASSO-Training),
[taxonomy review](https://github.com/mm1719/PICASSO-Taxonomy-Review).
