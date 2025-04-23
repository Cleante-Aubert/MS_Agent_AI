import streamlit as st
from streamlit_option_menu import option_menu
import time

# Configuration de la page
st.set_page_config(
    page_title="Plateforme de Recrutement",
    page_icon="👔",
    layout="wide"
)

# Fonction pour créer un chat IA simulé
def chat_ia():
    st.header("Génération de Poste")
    
    # Initialiser l'historique de chat s'il n'existe pas
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Afficher les messages existants
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Zone de saisie
    prompt = st.chat_input("Comment puis-je vous aider à générer une fiche de poste?")
    
    # Gérer la saisie de l'utilisateur
    if prompt:
        # Ajouter le message de l'utilisateur à l'historique
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Simuler une réponse de l'IA
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Simuler la génération de texte par l'IA
            assistant_response = f"Voici une ébauche de fiche de poste basée sur votre demande: '{prompt}'.\n\n"
            assistant_response += "Pour créer une fiche de poste complète, nous pouvons aborder les éléments suivants:\n"
            assistant_response += "- Description du poste\n- Responsabilités principales\n- Compétences requises\n- Formation et expérience\n- Avantages et rémunération"
            
            # Animation de l'écriture
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
        
        # Ajouter la réponse de l'IA à l'historique
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

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
    .candidate-card {
        background-color: #F3F4F6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .job-card {
        background-color: #EFF6FF;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
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
    .close-button {
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 24px;
        cursor: pointer;
    }
    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"] {
        gap: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialiser l'état pour le chat
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# Créer le menu de navigation horizontal
selected = option_menu(
    menu_title=None,
    options=["Home", "Fiches de Postes", "Candidats Idéaux"],
    icons=["house", "file-text", "people"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Bouton pour ouvrir le chat en haut à droite
col1, col2 = st.columns([4, 1])
with col2:
    if st.button("Génération de Poste"):
        st.session_state.chat_open = True

# Afficher le contenu de chaque page
if selected == "Home":
    st.markdown('<h1 class="main-header">Bienvenue sur votre Plateforme de Recrutement</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    Cette plateforme vous aide à gérer efficacement votre processus de recrutement:
    
    - **Fiches de Postes**: Consultez et gérez vos descriptions de postes
    - **Candidats Idéaux**: Visualisez les profils des candidats potentiels
    - **Génération de Poste**: Utilisez notre outil IA pour créer rapidement des fiches de postes
    
    Utilisez le menu ci-dessus pour naviguer entre les différentes fonctionnalités.
    """)
    
    # Quelques statistiques fictives
    st.subheader("Tableau de bord")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Postes Ouverts", value="12", delta="2")
    with col2:
        st.metric(label="Candidatures Reçues", value="87", delta="14")
    with col3:
        st.metric(label="Entretiens Planifiés", value="9", delta="-2")

elif selected == "Fiches de Postes":
    st.markdown('<h1 class="main-header">Fiches de Postes</h1>', unsafe_allow_html=True)
    
    # Exemple de fiches de postes
    fiches_postes = [
        {
            "titre": "Développeur Full Stack",
            "departement": "Technologie",
            "type": "CDI",
            "description": "Nous recherchons un développeur full stack expérimenté pour rejoindre notre équipe et travailler sur nos applications web et mobiles."
        },
        {
            "titre": "Chef de Projet Marketing",
            "departement": "Marketing",
            "type": "CDI",
            "description": "Responsable de la planification, du développement et de l'exécution des campagnes marketing pour nos produits et services."
        },
        {
            "titre": "Data Scientist",
            "departement": "Data & Analytics",
            "type": "CDI",
            "description": "Analyser de grands ensembles de données et créer des modèles prédictifs pour aider à la prise de décision commerciale."
        },
        {
            "titre": "Ingénieur DevOps",
            "departement": "Infrastructure",
            "type": "CDI",
            "description": "Responsable de l'infrastructure cloud, de l'automatisation du déploiement et de la mise en place des pipelines CI/CD."
        }
    ]
    
    # Ajouter un filtre de recherche
    search = st.text_input("Rechercher une fiche de poste")
    
    # Afficher les fiches de postes
    for job in fiches_postes:
        if search.lower() in job["titre"].lower() or search.lower() in job["departement"].lower() or search == "":
            st.markdown(f"""
            <div class="job-card">
                <h3>{job["titre"]}</h3>
                <p><strong>Département:</strong> {job["departement"]}</p>
                <p><strong>Type de contrat:</strong> {job["type"]}</p>
                <p>{job["description"]}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Bouton pour ajouter un nouveau poste
    if st.button("+ Ajouter une fiche de poste"):
        st.session_state.chat_open = True

elif selected == "Candidats Idéaux":
    st.markdown('<h1 class="main-header">Candidats Idéaux</h1>', unsafe_allow_html=True)
    
    # Exemple de candidats
    candidats = [
        {
            "nom": "Sophie Martin",
            "poste": "Développeur Full Stack",
            "competences": ["JavaScript", "React", "Node.js", "Python"],
            "experience": "5 ans",
            "matching": "95%"
        },
        {
            "nom": "Thomas Dubois",
            "poste": "Chef de Projet Marketing",
            "competences": ["Marketing Digital", "Gestion de Projet", "SEO/SEM"],
            "experience": "8 ans",
            "matching": "87%"
        },
        {
            "nom": "Emma Leroy",
            "poste": "Data Scientist",
            "competences": ["Python", "R", "Machine Learning", "SQL"],
            "experience": "3 ans",
            "matching": "92%"
        },
        {
            "nom": "Alexandre Bernard",
            "poste": "Ingénieur DevOps",
            "competences": ["AWS", "Docker", "Kubernetes", "Terraform"],
            "experience": "6 ans",
            "matching": "89%"
        },
        {
            "nom": "Julie Moreau",
            "poste": "Développeur Front-End",
            "competences": ["HTML/CSS", "JavaScript", "React", "Vue.js"],
            "experience": "4 ans",
            "matching": "83%"
        },
        {
            "nom": "Nicolas Petit",
            "poste": "Analyste Business",
            "competences": ["Analyse de données", "Tableau", "Power BI", "Excel"],
            "experience": "7 ans",
            "matching": "78%"
        }
    ]
    
    # Ajouter des filtres
    col1, col2 = st.columns(2)
    with col1:
        filtre_poste = st.selectbox("Filtre par poste", ["Tous"] + list(set([c["poste"] for c in candidats])))
    with col2:
        filtre_exp = st.slider("Expérience minimum (années)", 0, 10, 0)
    
    # Créer une grille de candidats
    filtered_candidats = [c for c in candidats if (filtre_poste == "Tous" or c["poste"] == filtre_poste) and int(c["experience"].split()[0]) >= filtre_exp]
    
    # Afficher la grille de candidats (3 par ligne)
    cols = st.columns(3)
    for i, candidat in enumerate(filtered_candidats):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="candidate-card">
                <h3>{candidat["nom"]}</h3>
                <p><strong>Poste ciblé:</strong> {candidat["poste"]}</p>
                <p><strong>Expérience:</strong> {candidat["experience"]}</p>
                <p><strong>Compétences:</strong> {", ".join(candidat["competences"])}</p>
                <p><strong>Matching:</strong> <span style="color: {'green' if float(candidat["matching"].strip('%')) > 85 else 'orange'};">{candidat["matching"]}</span></p>
            </div>
            """, unsafe_allow_html=True)

# Afficher le chat dans une colonne à droite s'il est ouvert
if st.session_state.chat_open:
    st.markdown("""
    <div class="chat-overlay">
        <div class="chat-container">
            <div class="chat-header">
                <h3>Génération de Poste assistée par IA</h3>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Créer deux colonnes pour afficher le chat sur le côté droit
    chat_col1, chat_col2 = st.columns([2, 1])
    
    with chat_col2:
        # Bouton pour fermer le chat
        if st.button("❌ Fermer"):
            st.session_state.chat_open = False
            st.experimental_rerun()
        
        # Afficher l'interface de chat
        chat_ia()