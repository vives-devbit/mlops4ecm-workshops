import argparse
import subprocess

# Configuration constants
MODEL_NAME = "openai/whisper-base"
CACHE_DIR = "whisper_cache_dir"
OUTPUT_DIR = "whisper_model_dir"

def export_encoder_decoder(optimize: bool, precision: str):
    print("Exporting Whisper encoder and decoder to ONNX (no pre/post-processing yet)...")
    
    cmd = [
        "python", "-m", "onnxruntime.transformers.models.whisper.convert_to_onnx",
        "-m", MODEL_NAME,
        "--cache_dir", CACHE_DIR,
        "--output", OUTPUT_DIR,
        "--precision", precision,
        "--no_beam_search_op",
    ]

    if optimize:
        cmd.append("--optimize_onnx")

    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Whisper encoder/decoder to ONNX (no preprocessing, no postprocessing).")
    parser.add_argument("--optimize", action="store_true", help="Enable ONNX graph optimization.")
    parser.add_argument("--precision", choices=["fp32", "fp16", "int8"], default="fp32", help="Precision format for the exported model.")

    args = parser.parse_args()

    export_encoder_decoder(optimize=args.optimize, precision=args.precision)

    print()
    print("DONE Exported encoder and decoder models.")
    print(f"Check the ONNX files inside '{OUTPUT_DIR}/'")
    print()
