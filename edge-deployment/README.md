
# Edge AI Deployment: Optimizing and Scaling AI Models on Devices

This workshop is part of the **"Edge AI Deployment"** course:

- 📚 Read the full [written guide](https://mlops4ecm.be/handleidingen/edge-deployment/) with detailed explanations
- 🎧 Listen to the [podcast series](https://mlops4ecm.be/handleidingen/edge-deployment/) for audio insight
- 📄 Download the [slide deck (PDF)](https://mlops4ecm.be/handleidingen/Edge%20AI%20Deployment.pdf) for a visual overview

Whether you're here to learn by coding, watching, or listening — you're covered.

## 🧭 Lab Overview

<img src="../media/ai-at-the-edge-intro.jpg" style="width: 300px" align="right">

Welcome to the **Edge AI Optimization Workshop** — a practical, hands-on series of labs that introduces you to neural network deployment, inference, and optimization techniques for both embedded systems and powerful GPU servers.

Each lab builds on the last, guiding you through the process of deploying AI models in constrained environments while maximizing performance.

### Lab 01 – [First Steps with OLAMA](01-first-steps-with-olama/)

Run your first LLM and vision models on a ROCK 5B embedded device. Then compare to GPU inference on a server. Discover the limits of local AI execution and get familiar with prompt-based interactions.

### Lab 02 – [Grocery Classification with Pretrained Models](02-grocery-classification/)

Use pretrained multimodal models to classify real-world grocery images. Evaluate the effectiveness of prompt engineering and model selection — without any training required.

### Lab 03 – [Generate Synthetic Data with Diffusion](03-synthetic-data-generation/)

Use Stable Diffusion and large language models to augment your dataset. Focus on underrepresented grocery classes and explore how synthetic data can balance a real dataset.

### Lab 04 – [Train on Real + Synthetic Data](04-train-on-augmented-dataset/)

<img src="../media/edge-ai-industrial-robotics.jpg" style="width: 300px" align="right">

Train a convolutional model (e.g. MobileNet) on the combined real and synthetic dataset. Compare performance against a baseline trained on only real data.

### Lab 05 – [Optimize Deployment with ONNX Runtime](05-onnx-runtime-optimization/)

Export your model to ONNX, run it on the ROCK 5B using ONNX Runtime, and apply quantization to reduce inference time. Learn how to visualize and understand neural network graphs.

### Lab 06 – [Distill a Smaller Model](06-knowledge-distillation/)

Train a small model (MobileNet) using outputs from a larger teacher model (e.g. ResNet). Learn how knowledge distillation can compress models while retaining performance — ideal for edge deployment.

## 🚀 Goal of the Workshop

By the end of this workshop, you'll have:

- Run LLMs and vision models on embedded and server hardware
- Evaluated pretrained models on real-world data
- Used diffusion models for synthetic data generation
- Trained and optimized your own models for edge deployment
- Applied quantization and knowledge distillation to shrink models without sacrificing performance

You'll gain practical experience with tools and formats like **OLAMA**, **Stable Diffusion**, **ONNX Runtime**, **Netron**, and **MobileNet** — all in the context of real, edge-oriented applications.

## 🛠️ Prerequisites

- Basic Python experience and some command-line confidence
- Familiarity with machine learning (e.g. training a CNN)
- No prior deep learning deployment experience required
- SSH access to a ROCK 5B device and a GPU server VM
