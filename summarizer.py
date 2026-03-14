import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize(text, query=""):

    text = text[:10000]

    prompt = f"""
You are an AI research assistant.

User question:
{query}

Research data:
{text}

Explain the answer clearly and simply.
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text