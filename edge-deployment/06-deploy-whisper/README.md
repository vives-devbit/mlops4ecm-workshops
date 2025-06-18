
# 🧠 Lab 07 — Deploy Whisper on the Edge (C++ & ONNX)

In this lab, we’ll take the Whisper model you've explored in Lab 06 and deploy it on a real ARM-based **edge device** using **C++** and **ONNX Runtime**. No Python. No Hugging Face. Just fast, efficient inference on the Rock 5B board — even with quantization to `int8`.

## 🧭 What is this lab about?

In previous labs, you worked with **Whisper** — a modern **audio transcription model** that converts spoken English into written text. You’ve already seen how the model is structured: an **encoder** processes the audio, and a **decoder** generates the text.

In this lab, we will:

1. Export the **entire Whisper pipeline** (from raw audio to text) as one big ONNX model — including:

   * Preprocessing (mel spectrogram)
   * Audio encoder
   * Text decoder
   * Postprocessing (token decoding)
2. Run this ONNX model using **ONNX Runtime** (Python)
3. Run it again — this time in a **C++ application**
4. Move everything to a real **ARM device** (Rock 5B board)
5. Add **int8 quantization** for maximum efficiency
6. Benchmark the speed difference 🚀

## 🚀 Step 1 — Export the full Whisper model

Connect to your virtual machine via VS Code (as always).
Navigate to the lab folder:

```bash
cd ~/mlops-workshops/edge-deployment/06-deploy-whisper/
```

Export the **monolithic** Whisper ONNX model:

```bash
python 04-export-whisper-onnx.py
```

This will generate:

```
whisper_end_to_end.onnx
```

✅ This ONNX file contains everything — even preprocessing and token decoding — thanks to custom operators from the **ONNX Runtime Extensions** library.

## 🎤 Step 2 — Run the model with ONNX Runtime (Python)

You’ll also need a test audio file. If you completed Lab 06, you already have `speech.wav`. If not, copy it over:

```bash
cp ../05-explore-whisper/speech.wav .
```

Then run the model with:

```bash
python 05-run-whisper-onnx.py
```

🎉 This should give you a transcription using only ONNX Runtime — no PyTorch or Transformers.

## 🛠 Step 3 — Compile the C++ application (on the server)

Let’s now compile and run a **C++ application** that uses this ONNX model.

```bash
cd 06-whisper-from-cpp/
mkdir build
cd build
cmake ..
make
./main
```

✔ This runs Whisper using C++ and the monolithic `whisper_end_to_end.onnx` model — on the server.

🧠 Make sure you're in the `build/` folder when running, because `main.cpp` expects relative paths like `../../speech.wav`.

## 🌍 Step 4 — Move to the Edge (Rock 5B board)

Now, SSH into your assigned **Rock 5B** board.

```bash
ssh radxa@<your-board-ip>
```

Clone the repo:

```bash
git clone https://github.com/AlexanderDhoore/<date>-mlops-workshops.git mlops-workshops/
```

Install the tools:

```bash
sudo apt update
sudo apt install cmake g++
```

Build the C++ app:

```bash
cd mlops-workshops/edge-deployment/06-deploy-whisper/07-whisper-on-arm/
mkdir build
cd build
cmake ..
make
```

Now, copy over the required files from your VM to the Rock 5B using **VS Code**:

* `speech.wav`
* `whisper_end_to_end.onnx`

Then run:

```bash
./main
```

🎉 Boom — Whisper runs **on ARM**, in **C++**, using **ONNX Runtime + Extensions**!

## 🧪 Step 5 — Quantize the model to `int8`

Let’s make it smaller and faster.

On the server:

```bash
python 04-export-whisper-onnx.py --precision int8
```

Copy this new `whisper_end_to_end.onnx` to your Rock 5B (overwrite the existing one).
Now run the model again on the Rock:

```bash
./main
```

## ⏱ Step 6 — Benchmark the performance

You can compare the inference time between the `fp32` and `int8` models. Use:

```bash
time ./main
```

Or add timing to `main.cpp` if you're curious.

You should see that the **int8 model runs significantly faster** — often around 2× speedup and 4× smaller file size.

## 🎓 Recap — What did we learn?

* You exported and ran a **monolithic Whisper ONNX model** including pre/postprocessing
* You ran it with **ONNX Runtime in Python**
* You ran it again in **C++**
* You moved the app to a real **ARM edge device**
* You quantized the model and benchmarked it

👏 This is a complete deployment pipeline — from model to edge inference.
