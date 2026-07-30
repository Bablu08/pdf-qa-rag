import os
from groq import Groq

client = None

def ask_llm(prompt):
    global client

    if client is None:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_completion_tokens=512,
        top_p=1,
        stream=True
    )