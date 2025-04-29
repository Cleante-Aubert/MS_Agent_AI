import os
import numpy as np
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from backend.cosmos_db import CosmosDBManager
from backend.embedding import generate_embedding_cognitive

load_dotenv()

db = CosmosDBManager()

cv_container = db.cv_container

cvs = db.list_cvs()

def fetch_fiche_from_cosmos_db(keyword):
    print(f"Fetching fiche with keyword: {keyword}")
    try:
        fiche = db.get_job_description(keyword)
        if fiche :
            print(f"La fiche de poste a été retrouvé !")
            return fiche
        else:
            raise ValueError(f"Aucune fiche de poste trouvée avec : {keyword}")
    except ValueError as ve:
        print(f"Error fetching fiche: {ve}")
        raise

def fetch_all_fiches_from_cosmos_db():
    return db.list_cvs()


def competence_matching(fiche_competences, cvs):
    matched_candidates = []
    fiche_comp_set = set([comp.lower() for comp in fiche_competences])

    for cv in cvs:
        cv_comp_set = set([comp.lower() for comp in cv.get("competences", [])])
        if not cv_comp_set:
            continue
        common = fiche_comp_set.intersection(cv_comp_set)
        if common:
            score = len(common) / len(fiche_comp_set) * 100
            matched_candidates.append({
                "candidat_nom": cv.get("nom"),
                "candidat_prenom": cv.get("prenom"),
                "candidat_email": cv.get("email"),
                "match_score": round(score, 2),
                "competences_communes": list(common)
            })
            
    matched_candidates.sort(key=lambda x: x["match_score"], reverse=True)
    return matched_candidates

## Matching par contenu texte (TF-IDF)
def text_matching(fiche_content, cvs):
    documents = [fiche_content] + [cv.get("content") for cv in cvs if cv.get("content")]
    vectorizer = TfidfVectorizer(stop_words='french')
    tfidf_matrix = vectorizer.fit_transform(documents)

    fiche_vector = tfidf_matrix[0]
    cvs_vectors = tfidf_matrix[1:]

    scores = cosine_similarity(fiche_vector, cvs_vectors).flatten()
    matched_candidates = []

    for i, score in enumerate(scores):
        matched_candidates.append({
            "candidat_nom": cvs[i].get("nom"),
            "candidat_prenom": cvs[i].get("prenom"),
            "candidat_email": cvs[i].get("email"),
            "match_score": round(score * 100, 2)
        })

def add_embedding_to_candidates(cvs, container):
    for cv in cvs:
        if not cv.get("embedding"):
            print(f"Generating embedding for {cv.get('email')}")
            contenu_cv = cv.get("content")
            if contenu_cv:
                embedding = generate_embedding_cognitive(contenu_cv)
                cv["embedding"] = embedding
                container.upsert_item(cv)
            else:
                print(f"Aucun contenu trouvé pour le CV de {cv.get('email')}")

## Matching par embedding qui recherche les 5 meilleurs candidats
def embedding_matching(fiche_content, cvs):
    fiche_embedding = generate_embedding_cognitive(fiche_content)

    if isinstance(fiche_embedding, dict):
        fiche_embedding = fiche_embedding.get("data",[])[0].get("embedding",[])

    fiche_vector = np.array(fiche_embedding).reshape(1, -1)

    matched_candidates = []

    for cv in cvs:
        cv_embedding = cv.get("embedding")

        if isinstance(cv_embedding, dict):
            cv_embedding = cv_embedding.get("data",[])[0].get("embedding",[])

        if cv_embedding:
            cv_vector = np.array(cv_embedding).reshape(1, -1)
            score = cosine_similarity(fiche_vector, cv_vector)[0][0]
            matched_candidates.append({
                "candidat_nom": cv.get("nom"),
                "candidat_prenom": cv.get("prenom"),
                "candidat_email": cv.get("email"),
                "match_score": round(score*100, 2)
            })

    matched_candidates.sort(key=lambda x: x["match_score"], reverse=True)
    return matched_candidates[:10] # Retourne les 10 meilleurs candidats

def match_candidats(keyword):
    fiche = db.get_job_description(keyword)
    if fiche:
        print(f"La fiche de poste a été retrouvé !")
    else:
        print(f"Aucune fiche de poste trouvée avec : {keyword}")
        return

    cvs = fetch_all_fiches_from_cosmos_db()

    add_embedding_to_candidates(cvs, cv_container)

    print("\n--- Matching par compétences ---")
    results_competences = competence_matching(fiche["competences"], cvs)
    for result in results_competences:
        print(result)

    print("\n--- Matching par Azure Embedding ---")
    results_embedding = embedding_matching(fiche["content"] ,cvs)
    for result in results_embedding:
        print(result)


if __name__ == "__main__":
    keyword = input("Recherche Fiche de poste : ").strip()
    match_candidats(keyword)