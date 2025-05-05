import streamlit as st

def initialize_session_state():
    """Initialise les variables de session nécessaires pour l'application."""
    if "user" not in st.session_state:
        st.session_state.user = None
    
    if "user_type" not in st.session_state:
        st.session_state.user_type = None  # "candidate" ou "recruiter"
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"
    
    if "selected_job" not in st.session_state:
        st.session_state.selected_job = None
    
    if "chatbot_messages" not in st.session_state:
        st.session_state.chatbot_messages = []
    
    if "fiche_inputs" not in st.session_state:
        st.session_state.fiche_inputs = {
            "titre": "",
            "secteur": "",
            "contrat": "",
            "niveau": "",
            "competences": ""
        }

def set_page(page_name):
    """Change la page actuelle."""
    st.session_state.current_page = page_name

def login_user(user_data, user_type):
    """Connecte un utilisateur et définit son type."""
    st.session_state.user = user_data
    st.session_state.user_type = user_type
    
    # Redirection selon le type d'utilisateur
    if user_type == "candidate":
        set_page("candidate_dashboard")
    elif user_type == "recruiter":
        set_page("recruiter_dashboard")

def logout_user():
    """Déconnecte l'utilisateur."""
    st.session_state.user = None
    st.session_state.user_type = None
    set_page("login")

def is_logged_in():
    """Vérifie si un utilisateur est connecté."""
    return st.session_state.user is not None

def get_user_type():
    """Récupère le type d'utilisateur connecté."""
    return st.session_state.user_type