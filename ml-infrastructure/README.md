
# Building ML Infrastructure and Deploying Production-Ready Models

Welcome to the **ML Infrastructure Workshop** — a hands-on series of labs designed to take you from notebook experimentation to fully automated, production-grade machine learning systems.

Each lab builds on the previous one, gradually introducing real-world tools and practices used in modern MLOps environments.

## 🧭 Lab Overview

<img src="../media/ml-infrastructure-server-rack-data-center.jpg" style="width: 300px" align="right">

**TODO Copy paste the quotes from the lab contents**

**TODO Copy paste the quotes from the lab contents**

**TODO Copy paste the quotes from the lab contents**

### 01 – [Running the Notebook](01-running-the-notebook/)

Set up a virtual machine, configure your Python environment, and run a notebook that trains a MobileNet classifier on grocery item images.

### 02 – [Refactor the Notebook](02-refactor-the-notebook/)

Transform the notebook into modular Python scripts for training and data loading. Enable parameterized runs and testing with `pytest`.

### 03 – [Notebook Visualization](03-notebook-visualization/)

Use notebooks to explore model performance, including confusion matrices and dataset analysis. Understand the value of post-training visualization.

### 04 – [Backend with FastAPI](04-backend-with-fastapi/)

Serve your trained model through a REST API built with FastAPI. Create an endpoint that accepts image uploads and returns predictions.

### 05 – [Connect the Frontend](05-connect-the-frontend/)

Integrate a Dash-based frontend with your API. Let users upload images and see model predictions in a web interface.

### 06 – [Docker Containers](06-docker-containers/)

<img src="../media/containers-shipping-analogy.jpg" style="width: 300px" align="right">

Package both the frontend and backend into Docker containers to ensure reproducibility and portability across systems.

### 07 – [Compose Deployment](07-compose-deployment/)

Use Docker Compose to launch your entire application stack (API + frontend) with a single command. Deploy your application to a production environment via GitHub or a Docker registry.

### 08 – [Deploy Model from S3](08-deploy-model-from-s3/)

Set up a local S3-compatible storage server (MinIO), upload your trained model, and configure your API to load the model from S3.

### 09 – [Train on S3 Dataset](09-train-on-s3-dataset/)

Move your training dataset to S3 and modify your code to load it from object storage instead of local disk — just like in cloud pipelines.

### 10 – [Extend the Dataset](10-extend-the-dataset/)

Upload new images and labels through the frontend to expand your dataset. Add a new class, retrain your model, and re-evaluate performance.

### 11 – [Pull Request Checks](11-pull-request-checks/)

Add automated checks for code quality and correctness using GitHub Actions. Run `black` and `pytest` on every pull request.

### 12 – [Automatic Deployment](12-automatic-deployment/)

Install a self-hosted GitHub Actions runner on your VM. Configure a workflow to automatically deploy your app with Docker Compose on every push to `main`.

### 13 – [Dagster Pipeline](13-dagster-pipeline/)

Set up Dagster to orchestrate ML pipelines: detect new data in S3, retrain the model, and store updated outputs. Run pipelines manually or on a schedule.

## 🚀 Goal of the Workshop

By the end of these labs, you'll have built a real, end-to-end machine learning system that can:

- Ingest and process data
- Train and evaluate models
- Serve predictions via API and UI
- Automate deployments and retraining

You'll also gain hands-on experience with tools like **FastAPI**, **Docker**, **MinIO**, **GitHub Actions**, and **Dagster** — all key components of a modern MLOps toolkit.

## 🛠️ Prerequisites

- Basic Python and Git knowledge
- Familiarity with machine learning (e.g. training a model in PyTorch)
- Willingness to use the terminal and VS Code
- Some exposure to Linux and SSH is helpful
