
import streamlit as st
from utils.session_manager import set_page, is_logged_in, get_user_type, logout_user
from typing import Dict, List, Callable, Any

def render_top_bar():
    """Affiche la barre de navigation supérieure."""
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        st.image("https://i.ibb.co/f4Kq0hP/logo-hiro.png", width=100)  # Placeholder pour un logo
    
    with col2:
        st.markdown("""
        <h1 style='text-align: center; color: #2E86C1;'>HiRo - Assistant RH Intelligent</h1>
        """, unsafe_allow_html=True)
    
    with col3:
        if is_logged_in():
            if st.button("📤 Déconnexion"):
                logout_user()
                st.rerun()

def render_job_card(job: Dict, show_button: bool = True, admin_mode: bool = False):
    """
    Affiche une carte pour une offre d'emploi en dark mode.
    """
    job_card = f"""
    <div class="job-card">
        <h3>{job["titre"]}</h3>
        <p>
            <strong>Département:</strong> {job["departement"]} &nbsp;|&nbsp;
            <strong>Type:</strong> {job["type"]} &nbsp;|&nbsp;
            <strong>Localisation:</strong> {job["localisation"]}
        </p>
    """
    
    if admin_mode:
        job_card += f"<p><strong>Publication:</strong> {job['date_publication']} &nbsp;|&nbsp; <strong>Salaire:</strong> {job['salaire']}</p>"
    
    if not show_button and not admin_mode:
        description = job["description"]
        if len(description) > 150:
            description = description[:150] + "..."
        job_card += f"<p>{description}</p>"
        
    job_card += "</div>"
    
    st.markdown(job_card, unsafe_allow_html=True)

def render_candidate_card(candidate: Dict):
    """
    Affiche une carte pour un candidat en dark mode.
    """
    candidate_card = f"""
    <div class="candidate-card">
        <h3>{candidate['prenom']} {candidate['nom']}</h3>
        <p><strong>Poste ciblé:</strong> {candidate.get('poste', 'Non spécifié')}</p>
        <p><strong>Expérience:</strong> {candidate.get('experience', 'Non spécifiée')}</p>
        <p><strong>Compétences:</strong> {', '.join(candidate.get('competences', ['Non spécifiées']))}</p>
        <p><strong>Matching:</strong> <span style="color: #00A8A8; font-weight: bold;">{candidate.get('matching', 'Non évalué')}</span></p>
    </div>
    """
    
    st.markdown(candidate_card, unsafe_allow_html=True)

def render_dashboard_stats():
    """
    Affiche les statistiques du tableau de bord en dark mode.
    """
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Postes Ouverts</div>
            <div class="stat-value">12</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Candidatures Reçues</div>
            <div class="stat-value">87</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Entretiens Planifiés</div>
            <div class="stat-value">9</div>
        </div>
        """, unsafe_allow_html=True)

def render_gen_post_button(key="gen_post_btn"):
    """
    Affiche un bouton stylisé pour la génération de poste.
    """
    st.markdown(
        f'<div class="gen-post-btn" onclick="document.querySelector(\'button[data-testid=\\\'{key}\\\']\').click()">Génération de Poste</div>',
        unsafe_allow_html=True
    )
    
    # Bouton caché qui sera cliqué via JavaScript
    return st.button("Génération de Poste", key=key)

def render_success_message(message: str):
    """
    Affiche un message de succès en dark mode.
    """
    st.markdown(f'<div class="success-message">{message}</div>', unsafe_allow_html=True)

def render_error_message(message: str):
    """
    Affiche un message d'erreur en dark mode.
    """
    st.markdown(f'<div class="error-message">{message}</div>', unsafe_allow_html=True)

def render_info_message(message: str):
    """
    Affiche un message d'information stylisé pour dark mode.
    """
    st.info(message)