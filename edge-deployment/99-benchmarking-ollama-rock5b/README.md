## Lab 99 - Benchmarking Ollama LLM models on the Rock 5b

In this lab, you'll explore the power of running large language models (LLMs) directly on edge devices, specifically the Rock 5b single-board computer. You'll learn how to install and use Ollama, a tool that makes it easy to run state-of-the-art LLMs locally, and you'll benchmark their performance to understand the capabilities and limitations of edge hardware.

---

### Installing Ollama

To get started, you'll need to install Ollama on your Rock 5b device. Ollama provides a simple installation script that sets up everything you need to run LLMs locally. Open a terminal and run the following command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This will download and install the latest version of Ollama for your platform.

---

### Verify installation

After installation, verify that Ollama is correctly installed by checking its version:

```bash
ollama -v
```

You should see output similar to:

```bash
ollama version is 0.7.1
```

If you see the version number, you're ready to proceed.

---

### Running your first LLM

Now let's try running your first large language model locally. Ollama makes it easy to pull and run models with a single command. For this lab, we'll start with the LLaMA 3 1B model, which is small enough to run on most edge devices:

```bash
ollama run llama3.2:1b
```

The first time you run this command, Ollama will download the model files. You should see output indicating the progress of the download:

```bash
pulling manifest
pulling 74701a8c35f6: 100% ▕███████████████████████████████████████████████████████████████████▏ 1.3 GB
pulling 966de95ca8a6: 100% ▕███████████████████████████████████████████████████████████████████▏ 1.4 KB
pulling fcc5a6bec9da: 100% ▕███████████████████████████████████████████████████████████████████▏ 7.7 KB
pulling a70ff7e570d9: 100% ▕███████████████████████████████████████████████████████████████████▏ 6.0 KB
pulling 4f659a1e86d7: 100% ▕███████████████████████████████████████████████████████████████████▏  485 B
verifying sha256 digest
writing manifest
success
```

Once the model is downloaded, you'll be able to interact with it directly in your terminal.

---

```bash
>>> Send a message (/? for help)
```

At this prompt, you can type any question or instruction, and the model will respond.

---

```bash
>>> You're helping participants in an Edge AI workshop. Give a cool one-paragraph welcome message that mentions running LLaMA 3 locally and how awesome it is.
```

The model should give you some text that looks like this.

```bash
Here's a potential welcome message:

"Welcome to our Edge AI workshop, where we'll dive into the exciting world of machine learning at the edge! Today, you get to experience running the latest and greatest in natural language processing with your own devices - specifically, your smartphones or laptops - using the powerful LLaMA 3 model. This cutting-edge AI engine is a game-changer for real-time text analysis, and with this workshop, you'll be able to harness its capabilities locally, without relying on cloud services. Get ready to explore the possibilities of Edge AI and experience the power of AI in your own context."
```

---

### Benchmarking a LLM

To understand the performance of LLMs on your Rock 5b, you can benchmark how fast the model processes tokens. Use the `--verbose` flag to get detailed timing information:

```bash
ollama run llama3.2:1b --verbose
```

You'll see output like this:

```bash
total duration:       7.803430944s
load duration:        184.853293ms
prompt eval count:    58 token(s)
prompt eval duration: 107.266241ms
prompt eval rate:     540.71 tokens/s
eval count:           115 token(s)
eval duration:        7.509147594s
eval rate:            15.31 tokens/s
```

The most important metric here is the "eval rate," which tells you how many tokens per second the model can generate. Try running this benchmark with different models and compare the results. You can also repeat the same benchmark on a more powerful server or virtual machine to see how hardware affects performance.

---

### Explore available LLM's

Ollama supports a wide range of open-source language models. You can browse the available models, see their sizes, and check the number of parameters by visiting the Ollama model search page:

