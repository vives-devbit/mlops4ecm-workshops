import pandas as pd
import os
import ollama
import random

prompt = "Please describe this image in one sentence. Only output the description — no extra text."

# Dataset paths
DATA_DIR = os.path.expanduser('~/GroceryStoreDataset/dataset')
TRAIN_CSV = os.path.join(DATA_DIR, 'train.txt')

def read_dataset(csv_file):
    df = pd.read_csv(csv_file, header=None)
    df.columns = ["path", "fine_label", "coarse_label"]
    for _, row in df.iterrows():
        img_path = os.path.join(DATA_DIR, row["path"])
        yield img_path

# Load 10 random samples
DATASET = list(read_dataset(TRAIN_CSV))
random.shuffle(DATASET)
SAMPLES = DATASET[:10]

# Generate and print descriptions
for path in SAMPLES:
    if not os.path.exists(path):
        print(f"⚠️ Skipping missing file: {path}")
        continue

    print(f"\n🖼️ {os.path.basename(path)}")

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

    description = response['message']['content'].strip()
    print(f"📝 Description: {description}")

