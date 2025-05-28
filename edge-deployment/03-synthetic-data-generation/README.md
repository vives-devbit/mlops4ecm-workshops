
### 🧪 Lab 03 – Generate Synthetic Data with Diffusion

> Use Stable Diffusion and large language models to augment your dataset. Focus on underrepresented grocery classes and explore how synthetic data can balance a real dataset.

### 🔐 SSH into the GPU Server

Start by connecting to your assigned GPU server:

```bash
ssh root@10.26.X.Y
````

Replace `X.Y` with the correct IP of your VM.

### 🐍 Activate Your Python Environment

We already created a Python virtual environment in the root of the `mlops-workshops/` folder.

Activate it:

```bash
cd ~/mlops-workshops/
source .venv/bin/activate
```

This gives you access to Python, pip, and all dependencies used in this workshop.

### 📦 Install Requirements

Now go to the correct lab folder and install the dependencies for this exercise:

```bash
cd ~/mlops4ecm-workshops/edge-deployment/03-synthetic-data-generation/
pip install -r requirements.txt
```

This will install:

* `diffusers` – for working with text-to-image models
* `transformers` – model config and tokenization support
* `torch` – runs the model on GPU
* `safetensors`, `accelerate`, etc.

Make sure this finishes without errors before continuing.

### 🎨 What Are Diffusion Models?

Diffusion models are a type of generative model. They work by **starting with random noise** and gradually "denoising" it to create realistic images, based on a prompt you provide.

In this lab, you’ll use a pretrained diffusion model to generate **synthetic grocery product images** from scratch. These models have learned to understand both **language** and **visual features**, so you can just describe what you want — and they’ll generate it.

### 🖼️ Generate Your First Image

We’ve included a Python script called `generate-image.py` that generates an image based on a prompt you provide on the command line.

Try it like this:

```bash
python generate-image.py "A wooden crate filled with bananas in a grocery store"
```

This will:

* Load a pretrained Stable Diffusion model (v1.5)
* Generate an image from the prompt
* Save it as `generated-image.png` in the current folder

You’ll see messages like:

```
🖼️ Generating image for prompt:
"A wooden crate filled with bananas in a grocery store"
✅ Image saved as 'generated-image.png'
```

### View the Image in VSCode

You’re already using VSCode to edit your scripts. Now, in the VSCode file explorer, navigate to:

```
~/mlops4ecm-workshops/edge-deployment/03-synthetic-data-generation/
```

Click on `generated-image.png` to open and view your image inside VSCode.

### Generating Synthetic Data

You just created a new image based on a single prompt. That’s cool — but imagine doing this **for hundreds of images**. This is what synthetic data generation is all about.

In many real-world scenarios (especially in industry), we run into **imbalanced datasets** — some classes have lots of examples, others have very few. Diffusion models can help fix that.

Instead of manually writing dozens of prompts for each class, we can **automate prompt generation** using our vision-capable LLM.

### Let Ollama Write the Prompts

We already have a script for that!

Run the following script to describe 10 random images from the training dataset:

```bash
python describe-dataset.py
````

This script:

* Loads 10 random images
* Sends each one to `gemma3:4b` via the Ollama API
* Asks the model to describe the image in one sentence

Each description is a **natural-language prompt** that can be passed directly to your diffusion model.

### Combine Both Ideas

You now have:

* A script that generates **prompts** from real dataset images (`describe-dataset.py`)
* A script that generates **images** from prompts (`generate-image.py`)

Your final task: **write a new script that connects these two steps**.

### Your Task: Create `synthetic-data.py`

Create a new script called `synthetic-data.py`. This script should:

1. Load a set of image paths from the dataset
2. Describe each image using Ollama
3. Use the description as a prompt to generate a new image
4. Save the synthetic image to disk

Use the existing scripts as a reference. You’ll just be **combining them** into one automated pipeline.

### 💡 Tips

* You can reuse the prompt logic and loop from `describe-dataset.py`
* You can copy the generation logic from `generate-image.py`
* Save each generated image with a name based on its source, e.g. `synthetic_<original_filename>.png`

### 🖥️ Monitor GPU Usage While Your Script Runs

Once you’ve written your `synthetic-data.py` script, run it like this:

```bash
python synthetic-data.py
````

While it’s running, open **another terminal** and SSH into the same server again:

```bash
ssh root@10.26.X.Y  # same server as before
```

Then monitor GPU activity using:

```bash
watch -n 1 nvidia-smi
```

This command refreshes the GPU stats every second.

You should see:

* **GPU Utilization:** ~100% while generating images
* **Memory Usage:** 7–12 GB depending on model
* **Power Draw:** will spike during generation

Example output:

```
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.247.01             Driver Version: 535.247.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA RTX 4000 SFF Ada ...    On  | 00000000:02:00.0 Off |                  Off |
| 53%   75C    P2              56W /  70W |   7988MiB / 20475MiB |    100%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
```

> 💡 This is a great way to **visually see** that your GPU is doing actual work. It also gives insight into how demanding diffusion models are, and why they're best suited for high-performance hardware.

To stop the monitoring view, press `Ctrl + C`.

### 🎯 Goal

By the end of this lab, you will have:

* Automatically described real images using an LLM
* Generated synthetic grocery product images from those descriptions
* Created your first mini synthetic dataset!
