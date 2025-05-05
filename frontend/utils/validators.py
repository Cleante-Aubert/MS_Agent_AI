import re

def validate_email(email):
    """Valide le format d'un email."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_password(password):
    """Valide la complexité d'un mot de passe."""
    # Au moins 6 caractères
    if len(password) < 6:
        return False
    return True

def validate_not_empty(text):
    """Vérifie qu'un champ n'est pas vide."""
    return bool(text and text.strip())

def validate_job_form(job_data):
    """Valide les données d'une fiche de poste."""
    required_fields = ['titre', 'secteur', 'contrat', 'niveau', 'competences']
    
    for field in required_fields:
        if not validate_not_empty(job_data.get(field, '')):
            return False, f"Le champ '{field}' est obligatoire."
    
    return True, ""

def validate_candidate_form(candidate_data, cv_file=None):
    """Valide les données d'un candidat."""
    required_fields = ['nom', 'prenom', 'email', 'competences']
    
    for field in required_fields:
        if not validate_not_empty(candidate_data.get(field, '')):
            return False, f"Le champ '{field}' est obligatoire."
    
    if not validate_email(candidate_data.get('email', '')):
        return False, "Format d'email invalide."
    
    if cv_file is not None and cv_file.name == '':
        return False, "Veuillez télécharger votre CV."
    
    return True, ""