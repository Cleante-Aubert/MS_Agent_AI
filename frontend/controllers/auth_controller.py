from frontend.utils.api_client import ApiClient
from frontend.utils.session_manager import login_user, logout_user
from frontend.models.user_model import User
from frontend.utils.validators import validate_email, validate_password

class AuthController:
    """Contrôleur pour gérer l'authentification."""
    
    @staticmethod
    def register(email, password, nom="", prenom="", user_type="candidate"):
        """Enregistre un nouvel utilisateur."""
        # Validation des données
        if not validate_email(email):
            return False, "Format d'email invalide."
        
        if not validate_password(password):
            return False, "Le mot de passe doit contenir au moins 6 caractères."
        
        # Appel à l'API
        response = ApiClient.register_user(email, password, nom, prenom)
        
        if "error" in response:
            return False, response["error"]
        
        return True, "Compte créé avec succès."
    
    @staticmethod
    def login(email, password, user_type="candidate"):
        """Authentifie un utilisateur existant."""
        # Validation des données
        if not validate_email(email):
            return False, "Format d'email invalide."
        
        # Appel à l'API
        response = ApiClient.login_user(email, password)
        
        if "error" in response:
            return False, response["error"]
        
        # Créer un objet User et le stocker dans la session
        user = User.from_api_response(response)
        if user:
            login_user(user, user_type)
            return True, "Connexion réussie."
        
        return False, "Erreur lors de la connexion."
    
    @staticmethod
    def logout():
        """Déconnecte l'utilisateur actuel."""
        logout_user()
        return True, "Déconnexion réussie."