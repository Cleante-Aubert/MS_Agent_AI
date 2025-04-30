import streamlit as st
from streamlit_option_menu import option_menu


from models.jobs import JobModel
from models.candidates import CandidateModel
from views.components import (
    render_job_card, 
    render_candidate_card, 
    render_dashboard_stats,
    render_top_bar,
    render_gen_post_button
)

class AdminViews:
    """
    Classe regroupant les vues pour l'interface recruteur en dark mode.
    """
    
    @staticmethod
    def render_navigation() -> str:
        """Affiche le menu de navigation horizontal en dark mode."""
        # Afficher la barre supérieure
        render_top_bar()
        
        selected = option_menu(
            menu_title=None,
            options=["Accueil", "Fiches de Postes", "Candidats Idéaux"],
            icons=["house", "file-text", "people"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#1E1E1E"},
                "icon": {"color": "#00A8A8", "font-size": "1rem"},
                "nav-link": {"font-size": "1rem", "text-align": "center", "margin":"0px", "--hover-color": "#2A2A2A"},
                "nav-link-selected": {"background-color": "#00A8A8", "color": "white"},
            }
        )
        
        return selected
    
    @staticmethod
    def render_home_page():
        """Affiche la page d'accueil en dark mode."""
        st.markdown('<h1 class="main-header">Bienvenue sur votre Plateforme de Recrutement</h1>', unsafe_allow_html=True)
        
        # Deux boutons pour la génération de poste - un en haut à droite et un autre en bas
        col1, col2 = st.columns([3, 1])
        with col2:
            if render_gen_post_button("gen_post_btn_top"):
                st.session_state.show_chatbot_page = True
                st.experimental_rerun()
        
        st.markdown("""
        <div style="margin-bottom: 30px;">
        Cette plateforme vous aide à gérer votre processus de recrutement :
        
        - **Fiches de Postes** : Consultez et gérez vos descriptions de postes
        - **Candidats Idéaux** : Visualisez les profils des candidats potentiels
        - **Génération de Poste** : Utilisez notre outil IA pour créer rapidement des fiches de postes
        </div>
        """, unsafe_allow_html=True)
        
        # Afficher le tableau de bord
        st.markdown('<h2 class="subheader">Tableau de bord</h2>', unsafe_allow_html=True)
        render_dashboard_stats()
        
        # Second bouton de génération en bas
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if render_gen_post_button("gen_post_btn_bottom"):
                st.session_state.show_chatbot_page = True
                st.experimental_rerun()
    
    @staticmethod
    def render_jobs_page():
        """Affiche la page des fiches de poste en dark mode."""
        st.markdown('<h1 class="main-header">Fiches de Postes</h1>', unsafe_allow_html=True)
        
        # Bouton pour ajouter un nouveau poste
        col1, col2 = st.columns([3, 1])
        with col2:
            st.markdown(
                '<div class="gen-post-btn" onclick="document.querySelector(\'button[data-testid=\\\'new_job_btn\\\']\').click()">+ Nouveau Poste</div>',
                unsafe_allow_html=True
            )
            button_new = st.button("+ Nouveau Poste", key="new_job_btn")
            if button_new:
                st.session_state.show_chatbot_page = True
                st.experimental_rerun()
        
        # Recherche avec style dark mode
        st.text_input("Rechercher une fiche de poste", placeholder="Entrez un mot-clé...")
        
        # Afficher les offres
        all_jobs = JobModel.get_all_jobs()
        jobs = [job for job in all_jobs if job.get("metadata", {}).get("source") == "générée_par_HiRo"]

        if jobs:
            for job in jobs:
                render_job_card(job, admin_mode=True)
                
                # Boutons d'action
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✏️ Modifier", key=f"edit_{job['id']}"):
                        st.session_state.edit_job = job
                        st.experimental_rerun()
                with col2:
                    if st.button("👁️ Voir candidatures", key=f"view_apps_{job['id']}"):
                        st.session_state.view_job_applications = job
                        st.experimental_rerun()
        else:
            st.markdown('<div style="text-align: center; margin: 50px 0;">Aucune fiche de poste disponible</div>', unsafe_allow_html=True)
    
    @staticmethod
    def render_candidates_page():
        """Affiche la page des candidats en dark mode."""
        st.markdown('<h1 class="main-header">Candidats Idéaux</h1>', unsafe_allow_html=True)
        
        # Filtres adaptés au dark mode
        col1, col2 = st.columns(2)
        with col1:
            filtre_poste = st.selectbox("Filtre par poste", ["Tous", "Développeur Full Stack", "Chef de Projet Marketing", "Data Scientist", "Ingénieur DevOps"])
        with col2:
            filtre_exp = st.slider("Expérience minimum (années)", 0, 10, 0)
        
        # Récupérer les candidats
        candidates = CandidateModel.get_all_candidates()
        
        # Filtrer les candidats selon les critères
        filtered_candidates = candidates
        if filtre_poste != "Tous":
            filtered_candidates = [c for c in filtered_candidates if c.get("poste") == filtre_poste]
        if filtre_exp > 0:
            filtered_candidates = [c for c in filtered_candidates if int(c.get("experience", "0").split()[0]) >= filtre_exp]
        
        # Afficher les candidats
        if filtered_candidates:
            cols = st.columns(3)
            for i, candidate in enumerate(filtered_candidates):
                with cols[i % 3]:
                    render_candidate_card(candidate)
                    
                    # Bouton pour voir le profil détaillé
                    if st.button("Voir profil détaillé", key=f"view_profile_{candidate['id']}"):
                        st.session_state.view_candidate = candidate
                        st.experimental_rerun()
        else:
            st.markdown('<div style="text-align: center; margin: 50px 0;">Aucun candidat ne correspond à vos critères</div>', unsafe_allow_html=True)

