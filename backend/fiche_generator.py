import getpass
import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from backend.cosmos_db import CosmosDBManager
from dotenv import load_dotenv
import uuid


load_dotenv()

if not os.environ.get("AZURE_OPENAI_API_KEY"):
  os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass("Enter API key for Azure: ")

client = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
)


def load_prompt_from_env_hiro(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

template = load_prompt_from_env_hiro("./config/prompts/prompt_env_hiro.txt")


prompt = PromptTemplate(input_variables=["titre", "secteur", "contrat", "niveau", "competences"], template=template)
llm_chain = LLMChain(llm=client, prompt=prompt)


def generate_fiche(titre,secteur,contrat, niveau, competences, source=""):
   result = llm_chain.run(
      titre=titre,
      secteur=secteur,
      contrat=contrat,
      niveau=niveau, 
      competences=competences
  ).strip()
   
   result = CosmosDBManager.clean_duplicate_lines(result)
   
   print("Résultat de l'IA : ", result)
   
   fiche_id = str(uuid.uuid4())
   fiche = {
        "id": fiche_id,
        "titre": titre,
        "secteur": secteur,
        "contrat": contrat,
        "niveau": niveau,
        "competences": competences.split(", "),
        "content": result,
        "metadata": {
            "source": source,
            "upload_date": "2023-10-01"
        }
     }
   db = CosmosDBManager()
   pdf_base64 = db.generate_pdf_from_text(result)
   fiche["fichierPDF"] = pdf_base64

   if not isinstance(result, str):
      raise ValueError("Le texte de la fiche de poste doit être une chaîne de caractères.")

   try:
      db.add_job_description(job_info=fiche, job_description=result)
      print(f"Fiche de poste ajoutée avec succès, ID : {fiche_id}")
   except Exception as e:
    print(f"Erreur lors de l'ajout de la fiche de poste : {e}")
    raise
   
   return result, fiche_id

_all_ = ["generate_fiche"]

if __name__ == "__main__":
    titre = "Advisor Data Scientist"
    secteur = "Technologie"
    contrat = "CDI"
    niveau = " 10 ans d'expérience"
    competences = "Python, SQL, Machine Learning, Data Analysis, Data Visualization, Big Data, Cloud Computing, Data Engineering, Data Science, Business Intelligence, Data Warehousing, ETL, Tableau, Power BI, Hadoop, Spark, NoSQL, MongoDB, R, SAS, TensorFlow, PyTorch"
    

    # Générer la fiche de poste
    fiche_poste, fiche_id = generate_fiche(titre, secteur, contrat, niveau, competences)

    
    # Afficher la fiche de poste générée
    print("Fiche de Poste générée :\n")
    print(fiche_poste)
    print("Fiche générée :\n", fiche_poste)










## if __name__ == "__main__":
## 
##     titre = "Développeur Backend"
##     secteur = "Technologie"
##     contrat = "CDI"
##     niveau = "5 ans d'expérience"
##     competences = "Python, Django, SQL, API REST"
## 
##     # Générer la fiche de poste
##     fiche_poste = generate_fiche(titre, secteur, contrat, niveau, competences)
## 
##     # Afficher la fiche de poste générée
##     print("Fiche de Poste générée :\n")
##     print(fiche_poste)
## 
## 
## ## Pour faire un import de ce fichier, il faut faire :
## _all_ = ["generate_fiche"]



