
## Lab 03 – Notebook Visualization

<img src="../../media/notebook-visualization.jpg" style="width: 300px" align="right">

> Use Jupyter notebooks to explore model behavior, identify weak spots, and inspect dataset structure. No training is performed here — just analysis and visualization.

### 🧭 Objective

In the previous lab, you refactored your code into clean Python modules and created a training notebook (`grocery-store.ipynb`) that loads modules, trains a model, and visualizes a few predictions.

In this lab, you’ll go one step further: use **dedicated notebooks** to explore specific aspects of your model and dataset.

These notebooks:

* **Do not train anything**
* Assume you’ve already trained and **saved a model** using `run_training.py`
* Use your **Python modules** to load data and models
* Focus on interactive, exploratory **analysis**

By keeping notebooks small and focused, you make your project easier to debug, extend, and understand — even for future collaborators.

```
├── dataset_analysis.ipynb
├── prediction_gallery.ipynb
└── confusion_matrix.ipynb
```

Each notebook has a single goal. You can keep adding more notebooks later — thanks to your modular codebase, it’s easy.

### 🍓 Notebook 1 – `dataset_analysis.ipynb`

> Explore the training data distribution. Are some classes over- or under-represented?

Use this notebook to inspect your dataset’s structure and class imbalance. Look at:

* Number of images per class (bar plot)

This helps answer:

* Are there more apple images than kiwi?
* Are some classes extremely rare?

Steps:

* Load the `train.txt` or `val.txt` dataset CSVs
* Group and count samples per class
    - You can use the `pandas` library, if you know it
    - Otherwise just use pure Python code (loops)
* Visualize class counts as a bar chart
    - Use `matplotlib` to draw a `plt.bar()` graph

### 🤖 Notebook 2 – `prediction_gallery.ipynb`

> Build a lightweight prediction tool using **Gradio** for interactive exploration.

Use the [Gradio](https://gradio.app/) library to create a UI that lets you:

* Select a class (e.g. “fruits”)
* Show a few images from that class
* Run your model on them and display the predictions

This notebook creates a **mini demo** of your model — useful for presentations, quick tests, or debugging.

Steps:

* Install Gradio: `pip install gradio`
* Load your saved model and data loader
* Create a UI with dropdowns, buttons, and image previews
* Launch it inside the notebook (or in your browser)

### 🎁 Bonus Exercise

#### 📊 Notebook 3 – `confusion_matrix.ipynb` (Optional)

> Visualize how your model performs across different classes. Which categories does it confuse?

Use `sklearn.metrics.confusion_matrix` to generate a matrix comparing **true vs. predicted labels**. Then use `matplotlib` or `seaborn` to visualize the result.

This will help you identify weak spots in your model. For example:

* Does it confuse apples with kiwis?
* Are dairy products harder to classify than fruit?

Steps:

* Load your saved model (`model.pt`) from disk
* Run inference on the full validation set
* Collect predicted and true labels
* Visualize the confusion matrix

### 🧠 Key Takeaways

* Keep notebooks short and focused on one goal
* Load models and data from utility modules
* Use Python scripts for training — use notebooks for insight
* Use visual tools (like interactive UIs) to spot problems early

These notebooks are **useful, shareable, and explainable** — perfect for internal demos, team handoffs, or debugging sessions.
