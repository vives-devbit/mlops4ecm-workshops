
## Lab 04 – Train on Real + Synthetic Data

> Train a convolutional model (e.g. MobileNet) on the combined real and synthetic dataset.

### 🧪 Step 1: Generate Synthetic Data

We’ll begin by creating extra training data using **Stable Diffusion** and **Ollama**.

The script `synthetic_data.py` will:

- Load real images from the training dataset
- Describe them using a vision-language model (Ollama)
- Generate new images using Stable Diffusion
- Save them in `./synthetic/<class>/<filename>.png`

**Important**:

This script automatically generates a **balanced synthetic dataset**, with the same number of synthetic images per class (up to 10 per class). This avoids overrepresentation of popular classes and helps with downstream training.

Run it like this:

```bash
python synthetic_data.py
````

⚠️  Because running the script takes very long, a generated folder synthetic/ has already been added to the repo. Open it in VS Code and **explore the generated images**.

You can try to run the script yourself, but it's actually optional. To stop the script press **CTRL + C**

### 🧠 Step 2: Train Your Model

Now you can train a MobileNetV3 model using the real dataset, optionally combined with the synthetic data.

The script `run_training.py` accepts a `--synthetic` flag to include synthetic data:

```bash
# Baseline: real data only
python run_training.py

# Real + synthetic data
python run_training.py --synthetic

# Try --epochs N to train for more epochs, to get a better model
```

A working `data_utils.py` is already provided. You do **not** need to write any data loading logic.

> ✅ Tip: Try training both with and without `--synthetic`, and compare validation accuracy.

> I have to admit that, currently, there isn’t much of an improvement. I suspect this is because the validation dataset is very similar to the training dataset. The synthetic data helps the model generalize better to data outside the dataset, but this isn’t reflected in our accuracy score. Still, the general idea of synthetic data is a powerful one.

### 📷 Step 3: Explore Model Predictions

Once your model is trained, use the notebook `prediction_gallery.ipynb` to explore how well it performs.

Launch it in **VSCode**, using your existing virtual environment (`~/mlops-workshops/.venv`), and select a class to view predictions for real and synthetic images in the validation set.

This is a great way to understand what your model is good at — and where it still fails.

### 📊 Step 4: Dataset Analysis

Open the notebook `dataset_analysis.ipynb`.

This notebook helps you:

* Inspect the original training dataset
* Visualize class imbalance

Now extend it to **include synthetic data** as well. Did class imbalance improve?
How does the class distribution change once you include the balanced synthetic dataset?
