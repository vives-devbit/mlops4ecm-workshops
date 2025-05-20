import argparse
import os
import subprocess
import onnx
import onnxruntime as ort
from transformers import WhisperProcessor
from onnxruntime_extensions import util
from onnxruntime_extensions.cvt import gen_processing_models

# Configuration constants
MODEL_NAME = "openai/whisper-base"
CACHE_DIR = "whisper_cache_dir"
OUTPUT_DIR = "whisper_model_dir"
FINAL_MODEL = "whisper_end_to_end.onnx"

def export_core_model(optimize: bool, precision: str):
    print("Exporting Whisper ONNX model from Huggingface model hub...")
    cmd = [
        "python", "-m", "onnxruntime.transformers.models.whisper.convert_to_onnx",
        "-m", MODEL_NAME,
        "--cache_dir", CACHE_DIR,
        "--output", OUTPUT_DIR,
        "--precision", precision,
    ]

    if optimize:
        cmd.append("--optimize_onnx")

    subprocess.run(cmd, check=True)

def build_e2e_model():
    print("Building end-to-end model, including pre/post-processing...")
    processor = WhisperProcessor.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)

    pre_model, post_model = gen_processing_models(
        processor,
        pre_kwargs={"USE_AUDIO_DECODER": True, "USE_ONNX_STFT": True},
        post_kwargs={},
        opset=17
    )

    core_model_path = os.path.join(OUTPUT_DIR, "whisper-base_beamsearch.onnx")
    core_model = onnx.load(core_model_path)

    e2e_model = util.quick_merge(pre_model, core_model, post_model)
    onnx.save(e2e_model, FINAL_MODEL)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Whisper model to ONNX with optional optimization and precision.")
    parser.add_argument("--optimize", action="store_true", help="Enable ONNX graph optimization.")
    parser.add_argument("--precision", choices=["fp32", "fp16", "int8"], default="fp32", help="Precision format for the exported model.")

    args = parser.parse_args()

    export_core_model(optimize=args.optimize, precision=args.precision)
    build_e2e_model()

    print()
    print("DONE End-to-end model was created successfully.")
    print()
