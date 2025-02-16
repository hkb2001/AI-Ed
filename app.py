import os
from dotenv import load_dotenv
from openai import OpenAI
import re
load_dotenv()

api_key = os.getenv('AIMLAPI_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the AIMLAPI_KEY environment variable.")

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=api_key,    
)

def get_response(user_query):
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1",
        messages=[
            {
                "role": "system",
                "content": "You are an AI teaching assistant...",
            },
            {
                "role": "user",
                "content": user_query,
            },
        ],
        max_tokens=500,
        temperature=0.7, 
        top_p=0.9, 
        # response_format="text"
    )

    message = response.choices[0].message.content
    clean_message = re.sub(r"<think>.*?</think>", "", message, flags=re.DOTALL).strip()
    return clean_message

