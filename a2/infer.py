"""CPU or CUDA inference for the A2 classifier; never downloads weights."""
import argparse
import hashlib
import json
import os
from pathlib import Path

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")

import timm
import torch
from PIL import Image
from safetensors.torch import load_file
from torchvision import transforms
from torchvision.transforms import InterpolationMode


def predict(image_path, bundle, device="cpu"):
    if device not in ("cpu", "cuda"):
        raise ValueError("device must be 'cpu' or 'cuda'.")
    if device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError(
            "CUDA was requested but is unavailable. Check the NVIDIA driver and "
            "CUDA-enabled PyTorch, or use --device cpu."
        )
    config = json.loads((bundle / "config.json").read_text())
    labels = json.loads((bundle / "labels.json").read_text())
    if config["model_id"] != "picasso-a2-v1":
        raise ValueError("This helper supports only the 20-target A2 bundle.")
    if config["num_classes"] != 20 or [x["index"] for x in labels] != list(range(20)):
        raise ValueError("Invalid A2 label map.")
    weights = bundle / config["weights_file"]
    with weights.open("rb") as file:
        digest = hashlib.file_digest(file, "sha256").hexdigest()
    if digest != config["weights_sha256"]:
        raise ValueError("Weight checksum mismatch; obtain the matching A2 release asset.")
    torch.set_num_threads(4)
    model = timm.create_model(config["architecture"], pretrained=False,
                              num_classes=20, drop_path_rate=config["drop_path_rate"])
    model.load_state_dict(load_file(str(weights), device="cpu"), strict=True)
    model.to(device)
    model.eval()
    transform = transforms.Compose([
        transforms.Resize(config["resize_shorter_edge"],
                          interpolation=InterpolationMode.BICUBIC,
                          antialias=config["resize_antialias"]),
        transforms.CenterCrop(config["center_crop"]),
        transforms.ToTensor(),
        transforms.Normalize(config["mean"], config["std"]),
    ])
    with Image.open(image_path) as image:
        tensor = transform(image.convert("RGB")).unsqueeze(0)
    tensor = tensor.to(device)
    with torch.inference_mode():
        logits = model(tensor)
    if logits.shape != (1, 20) or not torch.isfinite(logits).all():
        raise ValueError("Invalid model output.")
    scores, indices = logits.softmax(dim=1)[0].topk(5)
    return [{**labels[index], "softmax_score": float(score)}
            for score, index in zip(scores.tolist(), indices.tolist())]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="A local RGB-compatible image crop")
    parser.add_argument("--bundle", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument(
        "--device", choices=("cpu", "cuda"), default="cpu",
        help="Inference device (default: cpu); cuda requires an available NVIDIA GPU",
    )
    args = parser.parse_args()
    print(json.dumps(predict(args.image, args.bundle, device=args.device), indent=2))
