import streamlit as st

def load_css():
    """
    Charge les styles CSS en dark mode pour l'application.
    """
    css = """
    <style>
        /* Variables pour les couleurs du dark mode */
        :root {
            --primary-color: #00A8A8;
            --secondary-color: #006666;
            --bg-color: #121212;
            --card-color: #1E1E1E;
            --text-color: #E0E0E0;
            --text-muted: #AAAAAA;
            --border-color: #333333;
            --input-bg: #2A2A2A;
            --highlight: #ABFFFF;
        }
        
        /* Styles globaux dark mode */
        .stApp, body, [data-testid="stAppViewContainer"] {
            background-color: var(--bg-color) !important;
            color: var(--text-color) !important;
        }
        
        /* Masquer éléments Streamlit par défaut */
        .stApp header, footer, [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        /* En-têtes */
        .main-header {
            font-size: 2rem;
            font-weight: 600;
            color: var(--text-color);
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .subheader {
            font-size: 1.5rem;
            font-weight: 500;
            color: var(--text-color);
            margin: 1rem 0;
        }
        
        /* Top bar */
        .top-bar {
            background-color: var(--card-color);
            padding: 12px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
        }
        
        .logo {
            color: var(--primary-color);
            font-size: 26px;
            font-weight: bold;
        }
        
        .profile {
            background-color: var(--secondary-color);
            padding: 5px 15px;
            border-radius: 20px;
            color: white;
            display: flex;
            align-items: center;
        }
        
        /* Cartes */
        .job-card {
            background-color: var(--card-color);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            border: 1px solid var(--border-color);
        }
        
        .job-card h3 {
            color: var(--primary-color);
            margin-top: 0;
            margin-bottom: 12px;
        }
        
        .job-card p {
            color: var(--text-color);
            margin: 8px 0;
        }
        
        .candidate-card {
            background-color: var(--card-color);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            border: 1px solid var(--border-color);
        }
        
        .candidate-card h3 {
            color: var(--primary-color);
            margin-top: 0;
            margin-bottom: 12px;
        }
        
        /* Statistiques */
        .stat-card {
            background-color: var(--card-color);
            border-radius: 8px;
            padding: 16px;
            text-align: center;
            border: 1px solid var(--border-color);
        }
        
        .stat-value {
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--primary-color);
            margin: 10px 0;
        }
        
        .stat-label {
            color: var(--text-color);
            font-size: 1rem;
        }
        
        /* Boutons */
        .stButton > button {
            background-color: var(--primary-color) !important;
            color: white !important;
            font-weight: 500 !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 0.5rem 1rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            background-color: var(--secondary-color) !important;
            box-shadow: 0 0 8px rgba(0, 168, 168, 0.5) !important;
        }
        
        /* Bouton de génération de poste */
        .gen-post-btn {
            background-color: var(--primary-color);
            color: white;
            padding: 10px 16px;
            border-radius: 4px;
            display: inline-block;
            cursor: pointer;
            text-align: center;
            margin-bottom: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }
        
        .gen-post-btn:hover {
            background-color: var(--secondary-color);
            box-shadow: 0 0 8px rgba(0, 168, 168, 0.5);
        }
        
        /* Chat */
        .chat-container {
            background-color: var(--card-color);
            border-radius: 8px;
            padding: 16px;
            margin-top: 16px;
            border: 1px solid var(--border-color);
        }
        
        .chat-header {
            background-color: var(--primary-color);
            color: white;
            padding: 12px 16px;
            border-radius: 6px 6px 0 0;
            margin: -16px -16px 16px -16px;
            font-weight: 500;
        }
        
        .user-message {
            background-color: var(--input-bg);
            padding: 10px 14px;
            border-radius: 8px;
            margin-bottom: 12px;
            margin-left: 25%;
            margin-right: 0;
            color: var(--text-color);
        }
        
        .bot-message {
            background-color: #004444;
            padding: 10px 14px;
            border-radius: 8px;
            margin-bottom: 12px;
            margin-right: 25%;
            margin-left: 0;
            color: var(--text-color);
        }
        
        /* Messages */
        .success-message {
            background-color: #004D40;
            color: #A7FFEB;
            padding: 12px 16px;
            border-radius: 4px;
            margin-top: 12px;
            text-align: center;
            border-left: 4px solid #00BFA5;
        }
        
        .error-message {
            background-color: #4A1212;
            color: #FFCDD2;
            padding: 12px 16px;
            border-radius: 4px;
            margin-top: 12px;
            text-align: center;
            border-left: 4px solid #D32F2F;
        }
        
        /* Inputs dark mode */
        .stTextInput > div > div > input {
            background-color: var(--input-bg) !important;
            color: var(--text-color) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        .stTextInput > label {
            color: var(--text-color) !important;
        }
        
        .stTextArea > div > div > textarea {
            background-color: var(--input-bg) !important;
            color: var(--text-color) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        /* Select boxes dark mode */
        .stSelectbox > div > div > div {
            background-color: var(--input-bg) !important;
            color: var(--text-color) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        /* Slider dark mode */
        .stSlider > div > div > div > div {
            background-color: var(--primary-color) !important;
        }
        
        /* Navigation menu dark mode */
        .nav-link {
            background-color: var(--card-color) !important;
            color: var(--text-color) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        .nav-link.active {
            background-color: var(--primary-color) !important;
            color: white !important;
            border: 1px solid var(--primary-color) !important;
        }
        
        .nav-link:hover:not(.active) {
            background-color: var(--input-bg) !important;
        }
        
        /* Text color overrides */
        p, h1, h2, h3, h4, h5, h6, span, div {
            color: var(--text-color) !important;
        }
        
        /* Links in dark mode */
        a {
            color: var(--primary-color) !important;
        }
        
        a:hover {
            color: var(--highlight) !important;
        }
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

def get_component_css(component_name: str) -> str:
    """
    Récupère le CSS pour un composant spécifique (version dark mode).
    """
    css = {
        "chat_page": """
        <style>
            .chat-page {
                background-color: #121212;
                min-height: calc(100vh - 100px);
                padding: 20px;
                border-radius: 8px;
            }
            
            .chat-page-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
                padding-bottom: 10px;
                border-bottom: 1px solid #333333;
            }
            
            .chat-messages-container {
                max-height: 60vh;
                overflow-y: auto;
                margin-bottom: 20px;
                padding-right: 10px;
            }
            
            .chat-input-container {
                background-color: #1E1E1E;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #333333;
            }
        </style>
        """
    }
    
    return css.get(component_name, "")