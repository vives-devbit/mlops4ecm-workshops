import ollama
import sys
import os

prompt = # TODO Ask to label an image

if len(sys.argv) != 2:
    print("Usage: python classify-image.py <path_to_image>")
    sys.exit(1)

path_to_image = sys.argv[1]

if not os.path.isfile(path_to_image):
    print(f"Error: File '{path_to_image}' not found.")
    sys.exit(1)

# Run inference
response = ollama.chat(
    model='gemma3:4b',
    messages=[
        {
            'role': 'user',
            'content': prompt,
            'images': [path_to_image]
        }
    ]
)

print(response['message']['content'])
