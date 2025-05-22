
# 02 – Refactor the Notebook

<img src="../../media/notebooks-refactoring-cleanup.jpg" style="width: 300px" align="right">

> Transform the notebook into modular Python scripts for training and data loading. Enable parameterized runs and testing with `pytest`.

Transform the notebook into a maintainable Python project. Extract the model, training logic, and dataset loading into separate Python scripts or modules. This will make your code easier to test, reuse, and deploy later on.

Now we can do a bunch of thing which we couldn't before:
- Create `run_training.py` script which takes parameters `LR, BATCH_SIZE`...
    - Use `run_training.py` to find good LR and test speed or training for different batch sizes.
    - You can run the script in parallel in multiple terminals!
- Unit test the dataloader with pytest
