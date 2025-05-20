## 🧪 Lab 01 – First Steps with Ollama

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

For example: if your board is named `Jirachi25`, the IP will be `10.26.3.25`.

### ⚙️ Install Ollama

Begin by checking whether you have `Ollama` installed, which is a way of running large language models efficiently on all kinds of devices, including our Linux board.

```bash
ollama --help
```

If this prints the help text, you are good to go. Otherwise you need to install ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

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

Type `/bye` to exit the interactive chat.

### 🧪 Benchmark with `--verbose`

You can easily do performance benchmarking with the `--verbose` flag:

```bash
ollama run gemma3:1b --verbose
```

After asking a question, you'll see detailed metrics:

* Total duration
* Prompt evaluation time
* Tokens per second

Example:

```
prompt eval rate:     20.62 tokens/s
eval rate:            13.67 tokens/s
```

A "token" is a piece of a word. The more tokens per second, the better the performance.

### 📦 Try a Larger Model

Now try the 4B model, which has 4 **billion** parameters:

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

Downloading large models takes quite a long time. To see a list of all the **models that are already on your device**, run:

```bash
ollama list
```

Play with some of these models and compare how they behave. Do you notice the difference in "intelligence" between the smaller and larger models?

### 🖼️ Run Vision Inference (Images)

Modern large language models can also process images as input. These models are sometimes called "vision-language models". It's quite amazing that this is possible on a small edge device like our ARM board.

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

This shows you an overview of how much free memory you have in the system.

**Try different models**, with different parameter sizes and try to find out how much memory each uses. Can you come up with a general formula?

```
1B (billion) parameter models use => ??
4B (billion) parameter models use => ??
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

Gemma models are available in Quantization-Aware training (QAT) versions. We'll see what this means in a later theory section.

https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/

Try running one of these models:

```bash
ollama run gemma3:4b-it-qat --verbose
```

QAT models use the same amount of resources (CPU, RAM) as the standard models, but they should be a bit **more intelligent** because they have been trained to adapt to the quantization of the model (an optimization technique).

### 🚀 Setup on the GPU Server

The ROCK5 is powerful, and can definitely handle language models very well. But for large vision models, we need some more powerful hardware. Time to try the server! Our servers have dedicated NVIDIA GPUs, which are very good at running neural networks.

### 🔐 SSH into the Server

```bash
ssh root@10.26.XX.YY
```

Please use the same YY number as your Rock 5B board. So if you are using `Jirachi25`, then SSH into virtual machine `10.26.XX.25`.

### ⚙️ Install Ollama (x86\_64 + GPU)

Just like we did on the ROCK 5B, we will install ollama on the server:

```bash
# check whether you have ollama:
ollama --help

# if not, install ollama like this:
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

### 🔍 Try different models

Take your time to really play with this:

https://ollama.com/search

Can you find any interesting models?

There are models specialized for **coding**, models optimized for **reasoning**, and so much more.

Our GPU has about 20 GB of VRAM, so you can try running much larger models than we have been up to now. For example:

```bash
ollama run deepseek-r1:32b
```

It's going to be slower, but far more intelligent.
