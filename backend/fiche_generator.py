import getpass
import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("AZURE_OPENAI_API_KEY"):
  os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass("Enter API key for Azure: ")

client = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)

# TODO : Charger le prompt depuis le fichier génération_fiche.txt
def load_prompt_from_env_hiro(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

template = load_prompt_from_env_hiro("../config/prompts/prompt_env_hiro.txt")


prompt = PromptTemplate(input_variables=["titre", "secteur", "contrat", "niveau", "competences"], template=template)
llm_chain = LLMChain(llm=client, prompt=prompt)

def generate_fiche(titre,secteur,contrat, niveau, competences):
   result = llm_chain.run(titre=titre, secteur=secteur, contrat=contrat, niveau=niveau, competences=competences)
   return result


if __name__ == "__main__":

    titre = "Développeur Backend"
    secteur = "Technologie"
    contrat = "CDI"
    niveau = "5 ans d'expérience"
    competences = "Python, Django, SQL, API REST"

    # Générer la fiche de poste
    fiche_poste = generate_fiche(titre, secteur, contrat, niveau, competences)

    # Afficher la fiche de poste générée
    print("Fiche de Poste générée :\n")
    print(fiche_poste)

_all_ = ["generate_fiche"]



