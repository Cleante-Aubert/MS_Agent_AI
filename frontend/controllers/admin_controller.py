import streamlit as st
from views.admin_views import AdminViews
from views.chatbot_view import render_chatbot_page
from models.jobs import JobModel
from models.candidates import CandidateModel
from typing import Dict

class AdminController:
    """
    Contrôleur pour l'interface recruteur en dark mode.
    """
    
    def __init__(self):
        """Initialise le contrôleur admin."""
        self.views = AdminViews()
        
        # Initialiser les états
        if "admin_page" not in st.session_state:
            st.session_state.admin_page = "Accueil"
        
        if "show_chatbot_page" not in st.session_state:
            st.session_state.show_chatbot_page = False
        
        if "edit_job" not in st.session_state:
            st.session_state.edit_job = None
        
        if "view_job_applications" not in st.session_state:
            st.session_state.view_job_applications = None
        
        if "view_candidate" not in st.session_state:
            st.session_state.view_candidate = None
    
    def run(self):
        """
        Exécute le contrôleur qui gère l'interface recruteur.
        """
        # Si la page chatbot est demandée, l'afficher dans une nouvelle "page"
        if st.session_state.show_chatbot_page:
            render_chatbot_page()
            return
            
        # Afficher le menu de navigation
        selected_page = self.views.render_navigation()
        
        # Si la page a changé via le menu, mettre à jour l'état
        if selected_page != st.session_state.admin_page:
            st.session_state.admin_page = selected_page
            # Réinitialiser les autres états
            st.session_state.edit_job = None
            st.session_state.view_job_applications = None
            st.session_state.view_candidate = None
        
        # Afficher la page appropriée
        if st.session_state.admin_page == "Accueil":
            self.views.render_home_page()
        elif st.session_state.admin_page == "Fiches de Postes":
            self.views.render_jobs_page()
        elif st.session_state.admin_page == "Candidats Idéaux":
            self.views.render_candidates_page()
    
    def handle_job_edit(self, job_id: int, job_data: Dict) -> Dict:
        """
        Gère la modification d'une offre d'emploi.
        
        Args:
            job_id: ID de l'offre d'emploi
            job_data: Nouvelles données
            
        Returns:
            Dict: Offre d'emploi mise à jour
        """
        return JobModel.update_job(job_id, job_data)
    
    def handle_job_delete(self, job_id: int) -> bool:
        """
        Gère la suppression d'une offre d'emploi.
        
        Args:
            job_id: ID de l'offre d'emploi
            
        Returns:
            bool: True si suppression réussie
        """
        return JobModel.delete_job(job_id)
    
    def handle_candidate_view(self, candidate_id: int) -> Dict:
        """
        Gère l'affichage détaillé d'un candidat.
        
        Args:
            candidate_id: ID du candidat
            
        Returns:
            Dict: Données du candidat
        """
        return CandidateModel.get_candidate_by_id(candidate_id)