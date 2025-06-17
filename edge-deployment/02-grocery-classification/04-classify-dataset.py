import pandas as pd
import os
import ollama
import sys
import os
import random

prompt = # TODO Ask to label an image

DATA_DIR = os.path.expanduser('~/GroceryStoreDataset/dataset')
CLASSES_CSV = os.path.join(DATA_DIR, 'classes.csv')
TRAIN_CSV = os.path.join(DATA_DIR, 'train.txt')
VAL_CSV = os.path.join(DATA_DIR, 'val.txt')

def read_dataset(csv_file):
    df = pd.read_csv(csv_file, header=None)
    df.columns = ["path", "fine_label", "coarse_label"]

    for idx in range(len(df)):
        row = df.iloc[idx]
        img_path = os.path.join(DATA_DIR, row["path"])
        label = row["coarse_label"]
        yield img_path, label

def get_classes():
    """ Load class names. Returns dict(int => class name) """
    return (
        pd.read_csv(CLASSES_CSV)
        .drop_duplicates("Coarse Class ID (int)")
        .set_index("Coarse Class ID (int)")["Coarse Class Name (str)"]
        .to_dict()
    )

DATASET = list(read_dataset(TRAIN_CSV))
CLASSES = get_classes()
random.shuffle(DATASET)

total = 0
good = 0

for path, label in DATASET:
    label = CLASSES[label]

    # Run inference
    response = ollama.chat(
        model='gemma3:4b',
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'images': [path]
            }
        ]
    )
    answer = response['message']['content'].strip()
    total += 1

    if label.lower() == answer.lower():
        good += 1

    print(os.path.basename(path))
    print(f"{label} => {answer}")
    print(f"accuracy: {good/total:.2f} | total = {total}")
    print()
