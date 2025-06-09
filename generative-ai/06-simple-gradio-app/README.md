# 🛠️ Lab 6 – Build Your First Gradio App

<img src="../../media/generative-ai-wizard-chatting.png" style="width: 300px" align="right">

In this lab, you'll learn how to create small, functional **web apps with Gradio** that connect to large language models and diffusion models.

Each example in this lab builds a **simple user interface** that takes user input, runs a model, and displays the result — all on your **own virtual machine**.

### ✅ Getting Started

Make sure you're still connected to your **virtual machine** using **Visual Studio Code + Remote SSH**, just like in the earlier labs.

You'll find the Gradio examples in this folder:

```
generative-ai/06-simple-gradio-app/
```

## 🧠 Example 1 – Text-to-Text with an LLM

Open the notebook:

```
06a-text-to-text-llm.ipynb
````

This example shows how to connect a simple **text input box** to a **language model** using Gradio.

### 🛠️ TODO:
Find this line in the code:

```python
{"role": "user", "content": }  # ← TODO
````

Fill it in with:

```python
{"role": "user", "content": prompt}
```

This sends the user's input into the model.

### 🌐 Run the App:

Once the app starts, open your browser and go to:

```
http://<your-ip>:8080
```

Replace `<your-ip>` with the IP address of your VM. You should see your Gradio app running!

### ⚠️ Note on Port Conflicts

Gradio apps use **port 8080** by default. If you **run the same cell again**, or try to launch another app while one is still running, you may see an error like:

```
OSError: [Errno 98] Address already in use
```

This means a previous app is still running in the background.

💡 **Quick fix:**

Open a terminal and type:

```
pkill python
```

This will stop all Python processes and free up the port so you can try again.

## 🖼️ Example 2 – Text-to-Image (Diffusion)

Open the next notebook:

```
06b-image-generation.ipynb
```

This app uses a **Stable Diffusion** model to generate an image from a text prompt.

### 🛠️ TODO:

In the code, find the missing value for:

```python
num_inference_steps=  # ← TODO
```

Set it to something like `20`:

```python
num_inference_steps=20
```

This controls how detailed the image generation process will be.

### 🌐 Run the App:

Launch the cell and go again to:

```
http://<your-ip>:8080
```

Type a prompt like:

> A robot sailing on a rubber duck in a stormy ocean

And see what comes out!

## 🧠 Example 3 – Image-to-Text (Vision LLM)

Now open:

```
06c-vision-to-text-llm.ipynb
```

This app lets you upload an image and ask a question about it. The model looks at the image and responds.

### 🛠️ TODO:

Find this placeholder in the code:

```python
"images": [...]  # ← TODO
```

Replace it with:

```python
"images": ["image.jpg"]
```

This tells the model which image file to use.

Then launch the app and test it by uploading an image and asking:

> What’s going on in this picture?

## 💬 Example 4 – Stateful Chatbot

Finally, open:

```
06d-chatbot-with-history.ipynb
```

This app builds a **chatbot that remembers what you said**. It uses Gradio’s `gr.Chatbot` component and a `gr.State` variable to keep the full history of the conversation.

### 🤔 Why This Matters

In the first example, the model **forgot everything** after each turn — it had no memory.

In this example, each message is added to a list of messages, and the model receives the full history every time it generates a reply. That’s how you build a chatbot with memory.

There’s **no TODO** in this notebook — just read through the code, try it out, and see how it works.

## 🌟 Bonus Exercise – Build Your Own AI App

Now that you've explored the core building blocks — language models, diffusion models, vision models, and Gradio — it's time to try combining them into something **uniquely your own**.

Can you create a **custom app** that mixes text, images, and interaction?

Try starting from one of the notebooks and expanding it. Add a second model, chain the outputs together, or wrap the whole thing in a new interface.

Here are some wild ideas to spark your creativity:

- 🍜 **AI Recipe Maker**: Upload a photo of ingredients → get a recipe → generate an image of the final dish.
- 🎨 **Logo Designer**: Type your startup idea → generate a logo or icon using a diffusion model.
- 🗺️ **Travel Planner**: Enter a destination and your budget → LLM generates a travel plan with local highlights.
- 🛋️ **Room Re-designer**: Upload a photo of your room → get suggestions for layout and furniture style → generate a visual preview.

**You don’t need to finish anything fancy.** The goal is to experiment, combine, and see what happens.

## 🎉 You Did It!

You now know how to:

* Build simple web apps using Gradio
* Connect models to real-time user input
* Work with both text and images
* Keep track of conversation history

These are the building blocks for your own creative applications!
