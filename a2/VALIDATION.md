# PICASSO 20-Class Plankton Classifier: conversion and inference verification

Architecture: ConvNeXt V2-L. Internal experiment trace: R3S2-A2.

## Original conversion checks

This is safe-format conversion of the A2 20-target EMA epoch-40 checkpoint, not retraining or a scientific test-set rerun. Original artifacts were read-only. No original images were used, no GPU was used, and network access was blocked during the original conversion verification. Subsequent installation and CUDA checks are recorded separately below.

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
`9f57ea912514206799ed788f8328e53627660ea8` were unchanged by that naming and
documentation refresh. This was additional package/CPU smoke verification,
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

Those initial smoke checks used the existing Linux x86_64 / Python 3.11.15
research environment; fresh Models installation had not yet been tested.
That gap was addressed by the subsequent check below. The separately reported
PICASSO-Training fresh-environment check covers only its model-free evaluation
dependencies, not this model stack.
Licenses, source-rights qualifications and privacy-audit limitations are unchanged.

## 2026-11-15 fresh installation and CPU inference

The published weight, metadata ZIP and checksum file were downloaded again.
Their digests matched the release, and the downloaded metadata matched main
commit `92d3763d567f18b257668d52f6de84c4f4edf2ba`. The executable helper,
requirements, labels, configuration and weights were unchanged by that
documentation-only refresh. The later device-selection change is recorded
separately below; requirements, labels, configuration and weights remain fixed.

A new Python 3.11.15 venv started with only pip 24.0 and setuptools 79.0.1,
with system site-packages disabled. The existing Python executable and standard
library were reused read-only; this was an isolated package installation, not
a new operating system. All six model dependencies came from the new venv.
The existing research environment's package and file-metadata inventories were
identical before and after testing.

Installation used the README's unmodified requirements from public PyPI, with
local pip configuration, extra indexes and caches disabled. No alternative
CPU-wheel source was substituted. Direct dependency versions are those in
the runtime list above; runtime torch identifies itself as `2.11.0+cu130`.
Linux kernel was `7.0.0-43-generic`, x86_64, with glibc 2.43.

| Check | Result |
| --- | --- |
| Fresh requirements installation | Exit 0 |
| `pip check` | Exit 0; no broken requirements |
| `sha256sum -c SHA256SUMS` | Exit 0; all 18 entries OK |
| Generated RGB 161 x 109 PNG through the documented CLI | Exit 0 |
| Generated grayscale 161 x 109 PNG through the same CLI | Exit 0 |
| Supplemental CPU forward with Python socket connections blocked | Passed; output exactly matched the RGB CLI |
| Incorrect model identifier | Rejected before model construction |
| Incorrect expected weight checksum | Rejected before model construction |
| Empty expected weight checksum | Rejected before model construction |
| Corrupt weight fixture | Rejected before model construction |
| Invalid label indices | Rejected before model construction |

The combined verification script passed eight inference/rejection checks.
Both CLI results had five distinct indices, exact label-map matches, finite
scores in [0, 1], descending scores and a top-five sum no greater than 1 within
floating-point tolerance. The supplemental forward recorded CPU parameters,
CPU input/output tensors and finite `[1, 20]` logits. CUDA devices were hidden
and CUDA was not initialized during these CPU checks. Invalid inputs were
separate fixtures; the real bundle was not corrupted.

Default PyPI installation includes NVIDIA/CUDA libraries inside the venv,
which occupied approximately 4.8 GiB excluding the weight file. No host driver
or system CUDA package was changed. Exact transitive versions, pip's install
report, generated fixtures and command outputs are retained in the private
verification archive. Direct requirements are pinned, but future transitive
resolution can differ. These synthetic checks are not an accuracy evaluation.

## 2026-11-15 separate CUDA model smoke

The same isolated environment and checksum-verified release weight also passed
a short FP32 CUDA model test on NVIDIA GeForce RTX 5090 (compute capability
12.0), driver 580.178.04, torch `2.11.0+cu130`, CUDA runtime 13.0.

- The process held the host's shared exclusive GPU lock for the whole check.
  The lock was released normally and no compute process remained afterward.
- The same frozen preprocessing produced a `[2, 3, 128, 128]` batch from the
  two generated RGB/grayscale images. The model was loaded strictly with
  `pretrained=False`; both model parameters and inputs were explicitly moved
  to CUDA. Python socket connection calls were blocked during model evaluation.
