import streamlit as st
from frontend.utils.api_client import ApiClient
from frontend.utils.validators import validate_candidate_form
from frontend.models.application_model import Application
import tempfile
import os

class CandidateController:
    """Contrôleur pour gérer les candidats et leurs candidatures."""
    
    @staticmethod
    def apply_for_job(job_id, candidate_data, cv_file):
        """Soumet une candidature pour une offre d'emploi."""
        # Validation des données
        is_valid, error_msg = validate_candidate_form(candidate_data, cv_file)
        if not is_valid:
            return False, error_msg
        
        # Sauvegarder temporairement le fichier CV
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(cv_file.name)[1]) as tmp:
            tmp.write(cv_file.getvalue())
            tmp_path = tmp.name
        
        try:
            # Préparation des données pour l'API
            candidate_info = {
                "nom": candidate_data["nom"],
                "prenom": candidate_data["prenom"],
                "email": candidate_data["email"],
                "competences": candidate_data["competences"],
                "source": "Portail Candidat",
                "uploadDate": candidate_data.get("uploadDate", "")
            }
            
            # Appel à l'API
            response = ApiClient.add_cv(tmp_path, candidate_info)
            
            if "error" in response:
                return False, response["error"]
            
            return True, "Candidature soumise avec succès."
        
        finally:
            # Nettoyer le fichier temporaire
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @staticmethod
    def get_candidate_applications(candidate_email):
        """Récupère les candidatures d'un candidat."""
        # Cette fonctionnalité nécessiterait un endpoint API supplémentaire
        # Pour l'instant, cette méthode retourne des données fictives
        
        applications = [
            Application(
                candidate_id=candidate_email,
                job_id="job_123",
                status="pending",
                match_score=None
            ),
            Application(
                candidate_id=candidate_email,
                job_id="job_456",
                status="reviewed",
                match_score=85
            )
        ]
        
        return True, f"{len(applications)} candidatures trouvées.", applications