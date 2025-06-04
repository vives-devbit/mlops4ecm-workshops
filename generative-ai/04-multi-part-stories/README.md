
# 🧩 Lab 4 – Chain Model Calls to Build Multi-Part Stories

<img src="../../media/chaining-llms.png" style="width: 300px" align="right">

In the previous labs, you used a large language model (LLM) to generate stories in a single step. In this lab, you're going to take a more structured approach: you'll **chain multiple model calls** to build a longer, coherent story in multiple parts.

The key idea is that LLMs are **stateless** — they don't remember what they said before — so if you want the story to flow from beginning to end, **you need to pass the context yourself**.

By the end of this lab, you will have built a multi-part storytelling system where:
- The LLM first generates a **table of contents** (abstracts) for the story
- Then, it writes each part of the story **one chapter at a time**
- You accumulate the story progressively to maintain context
- The full story is displayed in a nicely formatted way

## ✅ What You'll Learn

- How to break up a complex generation task into smaller steps
- How to **call a language model multiple times** in a loop
- How to structure prompts for chaining model outputs
- How to maintain context across calls by accumulating text

## 🧭 Getting Started

Just like in the previous labs:

1. Open **Visual Studio Code**
2. Connect to your **remote virtual machine** (using the green/blue button in the bottom-right)
3. Navigate to the folder:

```

generative-ai/04-multi-part-stories/

```

4. Open the notebook:

```

story-generation.ipynb

````

## 🛠️ Choose a Story Idea

Scroll to the top of the notebook. In the **configuration section**, find the variable:

```python
story_idea = ""
````

✍️ **Your task:** Fill in a short creative idea to use as the foundation for your story.
Here are some examples:

* `"A robot falls in love with a toaster."`
* `"A lonely fox discovers a talking stone in the forest."`
* `"A spaceship crash lands on a mysterious ocean planet."`

🔒 The line below contains an `assert` to make sure you don’t forget to fill it in.

## 📖 Generate the Table of Contents

In the next section of the notebook, the model will generate a **series of short abstracts**, one for each part of the story. This is done using a prompt that tells it *not* to write the full story — just the chapter titles or summaries.

```python
abstracts_raw = response_toc['message']['content'].strip()
```

But the model response is just one big string!
👉 That’s where your next **TODO** comes in.

### 🛠️ TODO: Parse the abstracts into a list

Find this section:

```python
# TODO: Turn the raw response into a list of clean one-line abstracts
# Make sure to remove empty lines and extra whitespace.
# Hint: Use .split("\n") to break lines, then .strip() to remove whitespace.
abstracts = []
```

💡 **Tip:** Use `.split("\n")` to break the response into separate lines. Then use `.strip()` to remove any extra spaces or newlines around each line. You can use a simple `for` loop to go through each line and add it to the `abstracts` list using `.append()`.

Make sure you end up with a list of clean strings like:

```python
["The robot meets a toaster.", "They build a life together.", "A storm threatens their home.", ...]
```

## ✍️ Generate Each Chapter

This is where the story comes alive. For each abstract, you'll ask the model to write 1–2 paragraphs of story text.

Inside the loop, you’ll see that the **system prompt** and **user prompt** are designed to pass:

* The **abstracts for the full story**
* The **story so far** (so the model remembers what happened)

### 🛠️ TODO: Accumulate the full story as you go

Find this `TODO`:

```python
# TODO: Accumulate the story so far by appending this chapter
# (Hint: use += to add the current chapter text)
# full_story_so_far = ...
```

💡 **Tip:** After each new chapter is generated, append it to the `full_story_so_far` string using `+=`.
You may want to add a couple of **newlines** between chapters for readability.

## 📚 Display the Final Story

At the end of the notebook, the full story will be displayed — chapter by chapter — with titles and text output using Markdown formatting:

```python
  display(Markdown(f"### Part {i+1}: {abstract}\n\n"))
  display(Markdown(chapter_text))
```

🎉 That's it! You've now written a complete, multi-part story with coherent structure and narrative flow — by chaining model outputs together.

## 🎬 Bonus Exercise – Add a Cliffhanger

Want to keep your readers hooked between chapters?

**Your task:**  
Modify the generation prompt so that each chapter ends on a **cliffhanger** — a suspenseful moment that makes the reader want to continue.

💡 *Hints:*  
- Adjust the `system_prompt_chapter` to include something like:
  > “Always end each part with a dramatic or emotional cliffhanger that leads into the next chapter.”
- The rest of your code can stay the same — just tweak the prompt and regenerate the story.
- Experiment with different tones (mysterious, dramatic, funny...) to change the effect.

## 📝 Bonus Exercise – Generate Better Titles

Right now, each story part uses the original abstract as its title. But you can do better!

**Your task:**  
Write an extra LLM call for each chapter to generate a more engaging, creative, or poetic title — based on the full chapter text that was just written.

💡 *Hints:*  
- After you generate a chapter, send it back to the model with a new prompt like:
  > “Give this story part a short, catchy title. Be creative, but keep it under 10 words.”
- Store the title in a separate variable and use it when displaying the final story.
- Compare the original abstract vs. the generated title to see which works better.
