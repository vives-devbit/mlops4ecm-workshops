import os
import random
import pandas as pd
import ollama
import torch
from diffusers import StableDiffusion3Pipeline
from PIL import Image

# Constants
DATA_DIR = os.path.expanduser('~/GroceryStoreDataset/dataset')
CLASSES_CSV = os.path.join(DATA_DIR, 'classes.csv')
TRAIN_CSV = os.path.join(DATA_DIR, 'train.txt')
OUTPUT_DIR = './synthetic'
MODEL_NAME = "ckpt/stable-diffusion-3.5-medium"
OLLAMA_MODEL = "gemma3:4b"

# Prompt for Ollama
DESCRIPTION_PROMPT = "Please describe this image in one sentence. Only output the description — no extra text."

# Load class mapping: int → class name
def get_class_names():
    return (
        pd.read_csv(CLASSES_CSV)
        .drop_duplicates("Coarse Class ID (int)")
        .set_index("Coarse Class ID (int)")["Coarse Class Name (str)"]
        .to_dict()
    )

# Load dataset paths
def read_dataset(csv_file):
    df = pd.read_csv(csv_file, header=None)
    df.columns = ["path", "fine_label", "coarse_label"]
    return df

print("🔄 Loading dataset and class names...")
CLASSES = get_class_names()
df = read_dataset(TRAIN_CSV)
df = df.sample(n=100).reset_index(drop=True)  # random 100 samples

# Load diffusion model
print("🚀 Loading Stable Diffusion model...")
pipe = StableDiffusion3Pipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.bfloat16
).to("cuda")

# Run pipeline
for _, row in df.iterrows():
    img_path = os.path.join(DATA_DIR, row["path"])
    label_id = row["coarse_label"]
    class_name = CLASSES[label_id]
    original_filename = os.path.basename(img_path).replace(".jpg", ".png")

    if not os.path.exists(img_path):
        print(f"⚠️ Skipping missing file: {img_path}")
        continue

    print(f"\n🖼️ Describing: {original_filename} (class: {class_name})")

    # Describe image using LLM
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

    # Generate image from description
    image = pipe(
        prompt=description,
        num_inference_steps=20,
        guidance_scale=5,
        width=336,
        height=336
    ).images[0]

    # Save to: synthetic/<class_name>/<original_filename>.png
    class_dir = os.path.join(OUTPUT_DIR, class_name)
    os.makedirs(class_dir, exist_ok=True)
    output_path = os.path.join(class_dir, original_filename)
    image.save(output_path)
    print(f"✅ Saved: {output_path}")
