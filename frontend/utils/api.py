import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


API_URL = "https://127.0.0.1:8443"

def generate_fiche_api(titre, secteur, contrat, niveau, competences):
    try:
        payload = {
            "titre": titre,
            "secteur": secteur,
            "contrat": contrat,
            "niveau": niveau,
            "competences": competences
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{API_URL}/generate_fiche", json=payload, headers=headers, timeout=100, verify=False)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Erreur lors de l'appel à l'API : {e}"
    
@staticmethod
def register_user(email, password, nom="", prenom=""):
    """Enregistre un nouvel utilisateur."""
    url = f"{API_URL}/register"
    payload = {
        "userEmail": email,
        "password": password,
        "nom": nom,
        "prenom": prenom
    }
    
    try:
        response = requests.post(url, json=payload, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@staticmethod
def login_user(email, password):
    """Authentifie un utilisateur."""
    url = f"{API_URL}/login"
    payload = {
        "userEmail": email,
        "password": password
    }
    
    try:
        response = requests.post(url, json=payload, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@staticmethod
def get_job_postings():
    """Récupère toutes les fiches de poste."""
    url = f"{API_URL}/list_job_descriptions"
    
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@staticmethod
def add_cv(cv_file, candidate_info):
    """Ajoute un CV pour un candidat."""
    url = f"{API_URL}/add_cv"
    
    files = {'cv_file': cv_file}
    
    try:
        response = requests.post(url, files=files, data=candidate_info, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@staticmethod
def match_candidates(job_id):
    """Trouve les meilleurs candidats pour une fiche de poste."""
    url = f"{API_URL}/match_candidates/{job_id}"
    
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}