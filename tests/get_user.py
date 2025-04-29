from backend.cosmos_db import CosmosDBManager

def test_get_user():
    # Données utilisateur à tester (doit exister dans la base)
    user_info = {
        "userEmail": "hubert@benoit.com",
        "password": "ehzv456"
    }

    db = CosmosDBManager()

    try:
        user = db.get_user(user_info)

        if user:
            print("Utilisateur récupéré avec succès :")
            print(f"Nom : {user['nom']}")
            print(f"Prénom : {user['prenom']}")
            print(f"Email : {user['userEmail']}")
        else:
            print("Échec de l'authentification ou utilisateur introuvable.")

    except Exception as e:
        print(f"Erreur lors de la récupération du user : {e}")

if __name__ == "__main__":
    test_get_user()