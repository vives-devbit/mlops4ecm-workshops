import sys
import torch
from diffusers import StableDiffusionPipeline
import warnings

warnings.filterwarnings("ignore")

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-image.py \"your prompt here\"")
        sys.exit(1)

    prompt = sys.argv[1]

    print("🔄 Loading Stable Diffusion model...")
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    ).to("cuda")

    print(f"🖼️ Generating image for prompt:\n\"{prompt}\"")
    image = pipe(prompt).images[0]

    output_path = "generated-image.png"
    image.save(output_path)
    print(f"✅ Image saved as '{output_path}'")

if __name__ == "__main__":
    main()

