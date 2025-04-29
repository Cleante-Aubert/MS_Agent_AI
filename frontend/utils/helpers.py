import re
from typing import List, Dict, Any, Optional
from datetime import datetime

def format_date(date_str: str, input_format: str = "%d/%m/%Y", output_format: str = "%d/%m/%Y") -> str:
    """
    Convertit une date d'un format à un autre.
    
    Args:
        date_str: Chaîne de date à formater
        input_format: Format d'entrée (défaut: "%d/%m/%Y")
        output_format: Format de sortie (défaut: "%d/%m/%Y")
        
    Returns:
        str: Date formatée ou chaîne vide si conversion impossible
    """
    try:
        date_obj = datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except (ValueError, TypeError):
        return ""

def extract_competences_from_description(description: str) -> List[str]:
    """
    Extrait les compétences à partir d'une description de poste.
    
    Args:
        description: Description du poste
        
    Returns:
        List[str]: Liste des compétences extraites
    """
    # Recherche une section "Compétences requises:" ou similaire
    patterns = [
        r"Compétences requises[:\s]*([\s\S]*?)(?:\n\n|\Z)",
        r"Compétences[:\s]*([\s\S]*?)(?:\n\n|\Z)",
        r"Profil recherché[:\s]*([\s\S]*?)(?:\n\n|\Z)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            competences_text = match.group(1)
            # Extraire les éléments de liste (avec tirets ou puces)
            items = re.findall(r"[-•*]\s*([^\n\r]+)", competences_text)
            if items:
                # Nettoyer les compétences extraites
                return [item.strip() for item in items if item.strip()]
    
    # Si aucune section spécifique n'est trouvée, chercher des mots-clés techniques
    tech_keywords = [
        "JavaScript", "Python", "Java", "C#", "C++", "PHP", "Ruby",
        "React", "Angular", "Vue", "Node.js", "Express", "Django", "Flask",
        "SQL", "NoSQL", "MongoDB", "PostgreSQL", "MySQL", "AWS", "Azure", "GCP",
        "Docker", "Kubernetes", "Git", "CI/CD", "HTML", "CSS", "Marketing", "SEO",
        "Communication", "Gestion de projet", "Excel", "Word", "PowerPoint", "Tableau"
    ]
    
    found_keywords = []
    for keyword in tech_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', description, re.IGNORECASE):
            found_keywords.append(keyword)
    
    return found_keywords

def calculate_matching_score(job_competences: List[str], candidate_competences: List[str]) -> float:
    """
    Calcule un score de correspondance entre les compétences d'un poste et celles d'un candidat.
    
    Args:
        job_competences: Liste des compétences requises pour le poste
        candidate_competences: Liste des compétences du candidat
        
    Returns:
        float: Score de correspondance entre 0 et 1
    """
    if not job_competences or not candidate_competences:
        return 0.0
    
    # Normaliser les compétences (minuscules)
    job_comp_norm = [comp.lower() for comp in job_competences]
    candidate_comp_norm = [comp.lower() for comp in candidate_competences]
    
    # Compter les correspondances
    matches = sum(1 for comp in candidate_comp_norm if any(job_comp in comp or comp in job_comp for job_comp in job_comp_norm))
    
    # Calculer le score (basé sur les compétences requises pour le poste)
    score = matches / len(job_competences) if len(job_competences) > 0 else 0
    
    return min(score, 1.0)  # Plafonner à 1.0 (100%)

def format_matching_score(score: float) -> str:
    """
    Formate un score de correspondance pour l'affichage.
    
    Args:
        score: Score entre 0 et 1
        
    Returns:
        str: Score formaté en pourcentage
    """
    return f"{int(score * 100)}%"

def validate_email(email: str) -> bool:
    """
    Valide une adresse email.
    
    Args:
        email: Adresse email à valider
        
    Returns:
        bool: True si l'email est valide, False sinon
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """
    Valide un numéro de téléphone.
    
    Args:
        phone: Numéro de téléphone à valider
        
    Returns:
        bool: True si le numéro est valide, False sinon
    """
    # Accepte des formats variés (0123456789, 01 23 45 67 89, +33 1 23 45 67 89)
    pattern = r'^(?:\+\d{2}\s?)?(?:0|\(\d{1,3}\))[\s.-]?\d{1,3}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}$'
    return bool(re.match(pattern, phone))
