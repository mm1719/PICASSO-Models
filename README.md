# PICASSO Models

Two separately versioned, noncommercial FlowCAM classifiers. **A2 and R1 are not interchangeable.**

| Model | Targets | Release and documentation |
|---|---:|---|
| **PICASSO 20-Class Plankton Classifier** (ConvNeXt V2-L; R3S2-A2) | 20 | [Model weights](https://github.com/mm1719/PICASSO-Models/releases/tag/a2-20-target-v1) · [Documentation](a2/README.md) · [model card](a2/MODEL_CARD.md) |
| R1 historical baseline, EMA epoch 27 | 23 | [Preserved R1 release](https://github.com/mm1719/PICASSO-Models/releases/tag/r1-historical-baseline-v1) · [original R1 documentation](https://github.com/mm1719/PICASSO-Models/tree/r1-historical-baseline-v1) |

A2 adds source-rights uncertainty disclosures and a bounded membership-inference audit that measured a weak signal, **not proof of zero leakage**. Read its [data provenance](a2/DATA_PROVENANCE.md), [audit limitations](a2/PRIVACY_EVALUATION.md), and [CC BY-NC weight terms](a2/LICENSE.md). No original images or individual audit records are distributed. Saved model accuracies use different labels/cohorts and are not a controlled comparison.

A2 files are in **`a2/`**. Top-level inference/configuration/model-card files remain the historical **R1** bundle. For R1's checksum-verified package, use the immutable R1 release/tag, not the current branch README. Both weight files are separate release assets and are not committed to Git.

---

## R1 historical baseline documentation

A transparent, reproducible release of a **historical PICASSO R1 baseline** for FlowCAM plankton and particle image classification.

> **R1, not A2.** This checkpoint has **23 mixed taxonomic/particle targets**, not 23 species. It is not the current 20-target A2 application model and is not a drop-in replacement for it.

## Download

From the [R1 historical-baseline release](https://github.com/mm1719/PICASSO-Models/releases/tag/r1-historical-baseline-v1), download `model.safetensors` and the **Source code (zip)** archive. Extract the archive, then place the weight file in its top-level folder beside `config.json`. The weight file is a separate release asset, not part of the Git source archive.

- Weight size: 785,859,452 bytes (about 786 MB).
- Weight SHA-256: `553573b91469b2029ac72612ae473251208e629545ecce234095cdaed381ff34`.
- Format: safetensors, 380 float32 tensors. No executable pickle checkpoint is distributed.
- License: **CC BY-NC 4.0 for weights**. Noncommercial sharing and adaptation are allowed under its terms; free download is not a commercial-use grant.

## What this release shows

The model fine-tunes a pretrained **ConvNeXt V2-L** backbone for a 23-target classification task using six recorded FlowCAM data sources. The bundle preserves the exact label order, frozen RGB preprocessing, source attribution, historical results, and checksums.

| Historical saved test result | Value |
|---|---:|
| Image rows | 407,596 |
| Top-1 accuracy | 93.0622% |
| Macro F1 | 0.683153 |
| Balanced accuracy | 0.733799 |
| Weighted F1 | 0.931467 |

These are **saved internal results, not a new benchmark run**. The split is image-row stratified, not held-out-source/site. Class imbalance is substantial; some targets have only 2 or 3 test examples. These numbers do not establish reliable performance across instruments, regions, or acquisition conditions, and should not be compared directly with A2's different label space and cohort.

## Local CPU inference

Use Python 3.11 in an isolated environment. The versions below were checked for this release; they are not a claim about the historical training environment.

```bash
python -m venv .venv
# Activate .venv using your shell's command.
python -m pip install -r requirements.txt
python infer.py /path/to/your/image.png
```

Place `model.safetensors` beside `infer.py`, `config.json`, and `labels.json`. The helper checks the weight checksum, constructs the architecture with `pretrained=False`, loads only safetensors, and runs on CPU. It does not download pretrained weights or upload your images. It prints five labels with **uncalibrated softmax scores**, not expert-confirmed probabilities of biological identity.

Preprocessing: RGB → bicubic shorter-edge resize to 146 → center crop 128 × 128 → [0, 1] → ImageNet mean/std normalization. Do not substitute the upstream pretrained model's 288-pixel test transform.

To verify all downloaded bundle files on a system with `sha256sum`:

```bash
sha256sum -c SHA256SUMS
```

## Validation

All 380 exported tensors match the original raw float32 storage byte-for-byte. Four synthetic-image CPU forward passes before and after conversion produced bitwise-equal logits (max absolute difference 0). Explicit preprocessing also matched the source-code evaluation factory. No untrusted pickle was executed, no real training/test images were read for these checks, and no original checkpoint was changed.

This validates conversion, **not test-set reproducibility or a privacy/memorization audit**. See [validation details](VALIDATION.md), [machine-readable results](validation.json), and the [model card](MODEL_CARD.md).

## Attribution and terms

- Original ConvNeXt V2 research: Woo et al. (2023); pretrained model distributed through [timm](https://huggingface.co/timm/convnextv2_large.fcmae_ft_in22k_in1k).
- PICASSO task-specific fine-tuning and release: [mm1719](https://github.com/mm1719).
- Six training-source credits and links: [ATTRIBUTION.md](ATTRIBUTION.md).
- Weights: CC BY-NC 4.0. Third-party notices retain their original terms. No separate software license is granted for the new helper in this release; public visibility is not an open-source license. See [license scope](LICENSE.md).

No raw images, per-image manifests, acquisition credentials, private source exports, or original training-checkpoint configuration are included. No data-provider or upstream-author endorsement is implied.

Related work: [PICASSO application](https://github.com/mm1719/PICASSO), [training workflow](https://github.com/mm1719/PICASSO-Training), [taxonomy review interface](https://github.com/mm1719/PICASSO-Taxonomy-Review).
