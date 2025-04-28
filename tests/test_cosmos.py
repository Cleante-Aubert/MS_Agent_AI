from backend.cosmos_db import CosmosDBManager
import uuid
import os
import base64

# Test pour ajouter un CV dans CosmosDB
def test_add_cv():
    # Chemin du fichier CV (PDF ou DOCX)
    cv_file_path = "./data/cv/Chloé_Bernard_CV.pdf"  # Change le chemin selon ton fichier

    # générer un identifiant unique pour le CV
    cv_id = str(uuid.uuid4())

    # Informations du candidat (exemple)
    candidat_info = {
        "id": cv_id,  # Identifiant unique pour le candidat
        "candidatId": "samuel.mbaye@example.com",
        "nom": "Mbaye",
        "prenom": "Samuel",  # Base64 du fichier PDF
        "email": "samuel.mbaye@example.com",
        "competences": ["Python", "Django", "SQL", "API REST"],
        "metadata": {
            "source": "LinkedIn",
            "upload_date": "2023-10-01"
        }
    }

    # Initialiser le gestionnaire CosmosDB
    db = CosmosDBManager()

    # Ajouter le CV dans CosmosDB
    try:
        cv_id = db.add_cv(cv_file_path, candidat_info)
        print(f"CV ajouté avec succès, ID : {cv_id}")
    except Exception as e:
        print(f"Erreur lors de l'ajout du CV : {e}")

# Lancer le test si ce fichier est exécuté directement
if __name__ == "__main__":
    test_add_cv()
