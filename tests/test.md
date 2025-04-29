# Script pour intéragir avec le modèle 4o GPT, déployé sur Azure (avec Azure AI Foundry)


## Variable d'environnement nécessaire

- Un compte Azure avec accès à l'instance **Azure OpenAI**.
- Les informations suivantes doivent être disponibles :
  - `AZURE_OPENAI_API_KEY` (clé API)
  - `AZURE_OPENAI_ENDPOINT` (URL de l'endpoint Azure OpenAI)
  - `AZURE_OPENAI_API_VERSION` (version de l'API, ex: `2024-04-01-preview`)
  - Nom du **déploiement** associé au modèle (ex: `gpt-4o`)
  Les informations sont disponibles dans votre interface de déploiement du modèle sur Azure Foundry.

## 📄 Contenu du Script

- Utilisation de la bibliothèque `openai` (Azure OpenAI).
- Chargement des variables d'environnement via `python-dotenv`.
- Création d'une session avec un déploiement GPT-4.0.
- Envoi d'un prompt simulant une conversation entre un employé et l'assistant HiRo.
- Affichage de la réponse du modèle dans le terminal.