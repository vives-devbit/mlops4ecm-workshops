## 🧪 Lab 01 – First Steps with OLAMA

> Run your first LLM and vision models on a ROCK 5B embedded device. Then compare to GPU inference on a server. Discover the limits of local AI execution and get familiar with prompt-based interactions.

### 🎯 Objectives

- Run a large language model (LLM) on an embedded device (ROCK 5B)
- Interact with a vision-capable LLM
- Benchmark performance: CPU vs GPU
- Explore model selection on the Ollama platform

### 🖥️ Setup on the ROCK 5B

### 🔌 SSH into the Device

Each ROCK 5B is accessible on the network. Use the label on the device to find its IP:

```bash
ssh radxa@10.26.3.XX
# password: radxa
````

### ⚙️ Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This will install `Ollama`, which is a way of running large language models efficiently on all kinds of devices, including our Linux board.

* Installs `Ollama` software and CLI
* Enables the `ollama` systemd service
* Starts the local API on port `11434`

### 🤖 Run Your First Model

Gemma 3 is a really interesting model for LLMs on edge devices:

https://blog.google/technology/developers/gemma-3/

Pull and run a small text model to test the setup:

```bash
ollama pull gemma3:1b
ollama run gemma3:1b
```

Try a basic prompt:

```
> What is an orange?
```

### 🧪 Benchmark with `--verbose`

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

### 📦 Try a Larger Model

Now try the 4B model:

```bash
ollama pull gemma3:4b
ollama run gemma3:4b --verbose
```

Observe the performance drop:

```
eval rate: 5.95 tokens/s (much slower)
```

### 🔍 Explore Ollama Models

Visit [https://ollama.com](https://ollama.com)

Browse the models available — look for:

* **Text-only** models (Mistral, Phi, LLaMA)
* **Vision** models (check if vision input is supported)
* Models with better CPU support or smaller size

You can try other models by pulling and running them:

```bash
ollama run llama3.2:3b --verbose
```

### 🖼️ Run Vision Inference (Images)

Download a sample image:

```bash
wget -O image.jpg https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg
```

Then ask the model to describe it:

```bash
ollama run gemma3:4b --verbose
> What is in the ./image.jpg file?
```

This will take several **minutes** on the ROCK 5B (all CPU cores will max out). Move on to the next section while this is running.

### Monitor resource usage (CPU, RAM)

Check out the **CPU usage**, by opening another terminal, SSH into ROCK5 and:

```bash
top  # shows you CPU/memory usage
```

Notice how all CPU cores are maxed out while processing the image. This is because Ollama is running on CPU only. The board has an NPU, but we are not using it now.

Press **"q"** to exit `top` interface.

To monitor the **memory usage**, use:

```bash
free -h
```

This shows you an overview of how much free memory you have in the system. Try different models, with different parameter sizes and try to find out how much memory each uses. Can you come up with a general formula?

```
1B models use => ??
4B models use => ??
... more?
```

Based on this, what would be the largest model we can run on the ROCK5?

**NOTE**: Ollama actually keeps all models that you run cached in memory. So they will add up over time. You need to restart Ollama in between running models, to get a clear picture:

```bash
sudo systemctl restart ollama
ollama run <some model> --verbose
sudo systemctl restart ollama
ollama run <another model> --verbose
```

### Quantization-Aware Gemma

Gemma models are available in Quantization-Aware training versions. We'll see what this means in a later theory section.

https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/

Try running some of these models:

```bash
ollama run gemma3:1b-it-qat --verbose
ollama run gemma3:4b-it-qat --verbose
... more?
```

Compare their resource usage to the standard Gemma models. How many tokens / second? How much memory do they use?

### 🚀 Setup on the GPU Server

The ROCK5 is powerful, and can definitely handle language models very well. But for large vision models, we need some more powerful hardware. Time to try the server!

### 🔐 SSH into the Server

```bash
ssh root@10.26.28.XX
```

### ⚙️ Install Ollama (x86\_64 + GPU)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Ollama will detect the **NVIDIA GPU** and enable GPU acceleration automatically.

Before we run tests, let's see how powerful our hardware is. Run the following command to show GPU specs:

```bash
nvidia-smi  # shows GPU info
```

How much memory does our GPU have? Which size models (billion parameters) do you expect we can run on this?

### 🖼️ Vision Prompt on the Server

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

That's **much faster** than the CPU-only Linux board. This shows you just how powerful GPUs are!

### Try different models

Take your time to really play with this:

https://ollama.com/search

Can you get a feel for how "smart" or "stupid" some of these models are?
