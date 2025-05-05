from frontend.utils.api_client import ApiClient
from frontend.models.job_model import JobPosting
from frontend.utils.validators import validate_job_form

class JobController:
    """Contrôleur pour gérer les fiches de poste."""
    
    @staticmethod
    def generate_job_posting(job_data):
        """Génère une nouvelle fiche de poste."""
        # Validation des données
        is_valid, error_msg = validate_job_form(job_data)
        if not is_valid:
            return False, error_msg, None
        
        # Appel à l'API
        response = ApiClient.generate_job_posting(job_data)
        
        if "error" in response:
            return False, response["error"], None
        
        # Créer un objet JobPosting
        job = {
            "fiche": response.get("fiche", ""),
            "fichierPDF": response.get("fichierPDF", None),
            "id": response.get("id", "")
        }
        
        return True, "Fiche de poste générée avec succès.", job
    
    @staticmethod
    def get_all_job_postings():
        """Récupère toutes les fiches de poste."""
        # Appel à l'API
        response = ApiClient.get_job_postings()
        
        if "error" in response:
            return False, response["error"], []
        
        # Convertir les réponses en objets JobPosting
        job_postings = []
        for job_data in response:
            job = JobPosting.from_api_response(job_data)
            job_postings.append(job)
        
        return True, f"{len(job_postings)} fiches de poste trouvées.", job_postings