import streamlit as st
import time
from typing import List, Dict, Optional
from utils.styles import get_component_css
from views.components import render_top_bar, render_success_message
from utils.api import generate_fiche_api
import base64

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
    ## if st.button("← Retour", key="back_btn"):
    ##     st.session_state.show_chatbot_page = False
    ##     st.rerun()
    
    st.markdown('<div class="chat-page">', unsafe_allow_html=True)
    
    # Initialiser l'historique de chat
    if "chatbot_messages" not in st.session_state:
        st.session_state.chatbot_messages = [
            {
                "role": "assistant", 
                "content": "Bonjour! Je suis HiRo, votre assistant pour la génération de fiches de poste. Comment puis-je vous aider aujourd'hui?"
            }
        ]

    if "fiche_inputs" not in st.session_state:
        st.session_state.fiche_inputs = {
            "titre" : "",
            "secteur":"",
            "contrat":"",
            "niveau" : "",
            "competences" : ""
        }

    with st.expander("✍️ Paramètres personnalisés de la fiche", expanded=True) :
        st.session_state.fiche_inputs["titre"] = st.text_input("Titre du poste", value=st.session_state.fiche_inputs["titre"])
        st.session_state.fiche_inputs["secteur"] = st.text_input("Secteur", value=st.session_state.fiche_inputs["secteur"])
        st.session_state.fiche_inputs["contrat"] = st.text_input("Type de contrat", value=st.session_state.fiche_inputs["contrat"])
        st.session_state.fiche_inputs["niveau"] = st.text_input("Niveau d'expérience", value=st.session_state.fiche_inputs["niveau"])
        st.session_state.fiche_inputs["competences"] = st.text_area("Compétences (séparées par virgule)", value=st.session_state.fiche_inputs["competences"])

    # Affichage de l'historique
    for msg in st.session_state.chatbot_messages:
        cls = "user-message" if msg["role"] == "user" else "bot-message"
        st.markdown(f'<div class="{cls}">{msg["content"]}</div>', unsafe_allow_html=True)

    # Zone de saisie utilisateur
    user_input = st.text_input("Votre message", key="chatbot_input", placeholder="Posez une question ou cliquez sur Générer…")
    generate_btn = st.button("Générer la fiche de poste", key="generate_btn")

    response = None
    # Si on clique sur Générer
    if generate_btn:
        # On stocke le message de l'utilisateur
        if user_input:
            st.session_state.chatbot_messages.append({"role": "user", "content": user_input})

        with st.spinner("Génération de la fiche…"):
            inputs = st.session_state.fiche_inputs
            # Validation des champs
            if not all(inputs.values()):
                response = "Veuillez remplir tous les champs du formulaire avant de générer la fiche."
            else:
                try:
                    response = generate_fiche_api(
                        titre=inputs["titre"],
                        secteur=inputs["secteur"],
                        contrat=inputs["contrat"],
                        niveau=inputs["niveau"],
                        competences=inputs["competences"]
                    )
                except Exception as e:
                    response = f"Erreur lors de l'appel à l'API : {e}"

        # On ajoute la réponse du bot
        st.session_state.chatbot_messages.append({
            "role": "assistant",
            "content": response if isinstance(response, str) else response.get("fiche", "")
        })

    # Si la réponse contient un PDF, on propose le téléchargement
    if isinstance(response, dict) and "fichierPDF" in response:
        pdf_bytes = base64.b64decode(response["fichierPDF"])
        st.download_button(
            label="📄 Télécharger la fiche PDF",
            data=pdf_bytes,
            file_name="fiche_poste.pdf",
            mime="application/pdf"
        )

    # Bouton Enregistrer dans la BDD
    if len(st.session_state.chatbot_messages) > 1:
        if st.button("💾 Enregistrer cette fiche de poste", key="save_btn"):
            render_success_message("La fiche de poste a été enregistrée avec succès !")
            time.sleep(1.5)
            # Aucun rerun nécessaire, on peut juste vider l'historique si besoin
            st.session_state.chatbot_messages = []

    st.markdown('</div>', unsafe_allow_html=True)       



    
    # Afficher chaque message
    ## st.markdown('<div class="chat-messages-container">', unsafe_allow_html=True)
    ## for message in st.session_state.chatbot_messages:
    ##     role_class = "user-message" if message["role"] == "user" else "bot-message"
    ##     st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)
    ## st.markdown('</div>', unsafe_allow_html=True)
    ## 
    ##     
    ## send_button = st.button("Generer", key="send_btn")
    ## 
    ## if send_button:
    ##     with st.spinner("Génération de la fiche..."):
    ##         inputs = st.session_state.fiche_inputs
    ##         if not all(inputs.values()):
    ##             response = "❗Veuillez remplir tous les champs du formulaire avant de générer la fiche."
    ##         else:
    ##             try:
    ##                 response = generate_fiche_api(
    ##                     titre=inputs["titre"],
    ##                     secteur=inputs["secteur"],
    ##                     contrat=inputs["contrat"],
    ##                     niveau=inputs["niveau"],
    ##                     competences=inputs["competences"]
    ##                 )
    ##             except Exception as e:
    ##                 response = f"❌ Une erreur est survenue : {e}"
## 
    ##     # Traitement de la réponse
    ##     if isinstance(response, dict) and "fiche" in response:
    ##         st.session_state.chatbot_messages.append({
    ##             "role": "assistant",
    ##             "content": response["fiche"]
    ##         })
    ##     elif isinstance(response, str):
    ##         st.session_state.chatbot_messages.append({
    ##             "role": "assistant",
    ##             "content": response
    ##         })
## 
    ##     if isinstance(response, dict) and "fichierPDF" in response:
    ##         pdf_data = base64.b64decode(response["fichierPDF"])
    ##         st.download_button("📄 Télécharger la fiche PDF", data=pdf_data, file_name="fiche_poste.pdf", mime="application/pdf")
## 
    ## # Bouton enregistrer
    ## if len(st.session_state.chatbot_messages) > 3:
    ##     if st.button("💾 Enregistrer cette fiche de poste", key="save_btn"):
    ##         render_success_message("La fiche de poste a été enregistrée avec succès!")
    ##         time.sleep(1.5)
    ##         st.session_state.show_chatbot_page = False
    ##         st.rerun()
## 
    ## st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_chatbot_page()