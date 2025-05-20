# 🧪 Lab 05 – Explore Whisper Model through ONNX

In this lab, you'll explore the **Whisper model** from OpenAI — a transformer-based model for **automatic speech recognition (ASR)**, also known as **audio transcription**.

You’ll learn:
- What Whisper is and how it works
- How to run it using Hugging Face Transformers
- How to export parts of the model to ONNX format
- How to **visually explore the model** using Netron
- How **quantization** affects the model size and structure

## 🧠 What Is Whisper?

Whisper is a deep learning model that can **transcribe spoken language** into written text. You give it a short audio recording, and it tells you what was said.

It’s built using a **transformer architecture**, just like BERT or GPT — which you’ve seen in earlier labs. Specifically, Whisper uses:

- An **encoder**, which processes the input audio (as a mel spectrogram)
- A **decoder**, which generates text token-by-token, conditioned on the encoder's output

<img src="../../media/openai-whisper-architecture.png" style="width: 100%">

## 🎯 Goal of This Lab

Your goal in this lab is **not to train Whisper**, but to understand how it works by:
- Running it once with Hugging Face
- Exporting parts of the model to ONNX
- Opening those ONNX models in [Netron](https://netron.app/)
- Understanding what you’re looking at: **encoders**, **decoders**, and what happens during **quantization**

## 🛠️ Step 1 – Connect to Your VM

As always, start by connecting to your assigned **virtual machine** using **Visual Studio Code** with remote SSH.

Then activate the Python environment and install the required packages:

```bash
source ~/mlops-workshops/.venv/bin/activate
cd ~/mlops-workshops/edge-deployment/05-explore-whisper
pip install -r requirements.txt
````

## 🎙️ Step 2 – Record Some Audio

We’ll begin by recording a short audio clip.

Run the Gradio app:

```bash
python 01-record-audio-app.py
```

You’ll see two URLs printed:

```
* Running on local URL:  http://0.0.0.0:7860
* Running on public URL: https://...gradio.live
```

⚠️ **Use the public URL** (HTTPS is required for microphone access in most browsers)

Open the URL in your browser and record yourself saying something **in English**. Click “Save Recording” and download the WAV file if you want to keep it. The file will also be saved as `speech.wav` in your VM.

## 🧾 Step 3 – Transcribe with Hugging Face

Run the second script to transcribe your audio file:

```bash
python 02-whisper-huggingface.py
```

This uses Hugging Face Transformers to load the Whisper model and run inference. You'll see something like:

```
Transcription:

Hello, my name is Alexander and I'm a teacher at VIVES University of Applied Sciences.
```

Nice! 🎉 You just did state-of-the-art transcription using a transformer model — directly on your VM.

🧠 **Why Hugging Face?**
It’s easy to use, great for exploration and prototyping. But for edge deployment, we want something more lightweight — like ONNX.

## 📦 Step 4 – Export Encoder and Decoder to ONNX

Now let’s export the Whisper **encoder** and **decoder** separately to ONNX format, so we can explore them visually.

Run:

```bash
python 03-export-encoder-decoder.py
```

You’ll see a lot of logs — including some ONNX runtime warnings. You can ignore those for now.

The script creates two files:

* `whisper_model_dir/whisper-base_encoder.onnx`
* `whisper_model_dir/whisper-base_decoder.onnx`

## 💻 Step 5 – Download and Explore in Netron

Open the **file explorer in VS Code**, right-click the ONNX files, and choose **Download**.

Visit [https://netron.app](https://netron.app) and **open the encoder model** first.

### 👀 What to Look For

* The encoder starts with a **stack of transformer blocks** — each has self-attention and feedforward layers.
* At the end, you’ll see `LayerNorm` and many parallel branches — these are used to prepare attention **keys** and **values** for the decoder (called cross-attention heads).

Now open the **decoder model**.

* The decoder starts with embeddings and input tokens
* It includes layers for both **self-attention** and **cross-attention**
* The structure is more complex, but familiar: attention + residuals + normalization

## 🔬 Step 6 – Quantize the Model

Let’s try exporting a smaller version of the model using quantization.

Run:

```bash
python 03-export-encoder-decoder.py --precision int8
```

Or for half-precision:

```bash
python 03-export-encoder-decoder.py --precision fp16
```

This will generate files like:

* `whisper_model_dir/whisper-base_encoder_int8.onnx`
* `whisper_model_dir/whisper-base_decoder_int8.onnx`

## 📉 Step 7 – Compare File Sizes

Before opening them in Netron, compare the file sizes:

* `fp32` (default): \~90–300 MB
* `fp16`: roughly **half the size**
* `int8`: roughly **one-quarter the size**

You can see this easily in your file browser.

## 🧠 Step 8 – Visual Differences in Netron

Download and open the quantized models in Netron. Place your browser windows side-by-size with the standard fp32 models, to easily spot the differences.

### What’s Different?

You’ll notice:

* New layers like `DynamicQuantizeLinear`
* Many `MatMul` nodes replaced with `MatMulInteger`
* Possibly some reordering or structural simplification

This shows you how ONNX applies **quantization-aware operations** to reduce memory and speed up inference — especially useful on edge devices.

## ✅ Wrap-Up

You just:

* Explored the Whisper model in code and in structure
* Ran real audio transcription
* Exported the model for inspection
* Compared different model precisions and their visual graphs

In the next lab, you’ll take this further — combining preprocessing, inference, and decoding into a **single ONNX model** and deploying it on an embedded device.
