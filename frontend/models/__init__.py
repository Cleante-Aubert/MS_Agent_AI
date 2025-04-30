# Initialisation du package models
# Permet d'importer directement depuis le package models

from .jobs import JobModel
from .candidates import CandidateModel

__all__ = ['JobModel', 'CandidateModel']
