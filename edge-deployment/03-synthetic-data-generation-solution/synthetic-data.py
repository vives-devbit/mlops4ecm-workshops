import os
import random
import pandas as pd
import ollama
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Constants
DATA_DIR = os.path.expanduser('~/GroceryStoreDataset/dataset')
TRAIN_CSV = os.path.join(DATA_DIR, 'train.txt')
OUTPUT_DIR = './synthetic_images'
MODEL_NAME = "runwayml/stable-diffusion-v1-5"
OLLAMA_MODEL = "gemma3:4b"

# Prompt for Ollama
DESCRIPTION_PROMPT = "Please describe this image in one sentence. Only output the description — no extra text."

# Make output folder if needed
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset paths
def read_dataset(csv_file):
    df = pd.read_csv(csv_file, header=None)
    df.columns = ["path", "fine_label", "coarse_label"]
    for _, row in df.iterrows():
        img_path = os.path.join(DATA_DIR, row["path"])
        yield img_path

print("🔄 Loading image paths...")
DATASET = list(read_dataset(TRAIN_CSV))
random.shuffle(DATASET)
SAMPLES = DATASET[:10]

# Load diffusion model
print("🚀 Loading Stable Diffusion model...")
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16
).to("cuda")

# Run pipeline
for path in SAMPLES:
    filename = os.path.basename(path)

    if not os.path.exists(path):
        print(f"⚠️ Skipping missing file: {path}")
        continue

    print(f"\n🖼️ Describing: {filename}")

    # Describe image using LLM
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                'role': 'user',
                'content': DESCRIPTION_PROMPT,
                'images': [path]
            }
        ]
    )
    description = response['message']['content'].strip()
    print(f"📜 Prompt: {description}")

    # Generate image from description
    image = pipe(description).images[0]

    # Save generated image
    output_path = os.path.join(OUTPUT_DIR, f"synthetic_{filename}")
    image.save(output_path)
    print(f"✅ Saved: {output_path}")

