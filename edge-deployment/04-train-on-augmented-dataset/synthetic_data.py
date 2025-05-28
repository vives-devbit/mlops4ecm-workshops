import os
import random
import pandas as pd
import ollama
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Constants
DATA_DIR = os.path.expanduser('~/GroceryStoreDataset/dataset')
CLASSES_CSV = os.path.join(DATA_DIR, 'classes.csv')
TRAIN_CSV = os.path.join(DATA_DIR, 'train.txt')
OUTPUT_DIR = './synthetic'
MODEL_NAME = "runwayml/stable-diffusion-v1-5"
OLLAMA_MODEL = "gemma3:4b"
DESCRIPTION_PROMPT = "Please describe this image in one sentence. Only output the description — no extra text."

# Load class mapping: int → class name
def get_class_names():
    return (
        pd.read_csv(CLASSES_CSV)
        .drop_duplicates("Coarse Class ID (int)")
        .set_index("Coarse Class ID (int)")["Coarse Class Name (str)"]
        .to_dict()
    )

# Load dataset and group by class
def load_grouped_dataset(csv_path):
    df = pd.read_csv(csv_path, header=None)
    df.columns = ["path", "fine_label", "coarse_label"]
    grouped = {}

    for _, row in df.iterrows():
        label_id = row["coarse_label"]
        class_name = CLASSES[label_id]
        full_path = os.path.join(DATA_DIR, row["path"])
        grouped.setdefault(class_name, []).append(full_path)

    return grouped

print("🔄 Loading dataset and class names...")
CLASSES = get_class_names()
grouped_data = load_grouped_dataset(TRAIN_CSV)

print("🚀 Loading Stable Diffusion model...")
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16
).to("cuda")

# Generate images
for class_name, paths in grouped_data.items():
    selected = random.sample(paths, min(len(paths), 10))  # 10 samples per class

    for img_path in selected:
        original_filename = os.path.basename(img_path).replace(".jpg", ".png")

        if not os.path.exists(img_path):
            print(f"⚠️ Skipping missing file: {img_path}")
            continue

        print(f"\n🖼️ Describing: {original_filename} (class: {class_name})")

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{
                'role': 'user',
                'content': DESCRIPTION_PROMPT,
                'images': [img_path]
            }]
        )
        description = response['message']['content'].strip()
        print(f"📜 Prompt: {description}")

        image = pipe(description).images[0]

        class_dir = os.path.join(OUTPUT_DIR, class_name)
        os.makedirs(class_dir, exist_ok=True)
        output_path = os.path.join(class_dir, original_filename)
        image.save(output_path)
        print(f"✅ Saved: {output_path}")
