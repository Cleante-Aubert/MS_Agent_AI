import streamlit as st
from typing import List, Dict, Optional

class JobModel:
    """
    Modèle pour gérer les offres d'emploi.
    """
    
    @staticmethod
    def get_all_jobs() -> List[Dict]:
        """Récupère toutes les offres d'emploi."""
        if 'jobs' not in st.session_state:
            # Initialiser avec des données de démo
            from models.mock_data import JOBS_DATA
            st.session_state.jobs = JOBS_DATA
            
        return st.session_state.jobs
    
    @staticmethod
    def get_job_by_id(job_id: int) -> Optional[Dict]:
        """Récupère une offre d'emploi par son ID."""
        jobs = JobModel.get_all_jobs()
        for job in jobs:
            if job['id'] == job_id:
                return job
        return None
    
    @staticmethod
    def filter_jobs(departement=None, type_contrat=None, localisation=None, keyword=None) -> List[Dict]:
        """Filtre les offres d'emploi selon les critères spécifiés."""
        jobs = JobModel.get_all_jobs()
        filtered_jobs = jobs
        
        if departement and departement != "Tous":
            filtered_jobs = [job for job in filtered_jobs if job["departement"] == departement]
        
        if type_contrat and type_contrat != "Tous":
            filtered_jobs = [job for job in filtered_jobs if job["type"] == type_contrat]
        
        if localisation and localisation != "Toutes":
            filtered_jobs = [job for job in filtered_jobs if job["localisation"] == localisation]
        
        if keyword:
            keyword = keyword.lower()
            filtered_jobs = [
                job for job in filtered_jobs 
                if keyword in job["titre"].lower() or keyword in job["description"].lower()
            ]
            
        return filtered_jobs
    
    @staticmethod
    def add_job(job_data: Dict) -> Dict:
        """Ajoute une nouvelle offre d'emploi."""
        jobs = JobModel.get_all_jobs()
        
        # Attribuer un nouvel ID
        if jobs:
            new_id = max(job['id'] for job in jobs) + 1
        else:
            new_id = 1
            
        job_data['id'] = new_id
        
        # Ajouter à la liste
        jobs.append(job_data)
        st.session_state.jobs = jobs
        
        return job_data
    
    @staticmethod
    def update_job(job_id: int, job_data: Dict) -> Optional[Dict]:
        """Met à jour une offre d'emploi existante."""
        jobs = JobModel.get_all_jobs()
        
        for i, job in enumerate(jobs):
            if job['id'] == job_id:
                # Préserver l'ID
                job_data['id'] = job_id
                # Mettre à jour
                jobs[i] = job_data
                st.session_state.jobs = jobs
                return job_data
                
        return None
    
    @staticmethod
    def delete_job(job_id: int) -> bool:
        """Supprime une offre d'emploi."""
        jobs = JobModel.get_all_jobs()
        
        for i, job in enumerate(jobs):
            if job['id'] == job_id:
                # Supprimer
                del jobs[i]
                st.session_state.jobs = jobs
                return True
                
        return False