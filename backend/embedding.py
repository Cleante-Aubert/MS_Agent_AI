import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_embedding_cognitive(text: str) -> list:
    url = os.environ["AZURE_EMBEDDING_ENDPOINT"]
    api_key = os.environ["AZURE_EMBEDDING_API_KEY"]

    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }

    payload = {
        "imput":text,
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        embedding = response.json()
        return embedding["data"][0]["embedding"]
    else:
        raise Exception(f"Error generating embedding: {response.status_code} - {response.text}")

