from onnxruntime_extensions import OrtPyFunction
import numpy as np
import onnxruntime as ort

AUDIO_PATH = "speech.wav"
MODEL_PATH = "whisper_end_to_end.onnx"

# Read audio as raw bytes
raw_audio = np.fromfile(AUDIO_PATH, dtype=np.uint8)
raw_audio = np.expand_dims(raw_audio, axis=0)

# Load model
model = OrtPyFunction.from_model(MODEL_PATH, cpu_only=True)

# Core inputs
inputs = [
    raw_audio,                           # audio_stream
    np.asarray([200], dtype=np.int32),   # max_length
    np.asarray([0], dtype=np.int32),     # min_length
    np.asarray([2], dtype=np.int32),     # num_beams
    np.asarray([1], dtype=np.int32),     # num_return_sequences
    np.asarray([1.0], dtype=np.float32), # length_penalty
    np.asarray([1.0], dtype=np.float32), # repetition_penalty
]

# Inference
text = model(*inputs)[0][0]

print()
print("Transcription:")
print()
print(text.strip())
print()
