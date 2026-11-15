# PICASSO 20-Class Plankton Classifier

**Release `a2-20-target-v1`: noncommercial, 20-target A2 weights.**

A tensor-only release of a **ConvNeXt V2-L** FlowCAM classifier. Internal experiment trace: **R3S2-A2**, EMA epoch 40. This is the only downloadable model in PICASSO-Models. The targets include coarse taxonomic groups and non-taxonomic categories; they are not 20 species.

- RGB input; frozen 128 × 128 evaluation pipeline.
- Original saved test results: **93.9927% top-1**, **0.789876 macro F1**, 413,764 image rows. These were not rerun for this package and are not a cross-source benchmark.
- Safe-format weights, exact labels/configuration, checksums, inference helper, provenance, and conversion validation. No original images, per-image exports, machine-local paths, or training checkpoint pickle.
- **Weights: CC BY-NC 4.0.** Noncommercial only; preserve notices. Other repository files do not have a separately selected software/documentation license. See [LICENSE.md](LICENSE.md).

## What A2 Means

`R3S2` means Round 3, Stage 2; `A2` is the second augmentation-ablation variant
after the A0 baseline. It retains A0's ConvNeXt V2-L architecture, 20-target
label space and crop settings, while reducing RandAugment magnitude from 9 to
4 (`ra_m4`). The identifier describes the experiment, not a second-generation
architecture, release version or performance rank. The public name is
**PICASSO 20-Class Plankton Classifier**. The release tag `a2-20-target-v1` and
`model_id=picasso-a2-v1` remain unchanged.

## Important source-rights disclosure

The six principal datasets have identified public statements. A2 also used 48 EcoTaxa projects; an exact image-dataset license was located for project 6015, but exact snapshot-specific terms for the other 47 were not independently established. This package does not claim that all third-party rights are cleared, nor that source licenses automatically apply to learned parameters. Research-unit consent to release the model is confirmed. [Model card](MODEL_CARD.md), [attribution](ATTRIBUTION.md), and [project-level evidence](DATA_PROVENANCE.md) explain the limits without distributing source data.

## Local inference

From the [model release](https://github.com/mm1719/PICASSO-Models/releases/tag/a2-20-target-v1), download **`model.safetensors`** and **`PICASSO-20-Class-Plankton-Classifier-metadata.zip`**. Extract the metadata bundle, enter its `PICASSO-20-Class-Plankton-Classifier/` folder, and put the weight beside `config.json`. Run `sha256sum -c SHA256SUMS` there. The metadata bundle contains no weights or original images. Use this bundle, not the historical automatic source archive. Do not mix weights or labels from other model versions.

The safetensors file contains the full inference model, not just its classifier head. It does not include optimizer/scheduler state and is not a checkpoint for resuming training. Original checkpoints and other experiment weights are retained locally.

The CPU helper was checked on Linux x86_64 with Python 3.11.15 and the recorded
dependencies. Fresh installation of this model-inference stack and other
platforms remain unverified; see [validation boundaries](VALIDATION.md).

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
sha256sum -c SHA256SUMS
python infer.py /path/to/your/own/crop.png
```

The helper uses CPU, checks the weight SHA-256, and never downloads pretrained weights. It reports top-5 labels and softmax scores, not calibrated probabilities or expert identifications. The original runtime's checkpoint container is not included; this is not advertised as a drop-in application replacement.

## Scope and limits

Use for noncommercial research and evaluation with domain review. Do not infer ecological reliability, cross-instrument generalization, or safety-critical suitability from aggregate scores. Some targets have very few test examples, and the split is image-level rather than source/site-held-out. A bounded matched membership-inference audit measured a weak signal (primary AUROC 0.5171; 95% interval 0.5071–0.5265). It is not a privacy guarantee or an image-reconstruction test; [methods and limits](PRIVACY_EVALUATION.md).

[VALIDATION.md](VALIDATION.md) separates conversion checks from historical scientific evaluation. [The same-cohort A0-A3 result summaries](https://github.com/mm1719/PICASSO-Models/blob/main/experiments/round03_stage02/README.md) include configuration differences and the paired validation audit. A2 is the selected public model, not a claim of the highest score on every metric or a confirmed multi-seed gain.
