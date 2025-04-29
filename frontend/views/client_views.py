import streamlit as st
from streamlit_option_menu import option_menu
from typing import Dict, List, Callable, Any
import time

from models.jobs import JobModel
from views.components import render_job_card, render_success_message, render_error_message

class ClientViews:
    """
    Classe regroupant toutes les vues pour l'interface candidat.
    """
    
    @staticmethod
    def render_navigation() -> str:
        """Affiche le menu de navigation horizontal et retourne la page sélectionnée."""
        selected = option_menu(
            menu_title=None,
            options=["Accueil", "Offres d'emploi"],
            icons=["house", "briefcase"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )
        return selected
    
    @staticmethod
    def render_home_page():
        """Affiche la page d'accueil de l'espace candidat."""
        st.markdown('<h1 class="main-header">Bienvenue sur notre Plateforme de Recrutement</h1>', unsafe_allow_html=True)
        
        st.markdown("""
        Nous sommes ravis de vous accueillir dans notre espace candidat. Ici, vous pouvez :
        
        - Découvrir toutes nos **offres d'emploi** disponibles
        - **Postuler en ligne** facilement en quelques clics
        - **Suivre l'état** de vos candidatures
        
        Nous recherchons des talents comme vous pour rejoindre nos équipes !
        """)
        
        # Afficher quelques postes récents
        st.subheader("Postes récemment publiés")
        
        # Récupérer les données des offres d'emploi
        jobs = JobModel.get_all_jobs()
        if len(jobs) >= 2:
            col1, col2 = st.columns(2)
            
            with col1:
                render_job_card(jobs[0], show_button=False)
                
            with col2:
                render_job_card(jobs[1], show_button=False)
        
        # Bouton pour aller aux offres d'emploi
        if st.button("Voir toutes les offres d'emploi"):
            st.session_state.client_page = "Offres d'emploi"
            st.experimental_rerun()
    
    @staticmethod
    def render_jobs_list_page():
        """Affiche la page de liste des offres d'emploi."""
        st.markdown('<h1 class="main-header">Nos offres d\'emploi</h1>', unsafe_allow_html=True)
        
        # Si aucun poste n'est sélectionné, afficher la liste des postes
        if "selected_job" not in st.session_state or st.session_state.selected_job is None:
            # Filtres
            col1, col2, col3 = st.columns(3)
            
            with col1:
                departments = ["Tous"] + JobModel.get_departments()
                filtre_departement = st.selectbox("Département", departments)
            
            with col2:
                contract_types = ["Tous"] + JobModel.get_contract_types()
                filtre_type = st.selectbox("Type de contrat", contract_types)
            
            with col3:
                locations = ["Toutes"] + JobModel.get_locations()
                filtre_localisation = st.selectbox("Localisation", locations)
            
            # Recherche par mot-clé
            search = st.text_input("Rechercher par mot-clé")
            
            # Filtrer les offres
            filtered_jobs = JobModel.filter_jobs(
                departement=filtre_departement,
                type_contrat=filtre_type,
                localisation=filtre_localisation,
                keyword=search
            )
            
            # Afficher les offres filtrées
            if not filtered_jobs:
                st.info("Aucune offre d'emploi ne correspond à vos critères.")
            else:
                for job in filtered_jobs:
                    render_job_card(job)
                    
                    # Bouton pour voir les détails et postuler
                    if st.button(f"Voir détails et postuler", key=f"view_{job['id']}"):
                        st.session_state.selected_job = job
                        st.experimental_rerun()
        else:
            # Afficher les détails d'une offre et le formulaire de candidature
            ClientViews.render_job_details_page(st.session_state.selected_job)
    
    @staticmethod
    def render_job_details_page(job: Dict):
        """Affiche la page de détails d'une offre d'emploi et le formulaire de candidature."""
        # Bouton pour revenir à la liste
        if st.button("← Retour à la liste des offres"):
            st.session_state.selected_job = None
            st.experimental_rerun()
        
        # Afficher les détails du poste
        st.subheader(job["titre"])
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Département:** {job['departement']}")
            st.write(f"**Type de contrat:** {job['type']}")
        with col2:
            st.write(f"**Localisation:** {job['localisation']}")
            st.write(f"**Date de publication:** {job['date_publication']}")
        
        st.write(f"**Salaire:** {job['salaire']}")
        st.markdown(job["description"])
        
        # Formulaire de candidature
        ClientViews.render_application_form(job)
    
    @staticmethod
    def render_application_form(job: Dict):
        """Affiche le formulaire de candidature."""
        st.markdown('<h2 class="section-header">Formulaire de candidature</h2>', unsafe_allow_html=True)
        
        # Utiliser avec st.form pour créer un formulaire propre
        with st.form(key="candidature_form"):
            st.markdown('<div class="application-form">', unsafe_allow_html=True)
            
            # Informations personnelles
            st.subheader("Informations personnelles")
            col1, col2 = st.columns(2)
            with col1:
                prenom = st.text_input("Prénom *")
                email = st.text_input("Email *")
                telephone = st.text_input("Téléphone *")
            with col2:
                nom = st.text_input("Nom *")
                adresse = st.text_input("Adresse")
                ville = st.text_input("Ville")
            
            # Formation et expérience
            st.subheader("Formation et expérience")
            formation = st.text_area("Formation", height=100)
            experience = st.text_area("Expérience professionnelle", height=150)
            
            # Compétences
            st.subheader("Compétences")
            competences = st.text_area("Listez vos principales compétences", height=100)
            
            # Informations complémentaires
            st.subheader("Informations complémentaires")
            col1, col2 = st.columns(2)
            with col1:
                disponibilite = st.date_input("Disponibilité")
                pretentions = st.text_input("Prétentions salariales")
            with col2:
                mobilite = st.selectbox("Mobilité", ["Pas de mobilité", "Région", "France", "International"])
                teletravail = st.selectbox("Télétravail", ["Sur site uniquement", "Hybride", "Télétravail complet"])
            
            # CV et Lettre de motivation
            st.subheader("Documents")
            cv = st.file_uploader("CV (PDF, DOC, DOCX) *", type=["pdf", "doc", "docx"])
            lettre = st.file_uploader("Lettre de motivation", type=["pdf", "doc", "docx"])
            
            # Message complémentaire
            message = st.text_area("Message complémentaire", height=100)
            
            # Consentement RGPD
            rgpd = st.checkbox("J'accepte que mes données soient traitées dans le cadre de ma candidature *")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Bouton de soumission
            submit_button = st.form_submit_button(label="Envoyer ma candidature")
            
        # Traiter la soumission du formulaire (en dehors du form pour éviter les problèmes)
        if submit_button:
            # Vérifier que les champs obligatoires sont remplis
            if prenom and nom and email and telephone and cv and rgpd:
                # Préparer les données du candidat
                candidate_data = {
                    "nom": nom,
                    "prenom": prenom,
                    "email": email,
                    "telephone": telephone,
                    "adresse": adresse,
                    "ville": ville,
                    "formation": formation,
                    "experience": experience,
                    "competences": [comp.strip() for comp in competences.split(',') if comp.strip()],
                    "disponibilite": disponibilite.strftime("%Y-%m-%d"),
                    "pretentions": pretentions,
                    "mobilite": mobilite,
                    "teletravail": teletravail,
                    # Dans une vraie application, il faudrait sauvegarder les fichiers
                    "cv_path": "temp/cv.pdf",  # Chemin fictif
                    "lettre_path": "temp/lettre.pdf" if lettre else None
                }
                
                # Simuler l'envoi de la candidature
                with st.spinner("Envoi de votre candidature en cours..."):
                    time.sleep(2)  # Simuler un temps de traitement
                
                # Dans une application réelle, vous stockeriez ces données
                # Si le candidat n'existe pas déjà, ajoutez-le
                # from models.candidates import CandidateModel
                # candidate = CandidateModel.add_candidate(candidate_data)
                
                # Ajouter la candidature
                # application_data = {
                #     "job_id": job["id"],
                #     "candidate_id": candidate["id"],
                #     "message": message
                # }
                # CandidateModel.add_application(application_data)
                
                # Afficher un message de succès
                render_success_message("Votre candidature a été envoyée avec succès! Nous vous contacterons prochainement.")
                
                # Redirection vers la liste des offres après 3 secondes
                time.sleep(3)
                st.session_state.selected_job = None
                st.experimental_rerun()
            else:
                # Afficher un message d'erreur
                render_error_message("Veuillez remplir tous les champs obligatoires marqués d'un astérisque (*).")
