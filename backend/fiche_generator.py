import getpass
import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from backend.cosmos_db import CosmosDBManager
from dotenv import load_dotenv
import uuid
import base64
import io
import reportlab.lib.pagesizes as pagesizes
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from markdown2 import markdown


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


def clean_duplicate_lines(text):
    seen = set()
    cleaned_lines = []
    for line in text.split('\n'):
        if line not in seen:
            cleaned_lines.append(line)
            seen.add(line)
    return "\n".join(cleaned_lines)

def generate_pdf_from_text(text):
   buffer = io.BytesIO()

   doc = SimpleDocTemplate(buffer, pagesize=pagesizes.A4)
   elements = []

   style = getSampleStyleSheet()

   title_style = ParagraphStyle(
       name='TitleStyle',
       fontSize=18,
       spaceAfter=12,
       textColor=colors.HexColor("#2E86C1"),
       alignment=1,
       fontName="Helvetica-Bold"
   )
   body_style = ParagraphStyle(
       name='BodyStyle',
       fontSize=12, 
       leading=14,
       fontName="Helvetica",
       textColor=colors.black,
       spaceAfter=12,

   )

   html_paragraph = markdown(text)
   elements.append(Paragraph(html_paragraph, body_style))

   clean_text = clean_duplicate_lines(text)

   for para in clean_text.split("\n"):
    para = para.strip()
    if para:
        elements.append(Paragraph(para, body_style))

   doc.build(elements)

   buffer.seek(0)
   pdf_base64 = base64.b64encode(buffer.read()).decode('utf-8')
   return pdf_base64

def generate_fiche(titre,secteur,contrat, niveau, competences, source=""):
   result = llm_chain.run(
      titre=titre,
      secteur=secteur,
      contrat=contrat,
      niveau=niveau, 
      competences=competences
  )
   result = result.strip()
   result = clean_duplicate_lines(result)
   
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
   pdf_base64 = generate_pdf_from_text(result)
   fiche["fichierPDF"] = pdf_base64

   if not isinstance(result, str):
      raise ValueError("Le texte de la fiche de poste doit être une chaîne de caractères.")

   db = CosmosDBManager()
   try:
      db.add_job_description(job_info=fiche, job_description=result)
      print(f"Fiche de poste ajoutée avec succès, ID : {fiche_id}")
   except Exception as e:
    print(f"Erreur lors de l'ajout de la fiche de poste : {e}")
    raise
   
   return result, fiche_id

_all_ = ["generate_fiche"]

if __name__ == "__main__":
    titre = "Developpeur Frontend Web"
    secteur = "Technologie"
    contrat = "CDI"
    niveau = "5 ans d'expérience"
    competences = "JavaScript, React, CSS, HTML, API REST"
    

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



