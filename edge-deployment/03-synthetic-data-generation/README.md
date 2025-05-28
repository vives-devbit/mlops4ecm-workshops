
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
python generate-image.py "A wooden crate filled with ripe bananas in a grocery store"
```

This will:

* Load a pretrained Stable Diffusion model (v1.5)
* Generate an image from the prompt
* Save it as `generated-image.png` in the current folder

You’ll see messages like:

```
🖼️ Generating image for prompt:
"A wooden crate filled with ripe bananas in a grocery store"
✅ Image saved as 'generated-image.png'
```

### View the Image in VSCode

You’re already using VSCode to edit your scripts. Now, in the VSCode file explorer, navigate to:

```
~/mlops4ecm-workshops/edge-deployment/03-synthetic-data-generation/
```

Click on `generated-image.png` to open and view your image inside VSCode.