[https://ollama.com/search]()

Take a few minutes to explore the different models. Pay attention to the model size and parameter count—these factors determine whether a model can run on your device and how much memory and compute it will require.
LLMs often come in different variants such as `1B`, `3B`, `7B`, or even `70B`, where the number refers to the number of parameters (e.g., 1 billion, 7 billion). The number of parameters directly impacts the model's ability to represent complex patterns and knowledge. Larger models typically provide more accurate and contextually rich responses but require more memory, power, and computational resources to run. For example, a `70B` model might outperform a `7B` one in generating nuanced text, but it would be impractical for edge devices due to high inference latency and memory usage. On the other hand, smaller models like `1B` or `3B` can deliver acceptable results for many tasks while remaining feasible on devices with limited resources.

#### Parameter size vs RAM

The size of a model's parameters is closely related to the amount of RAM required to load and run it. As a rule of thumb, each parameter requires about one byte of memory, so a `7B` model needs roughly 7 GB of RAM just for the model weights, not including additional memory for processing and system overhead. The Rock 5b typically comes with 8 GB or 16 GB of RAM, which means that only smaller models (such as `1B`, `3B`, or sometimes `7B`) can be run comfortably. Attempting to load larger models may result in out-of-memory errors or severe performance degradation. Always check your device's available RAM and compare it to the model size before running a new LLM on the Rock 5b.

#### Quantization aware trained models (QAT)

Quantization aware trained models (QAT) are neural networks that have been trained with quantization in mind, allowing them to use lower-precision (such as 8-bit or 4-bit) weights and activations without significant loss in accuracy. This process reduces the memory footprint and computational requirements of the model, making it much more suitable for edge devices like the Rock 5b. The main impact of using QAT models during inference is faster processing and lower RAM usage, enabling larger or more complex models to run on hardware with limited resources. However, there may be a slight reduction in model accuracy compared to full-precision versions, but for many applications, this trade-off is worthwhile to achieve real-time performance on edge devices.

### Llama vs Gemma

Llama and Gemma are both families of open-source large language models (LLMs), but they come from different organizations and have distinct design goals.

**Llama** is developed by Meta (Facebook) and is known for its strong performance across a range of natural language processing tasks. Llama models are available in various sizes (such as 1B, 3B, 7B, and 70B parameters), making them suitable for both edge devices and powerful servers. Llama models are widely used in research and industry due to their balance of accuracy, efficiency, and permissive licensing.

**Gemma**, on the other hand, is a newer family of LLMs released by Google. Gemma models are designed with efficiency and responsible AI use in mind, often featuring optimizations for running on resource-constrained hardware. Like Llama, Gemma comes in multiple sizes and supports quantized versions for edge deployment. Gemma models emphasize transparency, safety, and ease of integration with Google's AI ecosystem.

When choosing between Llama and Gemma for edge deployment, consider factors such as model size, performance benchmarks, compatibility with your hardware, and the specific features or optimizations each model offers. Both are excellent choices for running LLMs locally, and experimenting with each can help you determine which best fits your use case.

### Recommended Models to Benchmark on Rock 5b

Here are some interesting models you can benchmark on the Rock 5b, covering [Llama](https://ollama.com/library/llama3.2/tags), [Gemma](https://ollama.com/library/gemma3/tags), and quantized (QAT) variants. These models are selected for their balance of performance and feasibility on edge hardware:

| Model Name         | Family  | Parameter Size | Quantized Version | Notes                                      |
|--------------------|---------|---------------|-------------------|--------------------------------------------|
| llama3.2:1b        | Llama   | 1B            | Yes (Q4_0, Q8_0)  | Very lightweight, good for quick tests     |
| llama3.2:3b        | Llama   | 3B            | Yes (Q4_0, Q8_0)  | Good balance of speed and capability       |
| llama2:7b          | Llama   | 7B            | Yes (Q4_0, Q8_0)  | May require 8GB+ RAM, try quantized first  |
| gemma3:2b          | Gemma   | 2B            | Yes (Q4_0, Q8_0)  | Efficient, designed for edge deployment    |
| gemma3:4b          | Gemma   | 4B            | Yes (Q4_0, Q8_0)  | Needs 8GB+ RAM, quantized recommended      |
| phi3:mini-4k-instruct | Phi-3 | 3.8B         | Yes (Q4_0, Q8_0)  | Compact, strong performance for its size   |
| mistral:7b         | Mistral | 7B            | Yes (Q4_0, Q8_0)  | Fast and efficient, popular for edge use   |

**Tips:**

- Use quantized versions (Q4_0, Q8_0) to reduce memory usage and improve speed.
- Start with smaller models (1B–3B) for best performance on 8GB RAM devices.
- For each model, try both full-precision and quantized variants to compare accuracy and speed.

You can find these models on the [Ollama model search page](https://ollama.com/search)

---

By the end of this lab, you'll have hands-on experience running and benchmarking LLMs on edge hardware, and you'll understand the trade-offs between model size, performance, and hardware capabilities.
