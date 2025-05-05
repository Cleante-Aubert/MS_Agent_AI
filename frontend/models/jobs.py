class JobPosting:
    """Modèle représentant une fiche de poste."""
    
    def __init__(self, job_id, titre, secteur, contrat, niveau, competences, content, pdf_file=None):
        self.job_id = job_id
        self.titre = titre
        self.secteur = secteur
        self.contrat = contrat
        self.niveau = niveau
        self.competences = competences if isinstance(competences, list) else [c.strip() for c in competences.split(",")]
        self.content = content
        self.pdf_file = pdf_file
    
    @staticmethod
    def from_api_response(api_response):
        """Crée un objet JobPosting à partir de la réponse de l'API."""
        return JobPosting(
            job_id=api_response.get("id", ""),
            titre=api_response.get("titre", ""),
            secteur=api_response.get("secteur", ""),
            contrat=api_response.get("contrat", ""),
            niveau=api_response.get("niveau", ""),
            competences=api_response.get("competences", []),
            content=api_response.get("content", ""),
            pdf_file=api_response.get("fichierPDF", None)
        )
    
    def to_dict(self):
        """Convertit l'objet en dictionnaire pour l'API."""
        return {
            "titre": self.titre,
            "secteur": self.secteur,
            "contrat": self.contrat,
            "niveau": self.niveau,
            "competences": ",".join(self.competences) if isinstance(self.competences, list) else self.competences
        }
    
    def get_summary(self):
        """Retourne un résumé de la fiche de poste."""
        return f"{self.titre} ({self.contrat}) - {self.secteur}"
    
JobModel = JobPosting
