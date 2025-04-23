import streamlit as st
from streamlit_option_menu import option_menu
import time

# Configuration de la page
st.set_page_config(
    page_title="Espace Candidat - Plateforme de Recrutement",
    page_icon="👤",
    layout="wide"
)

# CSS pour personnaliser l'interface
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 1rem;
        text-align: center;
    }
    .job-card {
        background-color: #EFF6FF;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        cursor: pointer;
    }
    .job-card:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    .stButton button {
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
    }
    div[data-testid="stSidebarNav"] {
        background-color: #F3F4F6;
        padding-top: 2rem;
    }
    .application-form {
        background-color: #F9FAFB;
        border-radius: 10px;
        padding: 20px;
        margin-top: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .section-header {
        color: #1E3A8A;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .success-message {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialiser les variables de session
if "selected_job" not in st.session_state:
    st.session_state.selected_job = None

if "application_submitted" not in st.session_state:
    st.session_state.application_submitted = False

# Exemple de fiches de postes
fiches_postes = [
    {
        "id": 1,
        "titre": "Développeur Full Stack",
        "departement": "Technologie",
        "type": "CDI",
        "localisation": "Paris",
        "description": """Nous recherchons un développeur full stack expérimenté pour rejoindre notre équipe et travailler sur nos applications web et mobiles.
        
**Missions principales:**
- Développer des fonctionnalités front-end et back-end
- Participer à la conception technique des projets
- Assurer la maintenance et l'amélioration continue des applications
- Collaborer avec les designers et les product managers

**Compétences requises:**
- JavaScript, React, Node.js
- HTML/CSS, responsive design
- SQL et NoSQL databases
- Git, CI/CD
""",
        "salaire": "45 000€ - 55 000€ selon expérience",
        "date_publication": "12/04/2025"
    },
    {
        "id": 2,
        "titre": "Chef de Projet Marketing",
        "departement": "Marketing",
        "type": "CDI",
        "localisation": "Lyon",
        "description": """Responsable de la planification, du développement et de l'exécution des campagnes marketing pour nos produits et services.
        
**Missions principales:**
- Élaborer et mettre en œuvre des stratégies marketing
- Gérer les budgets des campagnes et analyser leur ROI
- Coordonner les différentes équipes impliquées
- Suivre les KPIs et optimiser les performances

**Compétences requises:**
- Expérience en marketing digital
- Maîtrise des outils d'analyse marketing
- Excellentes capacités de communication
- Sens de l'organisation et gestion de projet
""",
        "salaire": "50 000€ - 60 000€ selon expérience",
        "date_publication": "15/04/2025"
    },
    {
        "id": 3,
        "titre": "Data Scientist",
        "departement": "Data & Analytics",
        "type": "CDI",
        "localisation": "Toulouse",
        "description": """Analyser de grands ensembles de données et créer des modèles prédictifs pour aider à la prise de décision commerciale.
        
**Missions principales:**
- Collecter, traiter et analyser des données complexes
- Développer des modèles d'apprentissage automatique
- Présenter les résultats d'analyse aux parties prenantes
- Collaborer avec les équipes produit et technique

**Compétences requises:**
- Python, R, SQL
- Machine Learning et statistiques
- Data visualization (Tableau, PowerBI)
- Bonnes compétences en communication
""",
        "salaire": "55 000€ - 65 000€ selon expérience",
        "date_publication": "10/04/2025"
    },
    {
        "id": 4,
        "titre": "Ingénieur DevOps",
        "departement": "Infrastructure",
        "type": "CDI",
        "localisation": "Bordeaux",
        "description": """Responsable de l'infrastructure cloud, de l'automatisation du déploiement et de la mise en place des pipelines CI/CD.
        
**Missions principales:**
- Concevoir et maintenir notre infrastructure cloud
- Automatiser les processus de déploiement
- Optimiser les performances et la sécurité
- Implémenter les meilleures pratiques DevOps

**Compétences requises:**
- AWS, Azure ou GCP
- Docker, Kubernetes
- Terraform, Ansible
- Linux, scripting (Python, Bash)
""",
        "salaire": "48 000€ - 58 000€ selon expérience",
        "date_publication": "18/04/2025"
    }
]

# Créer le menu de navigation horizontal
selected = option_menu(
    menu_title=None,
    options=["Accueil", "Offres d'emploi"],
    icons=["house", "briefcase"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Page d'accueil
if selected == "Accueil":
    st.markdown('<h1 class="main-header">Bienvenue sur notre Plateforme de Recrutement</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    Nous sommes ravis de vous accueillir dans notre espace candidat. Ici, vous pouvez:
    
    - Découvrir toutes nos **offres d'emploi** disponibles
    - **Postuler en ligne** facilement en quelques clics
    - **Suivre l'état** de vos candidatures
    
    Nous recherchons des talents comme vous pour rejoindre nos équipes!
    """)
    
    # Afficher quelques statistiques et postes mis en avant
    st.subheader("Postes récemment publiés")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="job-card">
            <h3>{fiches_postes[0]["titre"]}</h3>
            <p><strong>Département:</strong> {fiches_postes[0]["departement"]}</p>
            <p><strong>Localisation:</strong> {fiches_postes[0]["localisation"]}</p>
            <p><strong>Type de contrat:</strong> {fiches_postes[0]["type"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="job-card">
            <h3>{fiches_postes[1]["titre"]}</h3>
            <p><strong>Département:</strong> {fiches_postes[1]["departement"]}</p>
            <p><strong>Localisation:</strong> {fiches_postes[1]["localisation"]}</p>
            <p><strong>Type de contrat:</strong> {fiches_postes[1]["type"]}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Bouton pour aller aux offres d'emploi
    if st.button("Voir toutes les offres d'emploi"):
        st.session_state.selected_job = None
        st.session_state.application_submitted = False
        st.experimental_rerun()

# Page des offres d'emploi
elif selected == "Offres d'emploi":
    st.markdown('<h1 class="main-header">Nos offres d\'emploi</h1>', unsafe_allow_html=True)
    
    # Reset le formulaire de candidature si nécessaire
    if st.session_state.application_submitted:
        st.session_state.selected_job = None
        st.session_state.application_submitted = False
    
    # Si aucun poste n'est sélectionné, afficher la liste des postes
    if st.session_state.selected_job is None:
        # Ajouter des filtres
        col1, col2, col3 = st.columns(3)
        with col1:
            filtre_departement = st.selectbox("Département", ["Tous"] + list(set([job["departement"] for job in fiches_postes])))
        with col2:
            filtre_type = st.selectbox("Type de contrat", ["Tous"] + list(set([job["type"] for job in fiches_postes])))
        with col3:
            filtre_localisation = st.selectbox("Localisation", ["Toutes"] + list(set([job["localisation"] for job in fiches_postes])))
        
        # Recherche par mot-clé
        search = st.text_input("Rechercher par mot-clé")
        
        # Filtrer les fiches de postes
        filtered_jobs = fiches_postes
        if filtre_departement != "Tous":
            filtered_jobs = [job for job in filtered_jobs if job["departement"] == filtre_departement]
        if filtre_type != "Tous":
            filtered_jobs = [job for job in filtered_jobs if job["type"] == filtre_type]
        if filtre_localisation != "Toutes":
            filtered_jobs = [job for job in filtered_jobs if job["localisation"] == filtre_localisation]
        if search:
            filtered_jobs = [job for job in filtered_jobs if search.lower() in job["titre"].lower() or search.lower() in job["description"].lower()]
        
        # Afficher les fiches de postes
        if not filtered_jobs:
            st.info("Aucune offre d'emploi ne correspond à vos critères.")
        else:
            for job in filtered_jobs:
                job_card = f"""
                <div class="job-card" id="job-{job['id']}">
                    <h3>{job["titre"]}</h3>
                    <p><strong>Département:</strong> {job["departement"]}</p>
                    <p><strong>Localisation:</strong> {job["localisation"]}</p>
                    <p><strong>Type de contrat:</strong> {job["type"]}</p>
                    <p><strong>Date de publication:</strong> {job["date_publication"]}</p>
                </div>
                """
                st.markdown(job_card, unsafe_allow_html=True)
                
                # Bouton pour voir les détails et postuler
                if st.button(f"Voir détails et postuler", key=f"view_{job['id']}"):
                    st.session_state.selected_job = job
                    st.experimental_rerun()
    
    # Si un poste est sélectionné, afficher ses détails et le formulaire de candidature
    else:
        job = st.session_state.selected_job
        
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
        st.markdown('<h2 class="section-header">Formulaire de candidature</h2>', unsafe_allow_html=True)
        
        # Utiliser avec st.form pour créer un formulaire propre
        with st.form(key="candidature_form"):
            st.markdown('<div class="application-form">', unsafe_allow_html=True)
            
            # Informations personnelles
            st.subheader("Informations personnelles")
            col1, col2 = st.columns(2)
            with col1:
                # Correction: ne pas utiliser l'attribut required=True qui cause l'erreur
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
            
            # Correction: Utiliser st.form_submit_button correctement
            submit_button = st.form_submit_button(label="Envoyer ma candidature")
            
        # Traiter la soumission du formulaire en dehors du contexte du formulaire
        if submit_button:
            # Vérifier que les champs obligatoires sont remplis
            if prenom and nom and email and telephone and cv and rgpd:
                # Simuler l'envoi de la candidature
                with st.spinner("Envoi de votre candidature en cours..."):
                    time.sleep(2)  # Simuler un temps de traitement
                
                st.session_state.application_submitted = True
                st.success("Votre candidature a été envoyée avec succès! Nous vous contacterons prochainement.")
                
                # Redirection vers la liste des offres après 3 secondes
                time.sleep(3)
                st.experimental_rerun()
            else:
                st.error("Veuillez remplir tous les champs obligatoires marqués d'un astérisque (*).")
        else:
            st.error("")