import gradio as gr
import soundfile as sf
import numpy as np
import librosa

OUTPUT_WAV = "speech.wav"
TARGET_SR = 16000  # Whisper expects 16 kHz


def save_audio(audio):
    if audio is None:
        return None
    sample_rate, data = audio

    # Convert to float32 and scale to [-1.0, 1.0] if input is int16
    if not np.issubdtype(data.dtype, np.floating):
        data = data.astype(np.float32) / 32768.0

    # Resample to 16 kHz if needed
    if sample_rate != TARGET_SR:
        data = librosa.resample(data, orig_sr=sample_rate, target_sr=TARGET_SR)
        sample_rate = TARGET_SR

    # Clip and convert back to int16 for 16-bit PCM WAV
    data = np.clip(data, -1.0, 1.0)
    data = (data * 32767).astype(np.int16)

    # Save as mono WAV
    sf.write(OUTPUT_WAV, data, sample_rate)
    return OUTPUT_WAV


with gr.Blocks() as demo:
    gr.Markdown("# 🎙️ Record Audio for Whisper")
    gr.Markdown(
        "Speak into your microphone. The audio will be saved as a 16 kHz WAV file."
    )

    audio_input = gr.Audio(type="numpy", label="Microphone Input")
    record_button = gr.Button("Save Recording")
    output_file = gr.File(label="📁 Download WAV (16 kHz)")
    record_button.click(fn=save_audio, inputs=audio_input, outputs=output_file)

demo.launch(server_name="0.0.0.0", share=True)
