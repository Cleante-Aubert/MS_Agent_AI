# Assistant RH intelligent 

Dans le cadre du Hackaton organisé par Microsoft dans le thème de l'intelligence artificielle, nous développerons un assitant RH intelligent visant à simplifier le processus de recrutement. Cet outil sera capable de générer des fiches de poste et d'évaluer les candidats en fonction de ces fiches.

## Composants

### 1. Frontend
- **Streamlit** (Framework Python)

### 2. Backend
- **Azure OpenAI** via SDK en Python
- **LangChain** pour la logique :
    - Génération contrôlée (fiche de poste)
    - Similarité sémntique fiche ⇔ CV (RAG)

- Stockage vectoriel pour les CV (FAISS ou Azure Cognitive Search)
- Déploiement : ???
- Hébergement : **Azure**

### 3. RAG - Base de connaissance
- Données internes RH (modèles de fiches, critères de sélection, process, ...)
- Intégrer avec LangChain + retriever

## Architecture de notre application