import torch
import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from transformers.utils import logging
logging.set_verbosity_error()

# Path to the audio file to transcribe
AUDIO_FILE = "speech.wav"

# Choose the Whisper model variant from Hugging Face
MODEL_NAME = "openai/whisper-base"

# Use GPU if available, otherwise fall back to CPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load the tokenizer/processor and the model
processor = WhisperProcessor.from_pretrained(MODEL_NAME)
model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME).to(DEVICE)

# Load and resample the audio file to 16 kHz
audio, sr = librosa.load(AUDIO_FILE, sr=16000)

# Convert audio to input features (log-Mel spectrogram)
inputs = processor(audio, sampling_rate=sr, return_tensors="pt").input_features.to(
    DEVICE
)

# Run inference to generate token IDs
with torch.no_grad():
    predicted_ids = model.generate(inputs)

# Decode the predicted token IDs into text
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print()
print("Transcription:")
print()
print(transcription.strip())
print()
