from backend.cosmos_db import CosmosDBManager

def test_add_user():

    user_info = {
        "userEmail":"hubert@benoit.com",
        "prenom":"Benoit",
        "nom":"Hubert",
        "password":"ehzv456"
    }

    db = CosmosDBManager()

    try:
        id = db.add_user(user_info)
        print(f"l'utilisateur : {id} a été ajouté avec succès")
    except Exception as e : 
        print(f"Erreur lors de la création du user : {e}")

if __name__ == "__main__":
    test_add_user()