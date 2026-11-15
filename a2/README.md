# PICASSO A2: 20-target FlowCAM classifier

**Release `a2-20-target-v1`: noncommercial, 20-target A2 weights.**

A tensor-only export of PICASSO's A2 EMA epoch-40 ConvNeXt V2-L classifier. This is the **20-target A2 model**, not the separately released 23-target [R1 historical baseline](https://github.com/mm1719/PICASSO-Models/releases/tag/r1-historical-baseline-v1). The targets include coarse taxonomic groups and non-taxonomic categories; they are not 20 species.

- RGB input; frozen 128 × 128 evaluation pipeline.
- Original saved test results: **93.9927% top-1**, **0.789876 macro F1**, 413,764 image rows. These were not rerun for this package and are not a cross-source benchmark.
- Safe-format weights, exact labels/configuration, checksums, inference helper, provenance, and conversion validation. No original images, per-image exports, machine-local paths, or training checkpoint pickle.
- **Weights: CC BY-NC 4.0.** Noncommercial only; preserve notices. Other repository files do not have a separately selected software/documentation license. See [LICENSE.md](LICENSE.md).

## Important source-rights disclosure

The six principal datasets have identified public statements. A2 also used 48 EcoTaxa projects; an exact image-dataset license was located for project 6015, but exact snapshot-specific terms for the other 47 were not independently established. This package does not claim that all third-party rights are cleared, nor that source licenses automatically apply to learned parameters. Research-unit consent to release the model is confirmed. [Model card](MODEL_CARD.md), [attribution](ATTRIBUTION.md), and [project-level evidence](DATA_PROVENANCE.md) explain the limits without distributing source data.

## Local inference

From the [A2 release](https://github.com/mm1719/PICASSO-Models/releases/tag/a2-20-target-v1), download `model.safetensors` and the Source code archive. In the extracted archive, enter the **`a2/` directory** and place the weight file beside `config.json`. The weight is a separate release asset, not in the source archive. Verify `SHA256SUMS` from inside `a2/`. Do not use the R1 asset with A2 labels.

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

[VALIDATION.md](VALIDATION.md) separates conversion checks from historical scientific evaluation. R1 and A2 use different cohorts and labels, so their metrics are not a controlled comparison.
