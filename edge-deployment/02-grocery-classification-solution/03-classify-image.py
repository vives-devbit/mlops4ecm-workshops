import ollama
import sys
import os

prompt = """
In the image, which of the following do you see?

Apple, Avocado, Banana, Kiwi, Lemon, Lime, Mango, Melon, Nectarine, Orange, Papaya, Passion-Fruit, Peach, Pear, Pineapple, Plum, Pomegranate, Red-Grapefruit, Satsumas, Juice, Milk, Oatghurt, Oat-Milk, Sour-Cream, Sour-Milk, Soyghurt, Soy-Milk, Yoghurt, Asparagus, Aubergine, Cabbage, Carrots, Cucumber, Garlic, Ginger, Leek, Mushroom, Onion, Pepper, Potato, Red-Beet, Tomato, Zucchini

Please only answer with an item from the list. Say nothing else. Just choose the item from the list that best matches the image you are seeing.
"""

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

print(response['message']['content'].strip())
