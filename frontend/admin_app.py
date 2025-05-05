import streamlit as st
import sys
import os

# Ajouter le répertoire courant au chemin Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from frontend.controllers.auth_controller import AdminController
from utils.styles import load_css

def main():
    """
    Point d'entrée de l'application espace recruteur.
    """
    # Configuration de la page
    st.set_page_config(
        page_title="Espace Recruteur - Plateforme de Recrutement",
        page_icon="👔",
        layout="wide"
    )
    
    # Appliquer les styles CSS
    load_css()
    
    # Initialiser et exécuter le contrôleur admin
    controller = AdminController()
    controller.run()

if __name__ == "__main__":
    main()
