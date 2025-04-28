import os
import base64
from azure.cosmos import CosmosClient, exceptions
from azure.cosmos.partition_key import PartitionKey
from dotenv import load_dotenv
from backend.extract_cv import extract_cv_text
import uuid
import io
import reportlab.lib.pagesizes as pagesizes
from reportlab.pdfgen import canvas


load_dotenv()

class CosmosDBManager:
    def __init__(self):
        self.endpoint = os.environ["AZURE_COSMOS_ENDPOINT"]
        self.key = os.environ["AZURE_COSMOS_KEY"]
        self.database_name = "HiRoDatabase"
        self.cv_container="Cvs"
        self.fiche_container="FichesDePostes"

        # Initialize Cosmos client
        self.client = CosmosClient(self.endpoint, credential=self.key)

        # Create or get the database (cv)

        try:
            self.database = self.client.create_database_if_not_exists(id=self.database_name)
        except exceptions.CosmosResourceExistsError:
            self.database = self.client.get_database_client(self.database_name)
            print(f"Database {self.database_name} existe déjà.")
        except exceptions.CosmosHttpResponseError as e:
            print(f"Erreur lors de la création de la base de données : {e}")
            raise

        # Create or get container for cv

        try:
            self.cv_container = self.database.create_container_if_not_exists(
                id=self.cv_container,
                partition_key=PartitionKey(path="/candidatId"),
                indexing_policy={
                    "includedPaths": [
                        {"path": "/*"},
                    ],
                },
            )
        except exceptions.CosmosResourceExistsError:
            self.cv_container = self.database.get_container_client(self.cv_container)
            print(f"Container {self.cv_container} existe déjà.")

        except exceptions.CosmosResourceNotFoundError:
            print(f="Container {self.cv_container} existe déjà.")
            raise

        except exceptions.CosmosHttpResponseError as e:
            print(f"Erreur lors de la création du conteneur cv : {e}")
            raise

  

        # Create or get the container for job postings (fiche)
        try :
            self.fiche_container = self.database.create_container_if_not_exists(
                id=self.fiche_container,
                partition_key=PartitionKey(path="/ficheId"),
                indexing_policy={
                    "includedPaths": [
                        {"path": "/*"},
                    ],
                },
            )
        except exceptions.CosmosResourceExistsError:
            self.fiche_container = self.database.get_container_client(self.fiche_container)
            print(f"Container {self.fiche_container} existe déjà.")
        except exceptions.CosmosResourceNotFoundError:
            print(f"Container {self.fiche_container} n'existe pas.")
        except exceptions.CosmosHttpResponseError as e:
            print(f"Erreur lors de la création du conteneur fiche de poste : {e}")
            raise   


    def add_cv(self, cv_path, candidat_info, embedding=None):
           
           cv_text = extract_cv_text(cv_path)

           with open(cv_path, 'rb') as f:
               pdf_base64 = base64.b64encode(f.read()).decode('utf-8')
               

           source = candidat_info.get("source", "Unknown")

           id = str(uuid.uuid4())  # Generate a unique ID for the CV

           document = {
               "id": f"cv_{id}",
               "candidatId": candidat_info["email"],
               "nom": candidat_info["nom"],
               "prenom": candidat_info["prenom"],
               "email": candidat_info["email"],
               "competences": candidat_info["competences"],
               "fichierPDF": pdf_base64,
               # "embedding": embedding.tolist(),
               "content": cv_text,
               "metadata": {
                   "source": source,
                   "upload_date": candidat_info.get("uploadDate")
               }
           }
           
           if embedding is not None:
               document["embedding"] = embedding.tolist()

           try :
               response = self.cv_container.upsert_item(body=document)
               return response["id"]  # Return the ID of the inserted item
           except exceptions.CosmosHttpResponseError as e:
               print(f"Erreur lors de l'ajout du CV : {e}")
               raise
           except exceptions.CosmosResourceExistsError as e:
               print(f"Erreur : le document existe déjà : {e}")
               raise
           
    def generate_pdf_from_text(self, text):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=pagesizes.A4)
        c.drawString(100, 750, text)
        c.showPage()
        c.save()
        buffer.seek(0)

        pdf_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        return pdf_base64


        
    def add_job_description(self, job_info, job_description, embedding=None):

        job_id = str(uuid.uuid4())  # Generate a unique ID for the job description"

        if not isinstance(job_description, str):
            raise ValueError("Le texte de la fiche de poste doit être une chaîne de caractères.")


        pdf_base64 = self.generate_pdf_from_text(job_description)

        document = {
            "id": f"fiche_de_poste{job_id}",
            "ficheId": job_id,
            "fichierPDF": pdf_base64,
            "titre": job_info["titre"],
            "secteur": job_info["secteur"],
            "contrat": job_info["contrat"],
            "niveau": job_info["niveau"],
            "competences": job_info["competences"],
            "content": job_description,
            "embedding": embedding,
            "source": job_info["metadata"]["source"],
        }

        response = self.fiche_container.upsert_item(body=document)
        return response["id"]  # Return the ID of the inserted item
     
    def get_cv(self, email):
        """Recupere un CV par email du candidat"""
        query = f"SELECT * FROM c WHERE c.email = '{email}'"
        items = list(self.cv_container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items[0] if items else None
        
        
    def get_job_description(self, job_id):

        try:
            partition_key = job_id
            return self.fiche_container.read_item(item=job_id, partition_key=job_id)
        except Exception as e:
            print(f"Erreur lors de la récupération de la fiche de poste : {e}")
            return None
        
    def list_job_descriptions(self):
        """Recupere toutes les fiches de poste"""
        query = "SELECT * FROM c"
        items = list(self.fiche_container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items
        
    def list_cvs(self):
        query = "SELECT * FROM c"
        items = list(self.cv_container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items

    def search_cv_by_competence(self, competence):
        """Rechercher des CVs par compétence"""
        query = f"SELECT * FROM c WHERE ARRAY_CONTAINS(c.competences, '{competence}')"
        items = list(self.cv_container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items

    def search_cv_by_vector(self,embedding, top_k=5):
        """Rechercher des CVs par vecteur d'embedding"""
        query={
            "vector": embedding,
            "topK": top_k,
            "fields": ["id", "candidatId", "nom", "prenom", "email", "competences"],
        }

        results = self.cv_container.query_items(
            query="SELECT * FROM c VECTOR_SEARCH c.embedding ANN SEARCH @vector TOP_K @topK WITH EMBEDDING",  
            parameters=[
                {"name": "@vector", "value": query["vector"]},
                {"name": "@topK", "value": query["topK"]}
            ],
            enable_cross_partition_query=True
        )
        return list(results)
    
if __name__ == "__main__":
    # Exemple d'utilisation de CosmosDBManager
    db_manager = CosmosDBManager()

    # Ajouter un CV (exemple)
    candidat_info = {
        "nom": "Potier",
        "prenom": "Benjamin",
        "email": "potier.benjamin@yoyo.com",
        "competences": ["Python", "Django"],
        "source": "LinkedIn",
        "uploadDate": "2025-04-24"
    }
    cv_path = "./data/cv/Chloé_Bernard_CV.pdf" 
    db_manager.add_cv(cv_path, candidat_info)

    # Lister les CVs
    cvs = db_manager.list_cvs()
    print("Liste des CVs :", cvs)
           








