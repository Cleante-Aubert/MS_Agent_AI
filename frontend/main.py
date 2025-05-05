import streamlit as st
import sys
import os

# Ajouter le répertoire courant au chemin Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from frontend.controllers.auth_controller import AdminController
from utils.styles import load_css

def main():
    """
    Point d'entrée principal de l'application en dark mode.
    """
    # Configuration de la page
    st.set_page_config(
        page_title="HiRo - Assistant RH",
        page_icon="👔",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Appliquer les styles CSS dark mode
    load_css()
    
    # Initialiser et exécuter le contrôleur admin
    admin_controller = AdminController()
    admin_controller.run()

if __name__ == "__main__":
    main()