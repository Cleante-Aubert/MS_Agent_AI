class Application:
    """Modèle représentant une candidature."""
    
    def __init__(self, candidate_id, job_id, cv_path=None, status="pending", match_score=None):
        self.candidate_id = candidate_id
        self.job_id = job_id
        self.cv_path = cv_path
        self.status = status  # pending, reviewed, accepted, rejected
        self.match_score = match_score
    
    @staticmethod
    def from_api_response(api_response):
        """Crée un objet Application à partir de la réponse de l'API."""
        return Application(
            candidate_id=api_response.get("candidat_email", ""),
            job_id=api_response.get("job_id", ""),
            cv_path=api_response.get("cv_path", None),
            status=api_response.get("status", "pending"),
            match_score=api_response.get("match_score", None)
        )
    
    def to_dict(self):
        """Convertit l'objet en dictionnaire pour l'API."""
        return {
            "candidate_id": self.candidate_id,
            "job_id": self.job_id,
            "status": self.status
        }