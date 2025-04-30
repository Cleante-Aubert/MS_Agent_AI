import streamlit as st
import time
import base64

from utils.styles import get_component_css
from views.components import render_top_bar, render_success_message
from utils.api import generate_fiche_api

def render_chatbot_page():
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
    
    # Initialiser l'historique de chat
    if "chatbot_messages" not in st.session_state:
        st.session_state.chatbot_messages = [
            {
                "role": "assistant", 
                "content": "Bonjour! Je suis HiRo, votre assistant pour la génération de fiches de poste. Remplissez les champs ci-dessous pour commencer."
            }
        ]

    if "fiche_inputs" not in st.session_state:
        st.session_state.fiche_inputs = {
            "titre": "",
            "secteur": "",
            "contrat": "",
            "niveau": "",
            "competences": ""
        }

    with st.expander("✍️ Paramètres personnalisés de la fiche", expanded=True):
        st.session_state.fiche_inputs["titre"] = st.text_input("Titre du poste", value=st.session_state.fiche_inputs["titre"])
        st.session_state.fiche_inputs["secteur"] = st.text_input("Secteur", value=st.session_state.fiche_inputs["secteur"])
        st.session_state.fiche_inputs["contrat"] = st.text_input("Type de contrat", value=st.session_state.fiche_inputs["contrat"])
        st.session_state.fiche_inputs["niveau"] = st.text_input("Niveau d'expérience", value=st.session_state.fiche_inputs["niveau"])
        st.session_state.fiche_inputs["competences"] = st.text_area("Compétences (séparées par virgule)", value=st.session_state.fiche_inputs["competences"])

    generate_btn = st.button("Générer la fiche de poste ✨", key="generate_btn")

    response = None
    fiche_generee = False

    # Si on clique sur Générer ou Régénérer
    if generate_btn or st.session_state.get("regenerate_flag", False):
        st.session_state["regenerate_flag"] = False  # reset le flag
        with st.spinner("Génération de la fiche…"):
            inputs = st.session_state.fiche_inputs

            # Validation des champs
            if not all(inputs.values()):
                response = "❌ Veuillez remplir tous les champs du formulaire avant de générer la fiche."
                st.session_state.chatbot_messages.append({"role": "assistant", "content": response})
            else:
                try:
                    response = generate_fiche_api(
                        titre=inputs["titre"],
                        secteur=inputs["secteur"],
                        contrat=inputs["contrat"],
                        niveau=inputs["niveau"],
                        competences=inputs["competences"]
                    )
                    fiche_generee = True
                    fiche_texte = response["fiche"] if isinstance(response, dict) else response
                    st.session_state.chatbot_messages.append({"role": "assistant", "content": fiche_texte})
                except Exception as e:
                    error_msg = f"❌ Erreur lors de l'appel à l'API : {e}"
                    st.session_state.chatbot_messages.append({"role": "assistant", "content": error_msg})
                    fiche_generee = False

    # Affichage de l'historique
    for msg in st.session_state.chatbot_messages:
        cls = "user-message" if msg["role"] == "user" else "bot-message"
        st.markdown(f'<div class="{cls}">{msg["content"]}</div>', unsafe_allow_html=True)

    # Affichage des options après génération
    if fiche_generee:
        # Bouton Télécharger
        if "fichierPDF" in response:
            pdf_bytes = base64.b64decode(response["fichierPDF"])
            st.download_button(
                label="📄 Télécharger la fiche PDF",
                data=pdf_bytes,
                file_name="fiche_poste.pdf",
                mime="application/pdf"
            )

        # Bouton Régénérer
        if st.button("🔁 Régénérer la fiche"):
            st.session_state["regenerate_flag"] = True
            st.rerun()

        # Bouton Enregistrer
        if st.button("💾 Enregistrer cette fiche de poste", key="save_btn"):
            render_success_message("La fiche de poste a été enregistrée avec succès !")
            time.sleep(1.5)
            st.session_state.chatbot_messages = []

    st.markdown('</div>', unsafe_allow_html=True)       

if __name__ == "__main__":
    render_chatbot_page()
