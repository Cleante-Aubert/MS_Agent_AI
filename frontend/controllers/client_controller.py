import streamlit as st
from views.client_views import ClientViews
from models.jobs import JobModel
from models.candidates import CandidateModel

class ClientController:
    """
    Contrôleur pour l'interface candidat.
    Gère la logique entre les modèles et les vues.
    """
    
    def __init__(self):
        """Initialise le contrôleur client."""
        self.views = ClientViews()
        
        # Initialiser l'état de la page si nécessaire
        if "client_page" not in st.session_state:
            st.session_state.client_page = "Accueil"
        
        if "selected_job" not in st.session_state:
            st.session_state.selected_job = None
    
    def run(self):
        """
        Exécute le contrôleur qui gère l'interface candidat.
        """
        # Afficher le menu de navigation
        selected_page = self.views.render_navigation()
        
        # Si la page a changé via le menu, mettre à jour l'état
        if selected_page != st.session_state.client_page:
            st.session_state.client_page = selected_page
            st.session_state.selected_job = None  # Réinitialiser la sélection de poste
        
        # Afficher la page appropriée
        if st.session_state.client_page == "Accueil":
            self.render_home()
        elif st.session_state.client_page == "Offres d'emploi":
            self.render_jobs()
    
    def render_home(self):
        """Affiche la page d'accueil."""
        self.views.render_home_page()
    
    def render_jobs(self):
        """Affiche la page des offres d'emploi."""
        self.views.render_jobs_list_page()
    
    def handle_job_selection(self, job_id: int):
        """
        Gère la sélection d'une offre d'emploi.
        
        Args:
            job_id: ID de l'offre d'emploi
        """
        job = JobModel.get_job_by_id(job_id)
        if job:
            st.session_state.selected_job = job
            # Forcer un rechargement de la page
            st.experimental_rerun()
    
    def handle_job_application(self, job_id: int, candidate_data: dict, message: str = None):
        """
        Gère la soumission d'une candidature.
        
        Args:
            job_id: ID de l'offre d'emploi
            candidate_data: Données du candidat
            message: Message de candidature (optionnel)
            
        Returns:
            bool: True si la candidature a été soumise avec succès, False sinon
        """
        # Vérifier les champs obligatoires
        required_fields = ["nom", "prenom", "email", "telephone"]
        for field in required_fields:
            if field not in candidate_data or not candidate_data[field]:
                return False
        
        # Ajouter ou mettre à jour le candidat
        candidate = CandidateModel.add_candidate(candidate_data)
        
        # Créer la candidature
        application_data = {
            "job_id": job_id,
            "candidate_id": candidate["id"],
            "message": message
        }
        
        # Ajouter la candidature
        CandidateModel.add_application(application_data)
        
        # Réinitialiser la sélection de poste
        st.session_state.selected_job = None
        
        return True
