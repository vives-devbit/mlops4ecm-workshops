import ollama

prompt = "Hello, world!" # TODO Write your prompt here

response = ollama.chat(
    model='gemma3:4b',
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)

print(response['message']['content'])
