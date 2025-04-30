from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.cosmos_db import CosmosDBManager
from backend.fiche_generator import generate_fiche
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db = CosmosDBManager()


'''
CORS
'''

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:8501"] si tu veux restreindre à Streamlit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''
User
'''

class User(BaseModel):
    userEmail: str
    nom: str = ""
    prenom: str = ""
    password: str

@app.post("/register")
def register(user: User):
    try:
        db.add_user(user.dict())
        return {"message": "Utilisateur créé"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
def login(user: User):
    result = db.get_user(user.dict())
    if result:
        return {"message": "Connexion réussie", "user": result}
    raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")    

'''
Generation
'''

class FicheRequest(BaseModel):
    titre: str
    secteur: str
    contrat: str
    niveau: str
    competences: str

@app.post("/generate_fiche")
def generate_fiche_route(request: FicheRequest):
    try:
        content, fiche_id = generate_fiche(
            titre=request.titre,
            secteur=request.secteur,
            contrat=request.contrat,
            niveau=request.niveau,
            competences=request.competences
        )

        job_info = {
            "titre": request.titre,
            "secteur": request.secteur,
            "contrat": request.contrat,
            "niveau": request.niveau,
            "competences": request.competences,
            "metadata": {
                "source": "générée_par_HiRo"  # ou autre tag pour différencier la provenance
            }
        }

        doc_id = db.add_job_description(job_info, content)


        return {"fiche_id": fiche_id, "fiche": content, "document_id":doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
