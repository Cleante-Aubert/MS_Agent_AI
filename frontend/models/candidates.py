import streamlit as st
from typing import List, Dict, Optional, Any
import re

class CandidateModel:
    """
    Modèle pour gérer les candidats et leurs candidatures.
    """
    
    @staticmethod
    def get_all_candidates() -> List[Dict]:
        """Récupère tous les candidats."""
        if 'candidates' not in st.session_state:
            # Initialiser avec des données de démo
            from models.mock_data import CANDIDATES_DATA
            st.session_state.candidates = CANDIDATES_DATA
            
        return st.session_state.candidates
    
    @staticmethod
    def get_candidate_by_id(candidate_id: int) -> Optional[Dict]:
        """Récupère un candidat par son ID."""
        candidates = CandidateModel.get_all_candidates()
        for candidate in candidates:
            if candidate['id'] == candidate_id:
                return candidate
        return None
    
    @staticmethod
    def add_candidate(candidate_data: Dict) -> Dict:
        """Ajoute un nouveau candidat."""
        candidates = CandidateModel.get_all_candidates()
        
        # Attribuer un nouvel ID
        if candidates:
            new_id = max(candidate['id'] for candidate in candidates) + 1
        else:
            new_id = 1
            
        candidate_data['id'] = new_id
        
        # Ajouter à la liste
        candidates.append(candidate_data)
        st.session_state.candidates = candidates
        
        return candidate_data
    
    @staticmethod
    def update_candidate(candidate_id: int, candidate_data: Dict) -> Optional[Dict]:
        """Met à jour un candidat existant."""
        candidates = CandidateModel.get_all_candidates()
        
        for i, candidate in enumerate(candidates):
            if candidate['id'] == candidate_id:
                # Préserver l'ID
                candidate_data['id'] = candidate_id
                # Mettre à jour
                candidates[i] = candidate_data
                st.session_state.candidates = candidates
                return candidate_data
                
        return None
    
    @staticmethod
    def delete_candidate(candidate_id: int) -> bool:
        """Supprime un candidat."""
        candidates = CandidateModel.get_all_candidates()
        
        for i, candidate in enumerate(candidates):
            if candidate['id'] == candidate_id:
                # Supprimer
                del candidates[i]
                st.session_state.candidates = candidates
                return True
                
        return False
    
    # Gestion des candidatures
    
    @staticmethod
    def get_all_applications() -> List[Dict]:
        """Récupère toutes les candidatures."""
        if 'applications' not in st.session_state:
            # Initialiser avec des données de démo
            from models.mock_data import APPLICATIONS_DATA
            st.session_state.applications = APPLICATIONS_DATA
            
        return st.session_state.applications
    
    @staticmethod
    def get_application_by_id(application_id: int) -> Optional[Dict]:
        """Récupère une candidature par son ID."""
        applications = CandidateModel.get_all_applications()
        for application in applications:
            if application['id'] == application_id:
                return application
        return None
    
    @staticmethod
    def get_applications_by_job(job_id: int) -> List[Dict]:
        """Récupère toutes les candidatures pour un poste spécifique."""
        applications = CandidateModel.get_all_applications()
        return [app for app in applications if app['job_id'] == job_id]
    
    @staticmethod
    def get_applications_by_candidate(candidate_id: int) -> List[Dict]:
        """Récupère toutes les candidatures d'un candidat spécifique."""
        applications = CandidateModel.get_all_applications()
        return [app for app in applications if app['candidate_id'] == candidate_id]
    
    @staticmethod
    def add_application(application_data: Dict) -> Dict:
        """Ajoute une nouvelle candidature."""
        applications = CandidateModel.get_all_applications()
        
        # Attribuer un nouvel ID
        if applications:
            new_id = max(app['id'] for app in applications) + 1
        else:
            new_id = 1
            
        application_data['id'] = new_id
        
        # Ajouter le statut initial
        if 'statut' not in application_data:
            application_data['statut'] = "Soumise"
        
        # Ajouter à la liste
        applications.append(application_data)
        st.session_state.applications = applications
        
        return application_data
    
    @staticmethod
    def update_application_status(application_id: int, new_status: str) -> Optional[Dict]:
        """Met à jour le statut d'une candidature."""
        applications = CandidateModel.get_all_applications()
        
        for i, application in enumerate(applications):
            if application['id'] == application_id:
                application['statut'] = new_status
                st.session_state.applications = applications
                return application
                
        return None