
## Lab 02 – Grocery Classification with Pretrained Models

> Use pretrained multimodal models to classify real-world grocery images. Evaluate the effectiveness of prompt engineering and model selection — without any training required.

Now that we have powerful **large vision models (LVMs)** running on our GPU server, a natural question arises:

**What if we used these vision models to classify our images?**

- No need to train our own convolutional neural networks
- No more MobileNetV3, EfficientNet, or ResNet-50

This approach is easier because LVMs are already **pretrained**. We simply download and run them.

Of course, you'll quickly notice that performance (in terms of latency or frames per second) is not as high as with traditional convolutional models. But the capabilities they bring are impressive — and worth exploring.

### 🧬 Clone the Workshop Repository

SSH into the server and clone both the workshop and dataset repositories:

```bash
ssh root@10.26.X.Y  # your assigned server VM
git clone https://github.com/AlexanderDhoore/<date>-mlops-workshops.git mlops-workshops/
git clone https://github.com/marcusklasson/GroceryStoreDataset.git
```

This will create:

* `~/mlops-workshops/`: your working directory for this lab
* `~/GroceryStoreDataset/`: the dataset you'll be working with

### 🐍 The Ollama Python API

Ollama provides a simple and clean Python API for interacting with large language and vision models.

Open the file `02-grocery-classification/chat.py`:

```python
import ollama

prompt = # TODO Write your prompt here

response = ollama.chat(
    model='gemma3:4b',
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)
```

Replace the `# TODO` with a basic prompt. For example:

```python
prompt = "What is an orange?"
```

Now set up your Python environment and run the script:

```bash
cd ~/mlops-workshops/
python3 -m venv .venv/
source .venv/bin/activate

cd ~/mlops-workshops/edge-deployment/02-grocery-classification/
pip3 install -r requirements.txt
python3 chat.py
```

### 🖼️ Talking About Images

When using the Python SDK, we must **explicitly pass image paths** to the model. Unlike the CLI (`ollama run`), images are not auto-detected.

Look at the file `describe-image.py`. This script passes an image and a prompt to the model via the API.

First, check out some sample images:

```bash
> ls ~/GroceryStoreDataset/sample_images/natural/
Alpro-Fresh-Soy-Milk.jpg  Banana.jpg        Green-Bell-Pepper.jpg  Oatly-Natural-Oatghurt.jpg  Vine-Tomato.jpg
Arla-Standard-Milk.jpg    Granny-Smith.jpg  Lemon.jpg              Pink-Lady.jpg               Yellow-Onion.jpg
```

Open this folder in VSCode and **inspect the images** visually.

Now try describing an image:

```python
python3 describe-image.py ~/GroceryStoreDataset/sample_images/natural/<pick a file>.jpg
```

You should see a full visual description of the object in the image.

### 🏷️ Classifying Images

So far, the model is generating full descriptions. But we can also ask it to **classify** an image.

Open `classify-image.py`. The goal is for the model to return a **label** — just one class name — like “Apple”, “Carrots”, or “Yoghurt”.

The classification logic lives entirely in the **prompt**.

**Your task**: Write a prompt that makes the model output **only the class name**, and nothing else. No explanations, no extra sentences. Just the label.

To help you, here’s the complete list of available classes:

```
Apple, Avocado, Banana, Kiwi, Lemon, Lime, Mango, Melon, Nectarine, Orange, Papaya, Passion-Fruit, Peach, Pear, Pineapple, Plum, Pomegranate, Red-Grapefruit, Satsumas, Juice, Milk, Oatghurt, Oat-Milk, Sour-Cream, Sour-Milk, Soyghurt, Soy-Milk, Yoghurt, Asparagus, Aubergine, Cabbage, Carrots, Cucumber, Garlic, Ginger, Leek, Mushroom, Onion, Pepper, Potato, Red-Beet, Tomato, Zucchini
```

After writing your prompt, test it:

```bash
> python3 classify-image.py ~/GroceryStoreDataset/sample_images/natural/Banana.jpg
Banana
> python3 classify-image.py ~/GroceryStoreDataset/sample_images/natural/Pink-Lady.jpg
Apple
```

### 📊 Classifying the Dataset

Now that you can classify a single image, let’s try **evaluating** the model on part of the dataset.

Edit `classify-dataset.py` and add your prompt.

Then run:

```bash
python3 classify-dataset.py
```

This script will:

* Load random images from the training dataset
* Classify them using your prompt
* Compare the model output to the ground truth
* Print a **running accuracy score**

For example:

```
Beef-Tomato_007.jpg
Tomato => Tomato
accuracy: 0.79 | total = 14
```

> Press **CTRL+C** to stop the script early. It runs continuously, and full evaluation would take a long time.

### 🔍 What to Expect

* The model will misclassify some images — that’s okay. It was never trained on this specific dataset.
* Classification performance won’t be lightning-fast. These are large, general-purpose models running on GPUs.
* But it’s remarkable: you now have a **fully working image classifier** with **zero training**.

No MobileNet, no PyTorch, no fine-tuning. Just LLM + image + prompt.
