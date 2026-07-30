import os
from groq import Groq

client = None

def ask_llm(prompt):
    global client

    if client is None:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))