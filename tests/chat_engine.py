import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

deployment = "gpt-4o"

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)


print("Lancement de HiRo ...")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Tu es HiRo, un assistant virtuel spécialisé en Ressources Humaines.",
        },
        {
            "role": "user",
            "content": "Je suis un employé qui a besoin d'aide pour comprendre mes droits en matière de congés payés. Peux-tu m'expliquer ce que sont les congés payés et comment je peux en bénéficier ?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)
