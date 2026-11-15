"""CPU-only regression tests; no release weights or GPU are required."""
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import infer
from PIL import Image
from safetensors.torch import save_file


BUNDLE = Path(__file__).resolve().parent


class DeviceTests(unittest.TestCase):
    def test_unavailable_cuda_is_an_explicit_error(self):
        with patch.object(infer.torch.cuda, "is_available", return_value=False):
            with self.assertRaisesRegex(RuntimeError, "CUDA.*unavailable"):
                infer.predict(Path("missing.png"), Path("."), device="cuda")

    def test_unsupported_device_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "cpu.*cuda"):
            infer.predict(Path("missing.png"), Path("."), device="auto")

    def run_cli(self, *arguments):
        return subprocess.run(
            [sys.executable, str(BUNDLE / "infer.py"), *arguments],
            capture_output=True,
            text=True,
            timeout=30,
            env={**os.environ, "CUDA_VISIBLE_DEVICES": ""},
        )

    def test_cli_help_documents_devices(self):
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--device {cpu,cuda}", result.stdout)
        self.assertIn("default: cpu", result.stdout)

    def test_cli_rejects_unknown_device(self):
        result = self.run_cli("missing.png", "--device", "auto")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_cli_fails_when_cuda_is_hidden(self):
        result = self.run_cli("missing.png", "--device", "cuda")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CUDA was requested but is unavailable", result.stderr)
        self.assertIn("--device cpu", result.stderr)
        self.assertEqual(result.stdout, "")


class PredictionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.bundle = Path(temporary.name)
        self.image = self.bundle / "input.png"
        Image.new("RGB", (161, 109), (70, 120, 170)).save(self.image)
        self.labels = json.loads((BUNDLE / "labels.json").read_text())
        self.config = json.loads((BUNDLE / "config.json").read_text())
        self.weights = self.bundle / self.config["weights_file"]
        save_file(self.small_model().state_dict(), str(self.weights))
        self.config["weights_sha256"] = hashlib.sha256(
            self.weights.read_bytes()
        ).hexdigest()
        self.write_config()
        (self.bundle / "labels.json").write_text(json.dumps(self.labels))
        factory = patch.object(
            infer.timm, "create_model", side_effect=lambda *a, **k: self.small_model()
        )
        self.create_model = factory.start()
        self.addCleanup(factory.stop)

    @staticmethod
    def small_model():
        model = infer.torch.nn.Sequential(
            infer.torch.nn.AdaptiveAvgPool2d(1),
            infer.torch.nn.Flatten(),
            infer.torch.nn.Linear(3, 20),
        )
        with infer.torch.no_grad():
            model[-1].weight.zero_()
            model[-1].bias.copy_(infer.torch.arange(20))
        return model

    def write_config(self):
        (self.bundle / "config.json").write_text(json.dumps(self.config))

    def check_rows(self, rows):
        self.assertEqual([row["index"] for row in rows], [19, 18, 17, 16, 15])
        for row in rows:
            self.assertEqual(set(row), {"index", "target_id", "label", "softmax_score"})
            self.assertEqual(row["label"], self.labels[row["index"]]["label"])
            self.assertEqual(row["target_id"], self.labels[row["index"]]["target_id"])
            self.assertTrue(math.isfinite(row["softmax_score"]))
            self.assertGreaterEqual(row["softmax_score"], 0)
            self.assertLessEqual(row["softmax_score"], 1)

    def test_default_and_explicit_cpu_match_without_cuda_probe(self):
        with patch.object(
            infer.torch.cuda, "is_available", side_effect=AssertionError("CPU only")
        ):
            default = infer.predict(self.image, self.bundle)
            explicit = infer.predict(self.image, self.bundle, device="cpu")
        self.assertEqual(default, explicit)
        self.check_rows(default)
        self.assertFalse(self.create_model.call_args.kwargs["pretrained"])

    def test_grayscale_input_is_converted_to_rgb(self):
        Image.new("L", (161, 109), 90).save(self.image)
        self.check_rows(infer.predict(self.image, self.bundle, device="cpu"))

    def test_cuda_transfer_failure_does_not_fall_back(self):
        with patch.object(infer.torch.cuda, "is_available", return_value=True):
            with patch.object(
                infer.torch.nn.Module,
                "to",
                side_effect=RuntimeError("simulated CUDA transfer failure"),
            ) as transfer:
                with self.assertRaisesRegex(RuntimeError, "CUDA transfer failure"):
                    infer.predict(self.image, self.bundle, device="cuda")
        transfer.assert_called_once_with("cuda")

    def test_wrong_checksum_is_rejected_before_model_construction(self):
        self.config["weights_sha256"] = "0" * 64
        self.write_config()
        with self.assertRaisesRegex(ValueError, "Weight checksum mismatch"):
            infer.predict(self.image, self.bundle)
        self.create_model.assert_not_called()

    def test_empty_checksum_is_rejected_before_model_construction(self):
        self.config["weights_sha256"] = ""
        self.write_config()
        with self.assertRaisesRegex(ValueError, "Weight checksum mismatch"):
            infer.predict(self.image, self.bundle)
        self.create_model.assert_not_called()

    def test_corrupt_weight_is_rejected_before_model_construction(self):
        self.weights.write_bytes(b"invalid weight fixture")
        with self.assertRaisesRegex(ValueError, "Weight checksum mismatch"):
            infer.predict(self.image, self.bundle)
        self.create_model.assert_not_called()

    def test_wrong_model_id_is_rejected(self):
        self.config["model_id"] = "wrong"
        self.write_config()
        with self.assertRaisesRegex(ValueError, "supports only"):
            infer.predict(self.image, self.bundle)
        self.create_model.assert_not_called()

    def test_invalid_label_indices_are_rejected(self):
        self.labels[0]["index"] = 1
        (self.bundle / "labels.json").write_text(json.dumps(self.labels))
        with self.assertRaisesRegex(ValueError, "Invalid A2 label map"):
            infer.predict(self.image, self.bundle)
        self.create_model.assert_not_called()


if __name__ == "__main__":
    unittest.main()