- Three GPU forward passes produced finite `[2, 20]` logits on `cuda:0`.
  FP32 was used without autocast; TF32 and cuDNN benchmarking were disabled.
- All three passes matched CPU top-five indices. Maximum absolute logit
  difference was `1.430511474609375e-6`; maximum softmax-score difference was
  `2.384185791015625e-7`. Logits passed `atol=1e-4, rtol=1e-4` comparisons.

This establishes a successful CUDA forward on this host and these inputs, not
bitwise CPU/GPU equivalence or full-dataset parity. The public `infer.py` was
not changed during that separate smoke test; it was still CPU-only then.
The subsequent public device-selection implementation is verified below.

## 2026-11-15 CPU/CUDA helper and regression tests

The helper now accepts `--device cpu` or `--device cuda`, defaulting to CPU.
The Python API remains compatible with two-argument calls:
`predict(image_path, bundle, device="cpu")`. CUDA requests require available
CUDA and never silently fall back to CPU. Both the model and input move to the
requested device; strict weight loading, checksum checks, labels, preprocessing
and top-five JSON fields remain unchanged. No new dependency was added.

The same isolated Python 3.11.15 environment was reused without changing the
research environment. A failing test first demonstrated the missing device
argument; the implementation and regression suite then passed all 13 tests.
The shipped `test_infer.py` uses real CPU tensors, transforms and temporary
safetensors with a tiny model substituted for timm architecture construction.
It requires no release weight or GPU and checks:

- Default and explicit CPU outputs agree without probing CUDA.
- RGB/grayscale inputs retain the expected label and score structure.
- Unsupported devices are rejected; CLI help documents both supported choices.
- Hidden/unavailable CUDA produces a nonzero CLI exit with an actionable error.
- A simulated CUDA transfer failure propagates without a CPU retry.
- Wrong/empty checksums, corrupt weights, a wrong model ID and invalid label
  indices are rejected before model construction.

Real A2-weight integration checks additionally ran the actual CLI for two
generated images (RGB and grayscale), each with default CPU, explicit CPU and
explicit CUDA: six successful invocations, all exit 0. CPU JSON outputs exactly
matched the prior CPU-only helper. GPU top-five indices matched CPU for both
inputs, with finite scores and the same output schema.

Supplemental forward hooks verified CPU/CUDA model parameters and input/output
devices, with finite `[1, 20]` logits. On RTX 5090 / driver 580.178.04 /
torch `2.11.0+cu130`, the new helper used float32 tensors and unchanged PyTorch
backend defaults (`matmul.allow_tf32=False`, `cudnn.allow_tf32=True`). Maximum
absolute CPU/GPU logit differences were `2.913475036621094e-4` for RGB and
`7.62939453125e-6` for grayscale. Maximum softmax differences were
`4.9591064453125e-5` and `7.748603820800781e-7`, respectively. Logits passed
`atol=1e-4, rtol=1e-3` comparisons. These checks differ from the earlier
TF32-disabled standalone smoke; neither establishes all-input parity.

All GPU integration checks held the host's shared GPU mutex; the public helper
itself intentionally has no host-specific locking dependency. Network socket
connections were blocked during supplemental model forwards. Staged and
re-downloaded packages are checked against 19 checksum entries, including the
new test file and unchanged weight. The release tag, weight asset, licenses,
labels, configuration, saved metrics and historical conversion JSON are retained.

## Not established by these checks

- Historical 413,764-image test performance was not rerun; the saved metrics are explicitly historical.
- Historical upstream weight revision and original package versions are not independently pinned.
- The conversion checks themselves are not privacy evidence. A separate bounded membership-inference and limited overlap audit is documented in [PRIVACY_EVALUATION.md](PRIVACY_EVALUATION.md); it does not cover full content/near-duplicate overlap, acquisition correlation, image reconstruction, stronger white-box attacks, or differential privacy.
- Other GPUs/CPUs, Python versions, Windows/macOS and a separate host without NVIDIA drivers were not tested. The single-GPU smoke does not establish all-input equivalence, mixed-precision/compiled inference, throughput, cross-instrument generalization or production application integration.
- Conversion verification does not establish third-party rights or override unverified source contracts.
- The tensor-only package is not a drop-in replacement for software expecting the original checkpoint container. It must not be paired with incompatible weights or labels from another model version.
