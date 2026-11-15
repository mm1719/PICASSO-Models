# PICASSO 20-Class Plankton Classifier: conversion and inference verification

Architecture: ConvNeXt V2-L. Internal experiment trace: R3S2-A2.

## Passed checks

This is safe-format conversion of the A2 20-target EMA epoch-40 checkpoint, not retraining or a scientific test-set rerun. Original artifacts were read-only. No original images were used, no GPU was used, and network access was blocked during inference verification.

1. Statically interpreted protocol-2 metadata into inert descriptors. No pickle callable was executed; neither `torch.load` nor `pickle.load` was used. Unknown constructs are rejected. The parser passed nine rejection/safety tests.
2. Copied **380 dense float32 tensors**, totaling **785,802,320 tensor bytes**, from the checkpoint ZIP to safetensors. Per-tensor byte hashes, shapes, dtypes, offsets, and values all match.
3. Loaded original tensors reconstructed from raw bytes into the local timm model with `pretrained=False` and strict key checks, then separately loaded the exported tensors. Four synthetic RGB inputs (gradient, checkerboard, seeded noise, white) produced finite, **bitwise-identical logits**, maximum absolute difference **0**.
4. The frozen explicit RGB/resize/crop/normalization pipeline matched the source evaluation-transform factory bitwise for all four inputs.
5. The public inference helper passed a generated grayscale-PNG smoke test: RGB conversion, ordered top-5 label mapping, rejection of a non-A2 bundle, and rejection of an incorrect weight checksum.
6. An independent review checked labels/target IDs/metrics against saved evidence, complete nonoverlapping safe-format storage, classifier head `[20,1536]`, and absence of machine-local paths, credentials, personal contacts, or raw data in the public package. An independent tensor/header scan confirmed there are no extra payload bytes.
7. The original checkpoint SHA-256 was rechecked unchanged.

## Checksums and runtime

- Export bytes: **785,841,008**.
- Export SHA-256: `0865ff896cfd9f72509a819f19388dd8c3dc0da3e6befe84ce9ffede19334394`.
- Original checkpoint SHA-256: `32f4689c4894900bc2ae440bb17b553df10bd0444ad67b294652901a3b616430`.
- Runtime: Python 3.11.15; torch 2.11.0; torchvision 0.26.0; timm 1.0.26; safetensors 0.7.0; numpy 2.4.4; Pillow 12.2.0.

Original conversion results are in [validation.json](validation.json); the supplemental publication review below is documented separately. Every file in this A2 bundle and the weight asset is listed in `SHA256SUMS`; that file does not include itself. The source checkpoint and private audit scripts are not release assets.

## 2026-11-15 publication review

The executable helper, configuration and labels reviewed at commit
`9f57ea912514206799ed788f8328e53627660ea8` are unchanged by the naming and
documentation refresh. This is additional package/CPU smoke verification,
not a repeat of the original four-case conversion-equivalence study.

- The downloaded metadata ZIP matched the repository's `a2/` files. All 18
  `SHA256SUMS` entries passed, including the unchanged model weight. The local
  weight copy's hash matched the remote asset digest; its asset ID remained
  `749302585`. The large weight was not replaced or redownloaded for this review.
- The label map contains exactly 20 contiguous indices in the saved order.
- A generated grayscale 161 x 109 PNG passed the CPU helper: RGB conversion,
  finite top-five scores, distinct indices and exact matching label records.
  Network connection calls were blocked and CUDA devices were hidden.
- An incorrect model identifier and an incorrect expected weight checksum were
  both rejected. No GPU, real images, pickle checkpoint or external tracking
  was used for these smoke checks.
- The 20-target result-summary checksums and relative documentation links
  passed. Reachable historical file contents had no matches for the inspected
  credential/machine-local-path patterns; a pattern scan is not a complete
  privacy or secret-discovery guarantee.

The smoke checks used the existing Linux x86_64 / Python 3.11.15 research
environment. **A fresh installation of the Models inference dependencies was
not tested.** The separately reported PICASSO-Training fresh-environment check
covers only its model-free evaluation dependencies, not this model stack.
Licenses, source-rights qualifications and privacy-audit limitations are unchanged.

## Not established by these checks

- Historical 413,764-image test performance was not rerun; the saved metrics are explicitly historical.
- Historical upstream weight revision and original package versions are not independently pinned.
- The conversion checks themselves are not privacy evidence. A separate bounded membership-inference and limited overlap audit is documented in [PRIVACY_EVALUATION.md](PRIVACY_EVALUATION.md); it does not cover full content/near-duplicate overlap, acquisition correlation, image reconstruction, stronger white-box attacks, or differential privacy.
- No cross-hardware, GPU, all-input equivalence, cross-instrument generalization, or production application integration is claimed.
- Conversion verification does not establish third-party rights or override unverified source contracts.
- The tensor-only package is not a drop-in replacement for software expecting the original checkpoint container. It must not be paired with incompatible weights or labels from another model version.
