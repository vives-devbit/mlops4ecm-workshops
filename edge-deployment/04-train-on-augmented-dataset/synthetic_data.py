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

MAX_IMAGES_PER_CLASS = 10

# Track how many images we've generated per class
generated_count = {cls: 0 for cls in grouped_data.keys()}

# Round-robin style generation
for i in range(MAX_IMAGES_PER_CLASS):
    for class_name, paths in grouped_data.items():
        if generated_count[class_name] >= MAX_IMAGES_PER_CLASS:
            continue  # skip if max reached for this class

        # Find remaining unused images for this class
        available = [p for p in paths if os.path.exists(p)]
        if not available:
            print(f"⚠️ No available images for class: {class_name}")
            continue

        img_path = random.choice(available)
        original_filename = os.path.basename(img_path).replace(".jpg", ".png")

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
