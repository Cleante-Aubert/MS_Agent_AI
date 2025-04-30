import requests

API_URL = "http://localhost:8000/generate_fiche"

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
        response = requests.post(f"{API_URL}", json=payload, headers=headers, timeout=100, verify=False)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Erreur lors de l'appel à l'API : {e}"
