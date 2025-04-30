import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


API_URL = "https://127.0.0.1:8443/generate_fiche"

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