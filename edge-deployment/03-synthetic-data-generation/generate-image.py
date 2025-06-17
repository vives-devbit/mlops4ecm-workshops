import sys
import torch
from diffusers import StableDiffusion3Pipeline

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-image.py \"your prompt here\"")
        sys.exit(1)

    prompt = sys.argv[1]

    print("🔄 Loading Stable Diffusion model...")
    pipe = StableDiffusion3Pipeline.from_pretrained(
        "ckpt/stable-diffusion-3.5-medium",
        torch_dtype=torch.bfloat16
    ).to("cuda")

    print(f"🖼️ Generating image for prompt:\n\"{prompt}\"")
    image = pipe(
        prompt=prompt,
        num_inference_steps=20,
        guidance_scale=5,
        width=336,
        height=336
    ).images[0]

    output_path = "generated-image.png"
    image.save(output_path)
    print(f"✅ Image saved as '{output_path}'")

if __name__ == "__main__":
    main()

