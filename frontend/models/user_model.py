
class User:
    """Modèle représentant un utilisateur (candidat ou recruteur)."""
    
    def __init__(self, user_email, nom="", prenom="", user_type="candidate"):
        self.user_email = user_email
        self.nom = nom
        self.prenom = prenom
        self.user_type = user_type  # "candidate" ou "recruiter"
    
    @staticmethod
    def from_api_response(api_response):
        """Crée un objet User à partir de la réponse de l'API."""
        if not api_response or "user" not in api_response:
            return None
        
        user_data = api_response["user"]
        return User(
            user_email=user_data.get("userEmail", ""),
            nom=user_data.get("nom", ""),
            prenom=user_data.get("prenom", ""),
            user_type=user_data.get("userType", "candidate")
        )
    
    def get_full_name(self):
        """Retourne le nom complet de l'utilisateur."""
        if self.nom and self.prenom:
            return f"{self.prenom} {self.nom}"
        elif self.nom:
            return self.nom
        elif self.prenom:
            return self.prenom
        else:
            return self.user_email