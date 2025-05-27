# 🧪 Lab 01 – First Steps with OLAMA

> Run your first LLM and vision models on a ROCK 5B embedded device. Then compare to GPU inference on a server. Discover the limits of local AI execution and get familiar with prompt-based interactions.

## 🎯 Objectives

- Run a large language model (LLM) on an embedded device (ROCK 5B)
- Interact with a vision-capable LLM
- Benchmark performance: CPU vs GPU
- Explore model selection on the Ollama platform

## 🖥️ Setup on the ROCK 5B

### 🔌 Step 1 – SSH into the Device

Each ROCK 5B is accessible on the network. Use the label on the device to find its IP:

```bash
ssh radxa@10.26.3.XX
# password: radxa
````

### ⚙️ Step 2 – Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This will:

* Create system groups and a user
* Enable the `ollama` systemd service
* Start the local API on port `11434`

The service starts automatically, so no need to run `ollama serve`.

### 🤖 Step 3 – Run Your First Model

Pull and run a small text model to test the setup:

```bash
ollama pull gemma3:1b
ollama run gemma3:1b
```

Try a basic prompt:

```
> What is an orange?
```

### 🧪 Step 4 – Benchmark with `--verbose`

```bash
ollama run gemma3:1b --verbose
```

You'll see detailed metrics:

* Total duration
* Prompt evaluation time
* Tokens per second

Example:

```
prompt eval rate:     20.62 tokens/s
eval rate:            13.67 tokens/s
```

### 📦 Step 5 – Try a Larger Model

Now try the 4B model:

```bash
ollama pull gemma3:4b
ollama run gemma3:4b --verbose
```

Observe the performance drop:

```
eval rate: 5.95 tokens/s (much slower)
```

## 🖼️ Step 6 – Run Vision Inference (Apple Image)

Download a sample image:

```bash
wget -O image.jpg https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg
```

Then ask the model to describe it:

```bash
ollama run gemma3:4b --verbose
> What is in the ./image.jpg file?
```

This will take several **minutes** on the ROCK 5B (all CPU cores will max out). Time to try the server!

## 🚀 Setup on the GPU Server

### 🔐 Step 7 – SSH into the Server

```bash
ssh root@10.26.28.XX
```

### ⚙️ Step 8 – Install Ollama (x86\_64 + GPU)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Ollama will detect the NVIDIA GPU and enable GPU acceleration automatically.

### 🖼️ Step 9 – Vision Prompt on the Server

Download the same image again:

```bash
wget -O image.jpg https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg
```

Run inference:

```bash
ollama run gemma3:4b --verbose
> What is in the ./image.jpg file?
```

This time it runs in **\~2.5 seconds**:

```
prompt eval rate: 152.60 tokens/s
eval rate: 71.95 tokens/s
```

## 🔍 Step 10 – Explore Ollama Models

Visit [https://ollama.com](https://ollama.com)
Browse the models available — look for:

* **Text-only** models (Mistral, Phi, LLaMA)
* **Vision** models (check if vision input is supported)
* Models with better CPU support or smaller size

You can try other models by pulling and running them:

```bash
ollama pull phi:1.5
ollama run phi:1.5
```

## 💡 Step 11 - Experiments

* How big a model can you run on the ROCK 5B and server before it crashes?
* How many seconds did Gemma vision inference take on ROCK 5B vs GPU server?
* What’s the largest model you found on the Ollama website?

**Take your time** to really play with this. Get a feel for how "smart" or "stupid" some of these models are.
