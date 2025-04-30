from backend.cosmos_db import CosmosDBManager


# Test pour ajouter un CV dans CosmosDB
def test_add_cv():
    # Chemin du fichier CV (PDF ou DOCX)
    cv_file_path = "./data/cv/Chloé_Bernard_CV.pdf"  # Change le chemin selon ton fichier


    # Informations du candidat (exemple)
    candidat_info = {
        "nom": "Paolo",
        "prenom": "Dybala",
        "email": "paolo.dybala@email.com",
        "competences": ["Python", "Java", "SQL", "Advisor Senior", "Expert"],
        "metadata": {
            "source": "Monster",
            "upload_date": "2024-02-10"
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
