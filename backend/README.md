[**Lien de démarrage pourutiliser Azure AI en Python**](https://learn.microsoft.com/fr-fr/azure/ai-services/openai/quickstart?tabs=bash%2Ckeyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-python)

[**LanChain - Python & Azure**](https://python.langchain.com/docs/introduction/)

Ce projet implémente un backend pour un agent intelligent permettant de faire un match entre des CV et des fiches de poste. Il utilise des techniques de traitement du langage naturel (NLP), d'embedding, ainsi que des appels à une base de données Cosmos DB pour gérer les CV et les fiches de poste.

## Structure du projet

Le backend est composé de plusieurs modules principaux :

- **`cosmos_db.py`** : Gestion de l'intégration avec la base de données Cosmos DB.
- **`embedding.py`** : Génération d'embeddings pour les fiches de poste et les CV.
- **`extract_cv.py`** : Extraction et traitement des informations contenues dans les CV.
- **`fiche_generator.py`** : Génération et gestion des fiches de poste.
- **`match_candidat.py`** : Module principal de matching des candidats en fonction des compétences et des embeddings.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Les bibliothèques suivantes sont nécessaires pour faire fonctionner le projet :

- `requests`
- `numpy`
- `sklearn`
- `python-dotenv`
- `azure-cosmos`

Vous pouvez installer ces dépendances via `pip` en exécutant la commande suivante :

```bash
pip install -r requirements.txt
