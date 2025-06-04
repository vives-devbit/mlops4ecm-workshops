
# 🖼️ Lab 3 – Add an Image to Guide the Story

<img src="../../media/generative-ai-input-image.png" style="width: 300px" align="right">

In this lab, you'll take your generative AI skills one step further by introducing **images as input**. You'll explore how vision-capable language models can interpret images and use them to influence their output — either by describing them directly or by using them to guide a story.

This lab is split into two parts:
1. **Play with vision models by prompting them to use images**
2. **Integrate an image directly into your storytelling assistant**

> ✅ Make sure you're still connected to your **remote virtual machine** using VS Code, just like in the previous labs.

## 🧪 Part 1 – `image-prompt.ipynb`

In the first notebook, you’ll interact with a **vision-capable large language model** (e.g. Gemma 3) by giving it an image and a user prompt. The model will try to understand the image and respond accordingly.

### 🔧 What to do:

1. Open the notebook:

```
generative-ai/03-add-input-image/image-prompt.ipynb
````

2. If VS Code asks you to select a Python environment, choose the `.venv` that was created in Lab 2. It should be the first option.

3. Provide an image file (e.g. `image.jpg`, `picture.png`, etc.). You can use JPG, PNG, or other common formats — just make sure the file is in the same folder as the notebook. You can drag images from your Windows laptop into the folder in VS Code.

4. Edit the variable:

```python
path_to_image = "your-image.jpg"
````

and write your own prompt, for example:

```python
user_prompt = "Classify this image as indoor or outdoor."
```

Can you extend the prompt so that the model only responds with "indoor" or "outdoor", and nothing else?

5. Press **Run All** to execute the notebook.

### 🧠 Experiment:

* Try using different image types — simple vs complex, realistic vs abstract.
* Try different model sizes, especially larger ones (`gemma3:12b-it-qat`), to see how accuracy improves.
* Ask the model to:
  * Detect specific objects (dogs, cats, trees, flowers)
  * Classify by category (city/nature, apple/banana/pear)
  * Summarize or interpret the scene creatively

## 📖 Part 2 – `storytelling-with-image.ipynb`

In this second notebook, you’ll take your storytelling assistant from Lab 2 and give it **visual context** by passing in an image to inspire the story.

### 🔧 What to do:

1. Open the notebook:

   ```
   generative-ai/03-add-input-image/storytelling-with-image.ipynb
   ```

2. Provide an image file called `scene.jpg` (or another format like `.png` if you prefer). This image will be used as the **setting or inspiration** for your story.

3. Write a **user prompt** like:

   ```python
   "One of the objects in this scene becomes alive."
   ```

4. The notebook uses a system prompt + user prompt + image file path. This allows the model to use the image to shape the story setting, tone, and characters.

5. Press **Run All** to generate your story.

## ✅ What You’ve Learned in This Lab

By completing this lab, you now know how to:

* Use **vision-enabled LLMs** to interpret and analyze images
* Combine **text + image inputs** to guide generation
* Enhance your storytelling assistant with real-world visual context
