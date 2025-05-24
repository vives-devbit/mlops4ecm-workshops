
# Building ML Infrastructure and Deploying Production-Ready Models

This workshop is part of the "Building ML Infrastructure" course:

- 📚 Read the full [written guide](https://mlops4ecm.be/handleidingen/ml-infrastructure/) with detailed explanations
- 🎧 Listen to the [podcast episodes](https://mlops4ecm.be/handleidingen/ml-infrastructure/) for an audio companion
- 📄 Download the [slide deck (PDF)](https://mlops4ecm.be/handleidingen/Building%20ML%20Infrastructure.pdf) for a visual summary

Whether you prefer reading, listening, or watching — we've got you covered.

## 🧭 Lab Overview

<img src="../media/ml-infrastructure-server-rack-data-center.jpg" style="width: 300px" align="right">

Welcome to the **ML Infrastructure Workshop** — a hands-on series of labs designed to take you from notebook experimentation to fully automated, production-grade machine learning systems.

Each lab builds on the previous one, gradually introducing real-world tools and practices used in modern MLOps environments.

### Lab 01 – [Running the Notebook](01-running-the-notebook/)

Set up a virtual machine, configure your Python environment, and run a notebook that trains a MobileNet classifier on grocery item images.

### Lab 02 – [Refactor the Notebook](02-refactor-the-notebook/)

Turn your Jupyter notebook into a clean, testable Python project. Refactor the code into reusable modules, build a script for automated training, and add your first unit tests.

### Lab 03 – [Notebook Visualization](03-notebook-visualization/)

Use Jupyter notebooks to explore model behavior, identify weak spots, and inspect dataset structure. No training is performed here — just analysis and visualization.

### Lab 04 – [Backend with FastAPI](04-backend-with-fastapi/)

Serve your trained model through a REST API built with FastAPI. Create an endpoint that accepts image uploads and returns predictions.

### Lab 05 – [Connect the Frontend](05-connect-the-frontend/)

Integrate a Dash-based frontend with your API. Let users upload images and see model predictions in a simple web interface.

### Lab 06 – [Docker Containers](06-docker-containers/)

<img src="../media/containers-shipping-analogy.jpg" style="width: 300px" align="right">

Package both the backend and frontend into Docker containers to ensure reproducibility and portability across systems.

### Lab 07 – [Compose Deployment](07-compose-deployment/)

Use Docker Compose to launch your entire application stack (API + frontend) with a single command. Deploy your application to a production environment via GitHub or a Docker registry.

### Lab 08 – [Deploy Model from S3](08-deploy-model-from-s3/)

Move your training dataset to S3 and modify your code to load it from object storage instead of local disk — just like in cloud pipelines.

### Lab 09 – [Pull Request Checks](09-pull-request-checks/)

Add continuous integration (CI) checks to your project using GitHub Actions. Automatically test your code and check formatting every time someone opens a pull request.

### Lab 10 – [Automatic Deployment](10-automatic-deployment/)

Install a self-hosted GitHub Actions runner on your VM. Configure a workflow to automatically deploy your app with Docker Compose on every push to `main`.

## 🚀 Goal of the Workshop

By the end of these labs, you'll have built a real, end-to-end machine learning system that can:

- Ingest and process data
- Train and evaluate models
- Serve predictions via API and UI
- Automate deployments and retraining

You'll also gain hands-on experience with tools like **FastAPI**, **Docker Compose**, **MinIO S3**, and **GitHub Actions** — all key components of a modern MLOps toolkit.

## 🛠️ Prerequisites

- Basic Python and Git knowledge
- Familiarity with machine learning (e.g. training a model in PyTorch)
- Willingness to use the terminal and VS Code
- Some exposure to Linux and SSH is helpful
