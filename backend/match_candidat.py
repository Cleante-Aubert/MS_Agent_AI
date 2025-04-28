from extract_cv import extract_cv_text
from fiche_generator import generate_fiche
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from backend.cosmos_db import CosmosDBManager
from backend.embedding import generate_embedding_cognitive  

import numpy as np

load_dotenv()

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

def match_cv_and_fiche(email :str, fiche_id:str) -> float:
    db = CosmosDBManager()
    cv = db.get_cv_by_email(email)
    fiche = db.get_job_description_by_id(fiche_id)
    
    if not cv or not fiche:
        raise ValueError("CV ou fiche de poste introuvable.")
    
    cv_embedding = generate_embedding_cognitive(cv["content"])
    fiche_embedding = generate_embedding_cognitive(fiche["content"])
    
    score = cosine_similarity(cv_embedding, fiche_embedding)
    return round(score, 2)






### def match_cv_to_fiche(cv_path : str, fiche_path : str) -> str: 
###     """
###     Compare un CV avec une fiche de poste et retourne un score de correspondance.
###     
###     :param cv_path: Chemin vers le fichier CV (.pdf ou .docx)
###     :param fiche_path: Chemin vers le fichier de la fiche de poste (.txt)
###     :return: Score de correspondance entre 0 et 100
### 
###     """
###     
###     # Extraire le texte du CV
###     cv_text = extract_cv_text(cv_path)
###     
###     # Charger la fiche de poste
###     with open("../config/prompts/comparaison_cv.txt", 'r', encoding='utf-8') as file:
###         fiche_text = file.read()
### 
###     # Initialiser le modèle LLM
###     client = AzureChatOpenAI(
###         azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
###         azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
###         openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
###         openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
###     )
###     
###     # Créer un prompt pour évaluer la correspondance
###     prompt_template = "Évaluez la correspondance entre le CV suivant et la fiche de poste suivante de manière très simpliste en 3 lignes. Donnez un score entre 0 et 100.\n\nCV:\n{cv}\n\nFiche de Poste:\n{fiche_poste}\n\n."
###     prompt = PromptTemplate(input_variables=["cv", "fiche_poste"], template=prompt_template)
###     
###     llm_chain = LLMChain(llm=client, prompt=prompt)
###     
###     # Exécuter le modèle pour obtenir le score de correspondance
###     result = llm_chain.invoke({
###         "cv": cv_text,
###         "fiche_poste": fiche_path
###         })
###     
###     return result
### 
### ## Exemple d'utilisation
### 
### if __name__ == "__main__":
###     fiche = generate_fiche("Développeur Backend", "Technologie", "CDI", "5 ans d'expérience", "Python, Django, SQL, API REST")
###     cv_file = "../data/cv/Chloé_Bernard_CV.pdf"
### 
###     resultat = match_cv_to_fiche(cv_file, fiche)
### 
### 
###     print("Résultat de la correspondance :", resultat)