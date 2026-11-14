# Release verification

## Scope

Safe-format conversion of the R1 EMA checkpoint, not retraining or a new scientific evaluation. Source artifacts were read-only. No original images were used and no network or GPU was used during equivalence verification.

1. Statically parse protocol-2 metadata into inert descriptors. Unknown globals/opcodes and invalid shapes/offsets are rejected. Never invoke `torch.load`, `pickle.load`, or pickle callables.
2. Copy 380 dense float32 tensor storages directly from the source ZIP into safetensors; compare SHA-256 independently for every tensor. All match.
3. Reconstruct the original tensors from raw bytes, strictly load the same local timm architecture with `pretrained=False`, then compare to the safetensors-loaded tensors. All values match.
4. On four synthetic RGB images (gradient, checkerboard, seeded noise, and white), run both forms in eval mode on CPU with deterministic settings. All logits are finite and bitwise equal; max absolute difference is 0.
5. Compare the frozen explicit RGB/resize/crop/normalization preprocessing with the source-code evaluation-transform factory. All four input tensors are bitwise equal.

6. Run the published CPU inference helper on a generated grayscale PNG; verify RGB conversion, top-5 label mapping, rejection of a non-R1 bundle, and rejection of an incorrect weight checksum. All pass with network blocked.

The static exporter passed nine rejection/safety tests and an independent review. A separate reviewer verified complete safetensors coverage, all tensor hashes, absence of private header paths, and the equivalence procedure.

Machine-readable details, exact package versions, and source/export checksums are in `validation.json`. The exported weight SHA-256 is:

```text
553573b91469b2029ac72612ae473251208e629545ecce234095cdaed381ff34
```

The original checkpoint and private audit scripts are not distributed. The original checkpoint hash provides provenance; only the sanitized safe-format export is a release asset.

## What this does not establish

- It does not reproduce the historical 407,596-row test set or prove external generalization.
- It does not establish the exact software versions used in historical training.
- It is not a membership-inference, memorization, dataset-deduplication, or privacy audit.
- It does not prove equivalent outputs on different hardware, library versions, or all possible inputs.
- It does not make the 23-target historical R1 weight file compatible with the 20-target A2 application.
