import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('AIMLAPI_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the AIMLAPI_KEY environment variable.")

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=api_key,    
)

response = client.chat.completions.create(
    model="deepseek/deepseek-r1",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant who knows everything.",
        },
        {
            "role": "user",
            "content": "Tell me, why is the sky blue?"
        },
    ],
)

message = response.choices[0].message.content

print(f"Assistant: {message}")