import streamlit as st
import time
from typing import List, Dict, Optional
from utils.styles import get_component_css
from views.components import render_top_bar, render_success_message

def render_chatbot_page():
    """
    Affiche une page dédiée au chatbot en dark mode.
    """
    # Ajouter le CSS spécifique à la page de chat
    st.markdown(get_component_css("chat_page"), unsafe_allow_html=True)
    
    # Afficher la barre supérieure
    render_top_bar()
    
    # En-tête de la page
    st.markdown("""
    <div class="chat-page-header">
        <h2>Génération de Poste assistée par IA</h2>
        <button class="stButton" onclick="history.back()">← Retour</button>
    </div>
    """, unsafe_allow_html=True)
    
    # Bouton de retour fonctionnel
    if st.button("← Retour", key="back_btn"):
        st.session_state.show_chatbot_page = False
        st.experimental_rerun()
    
    st.markdown('<div class="chat-page">', unsafe_allow_html=True)
    
    # Initialiser l'historique de chat
    if "chatbot_messages" not in st.session_state:
        st.session_state.chatbot_messages = [
            {
                "role": "assistant", 
                "content": "Bonjour! Je suis HiRo, votre assistant pour la génération de fiches de poste. Comment puis-je vous aider aujourd'hui?"
            }
        ]
    
    # Afficher les messages dans un conteneur scrollable
    st.markdown('<div class="chat-messages-container">', unsafe_allow_html=True)
    
    # Afficher chaque message
    for message in st.session_state.chatbot_messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Zone de saisie
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("", key="chatbot_input", placeholder="Décrivez le poste à générer...")
    with col2:
        send_button = st.button("Envoyer", key="send_btn")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Traiter la saisie utilisateur
    if user_input and send_button:
        # Ajouter le message utilisateur
        st.session_state.chatbot_messages.append({"role": "user", "content": user_input})
        
        # Simuler une réponse
        with st.spinner("Assistant en réflexion..."):
            time.sleep(1)
            
            # Réponse appropriée selon le contenu
            if "développeur" in user_input.lower():
                response = """Voici une fiche pour un développeur Full Stack :

**Titre :** Développeur Full Stack
**Département :** Technologies
**Type :** CDI
**Localisation :** Paris
**Salaire :** 45 000€ - 55 000€

**Missions :**
- Développer des fonctionnalités front-end et back-end
- Participer à la conception technique des projets
- Assurer la maintenance et l'amélioration continue des applications
- Collaborer avec les designers et les product managers

**Compétences requises :**
- JavaScript, React, Node.js
- HTML/CSS, responsive design
- SQL et NoSQL databases
- Git, CI/CD

Souhaitez-vous modifier certains aspects de cette fiche ?"""
            elif "marketing" in user_input.lower():
                response = """Voici une fiche pour un Chef de Projet Marketing :

**Titre :** Chef de Projet Marketing
**Département :** Marketing
**Type :** CDI
**Localisation :** Lyon
**Salaire :** 50 000€ - 60 000€

**Missions :**
- Élaborer et mettre en œuvre des stratégies marketing
- Gérer les budgets des campagnes et analyser leur ROI
- Coordonner les différentes équipes impliquées
- Suivre les KPIs et optimiser les performances

**Compétences requises :**
- Expérience en marketing digital
- Maîtrise des outils d'analyse marketing
- Excellentes capacités de communication
- Sens de l'organisation et gestion de projet

Cette fiche vous convient-elle ou souhaitez-vous des ajustements ?"""
            else:
                response = f"Je vais vous aider à créer une fiche de poste pour '{user_input}'. Pour commencer, pourriez-vous me préciser :\n\n1. Le niveau d'expérience requis\n2. Les principales responsabilités\n3. Les compétences techniques nécessaires"
            
            # Ajouter la réponse
            st.session_state.chatbot_messages.append({"role": "assistant", "content": response})
        
        # Rafraîchir
        st.experimental_rerun()
    
    # Bouton pour enregistrer si la conversation est avancée
    if len(st.session_state.chatbot_messages) > 3:
        if st.button("💾 Enregistrer cette fiche de poste", key="save_btn"):
            render_success_message("La fiche de poste a été enregistrée avec succès!")
            time.sleep(1.5)
            st.session_state.show_chatbot_page = False
            st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)