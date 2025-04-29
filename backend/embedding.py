import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_embedding_cognitive(text):
    url = os.environ["AZURE_EMBEDDING_ENDPOINT"]
    api_key = os.environ["AZURE_EMBEDDING_API_KEY"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key,
    }

    data = {
        "model": "text-embedding-ada-002",
        "input": text,
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        embedding_json = response.json()
        return embedding_json["data"][0]["embedding"]
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None