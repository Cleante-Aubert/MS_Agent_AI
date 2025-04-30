# Initialisation du package utils
# Permet d'importer directement depuis le package utils

from .styles import load_css
from .helpers import (
    format_date,
    extract_competences_from_description,
    calculate_matching_score,
    format_matching_score,
    validate_email,
    validate_phone
)

__all__ = [
    'load_css',
    'format_date',
    'extract_competences_from_description',
    'calculate_matching_score',
    'format_matching_score',
    'validate_email',
    'validate_phone'
]