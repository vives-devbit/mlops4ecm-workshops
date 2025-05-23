# Lab 02 – Refactor the Notebook

<img src="../../media/notebooks-refactoring-cleanup.jpg" style="width: 300px" align="right">

> Turn your Jupyter notebook into a clean, testable Python project. Refactor the code into reusable modules, build a script for automated training, and add your first unit tests.

## 🧭 Objective

This lab marks your transition from **exploration** to **engineering**.

You'll split the original `grocery-store.ipynb` notebook into reusable modules, add a configurable training script, and write a unit test to verify that your dataloader works. After this lab, you'll have a clean and modular codebase that's easier to debug, test, and extend — and you’ll be ready for automation and deployment.

## 🔧 Step 1 – Refactor the Notebook into Modules

The goal here is to **extract core logic** from the notebook into Python modules.

Keep the notebook, but turn it into a lightweight driver: it loads the modules, trains a model, prints accuracy, and shows sample predictions — just like before. But the logic lives elsewhere.

### ✅ Suggested File Structure

```
├── data_utils.py          # Data loading and transforms
├── model_utils.py         # Model setup, load/save to disk
├── train_utils.py         # Training + evaluation logic
├── grocery-store.ipynb    # Minimal driver notebook (step 1)
├── run_training.py        # Standalone script to train models (step 2)
└── test_dataloader.py     # Unit tests for data pipeline (step 3)
```

You can optionally organize your code into subfolders with `__init__.py` files to create a **package** structure. This makes imports cleaner and helps keep related code grouped, which is especially useful as your project grows. It’s **not required** for this lab, but it mirrors how larger ML projects are typically structured.

### 📦 What goes where?

- **`data_utils.py`**
  - `DATA_DIR` and `CSV` definitions
  - `GroceryDataset` class
  - Image transforms
  - `get_classes()` function that loads class names from CSV.
  - `get_loaders()` function that returns PyTorch train/val dataloaders
    - Optional `batch_size` parameter (useful in step 2)

- **`model_utils.py`**
  - `DEVICE` definition (CPU/CUDA)
  - `create_model(num_classes)` that returns a MobileNetV3 model with a replaced classifier
  - `load_model(path)` loads an existing model from disk (optional `path` parameter)
  - `save_model(model, path)` saves a new model to disk (optional `path` parameter)

- **`train_utils.py`**
  - Uses `model_utils` to obtain `DEVICE` definition
  - `train_model(model, dataloader, epochs, learning_rate)`
    - Optional `epochs` and `learning_rate` parameters
  - `evaluate_model(model, dataloader)` → returns model accuracy

- **`grocery-store.ipynb`**
  - Use the above modules to run training and evaluation

  ```python
  from data_utils import *
  from model_utils import *
  from train_utils import *
  ```

  - Show 10 predictions as images with class labels
  - Nothing else — **no training logic inside**

The actual “visual” code can stay in the notebook — for example, drawing images with Matplotlib and showing predictions alongside them. That kind of code belongs in a notebook.

## 🚀 Step 2 – Add a Configurable Training Script

You now build a standalone script: `run_training.py`

This script should:

1. Load dataloaders from `data_utils.py`
2. Load a model from `model_utils.py`
3. Train it using functions from `train_utils.py`
4. Save the model to disk (e.g. `model.pt`)
5. Print final accuracy

Add **command-line arguments** with `argparse`:

```python
parser = argparse.ArgumentParser()
parser.add_argument("--batch-size", type=int, default=32)
parser.add_argument("--learning-rate", type=float, default=1e-3)
parser.add_argument("--epochs", type=int, default=5)
parser.add_argument("--output", type=str, default="model.pt")
```

Now you can launch experiments like:

```bash
python run_training.py --batch-size 64 --learning-rate 0.0005 --epochs 10
```

You can even run several in **parallel** by opening multiple terminals and running the script with different settings in each one:

```bash
python run_training.py --batch-size 16 --output model_bs16.pt
```

```bash
python run_training.py --batch-size 64 --output model_bs64.pt
```

Can you find the **optimal batch size and learning rate** to get the best performance in the least amount of time?

➡️ This is one of the **big advantages of script-based training**: fast, repeatable experimentation without the overhead of a notebook interface.


## 🧪 Step 3 – Add a Unit Test with PyTest

Focus on testing your **data pipeline**, since that's often a source of subtle bugs.

Install `pytest` if needed:

```bash
pip install pytest
```

Create a test file: `test_dataloader.py`

### ✅ Example Test

```python
def test_dataloader_shapes():
    from data_utils import get_loaders
    train_loader, _ = get_loaders(batch_size=4)
    images, labels = next(iter(train_loader))
    assert images.shape == (4, 3, 224, 224)
    assert labels.ndim == 1
```

### 🧠 Other Ideas

* Check that dataset length is > 0
* Check that label values are integers
* Check that transform returns a tensor

Run tests with:

```bash
pytest
```

➡️ This is your **first automated quality check**. We'll expand this idea later using GitHub Actions.

## 🎁 Bonus Exercises

### 🌀 Convert the Notebook Automatically (Optional)

Try turning your original notebook into a `.py` script using:

```bash
jupyter nbconvert --to script grocery-store.ipynb
```

This won't be perfect, but it's a useful starting point when refactoring.

### 🚀 Speed Up Training by Preprocessing Images (Optional)

Currently, your model resizes and normalizes images **on the fly**. This slows down training.

Try this:

1. Write a preprocessing script that loads each image, resizes to 224×224, and saves it to a new folder
2. Update your dataset class to load from that folder without extra transforms
3. Measure training speed with and without preprocessing

Use the `time` module to track epoch duration.

➡️ This is your first taste of **ML performance tuning**.

## ✅ Summary

After completing Lab 02, your project is no longer just a notebook — it’s a **real Python codebase**:

* Code is clean, testable, and reusable
* Training is scriptable and parameterized
* Notebooks are used for exploration, not logic
* You’ve written your first unit test

These are the **building blocks of MLOps** — and they’ll make the rest of the course faster, safer, and easier.

**Next up: exploratory notebooks to visualize performance and inspect your dataset.**
