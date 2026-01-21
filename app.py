import streamlit as st
from PIL import Image
import random 

# --- CONFIGURATION GÉNÉRALE ---
st.set_page_config(page_title="Hub Formation CACES", layout="centered", page_icon="🏗️")

# --- STYLE CSS ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        height: 50px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .element-container { margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- MÉMOIRE (STATE) ---
def init_state(key):
    if key not in st.session_state:
        st.session_state[key] = False

# --- MENU LATÉRAL ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/5360/5360937.png", width=100)
st.sidebar.title("📚 CHOIX DU LIVRET")

livret = st.sidebar.selectbox(
    "Quelle formation suivez-vous ?",
    ["CACES R.485 (Gerbeurs)", "CACES R.489 (Chariots)", "CACES R.486 (PEMP)"]
)
st.sidebar.markdown("---")

# ==============================================================================
# GESTION DU RAZ (Remise à Zéro automatique)
# ==============================================================================
if "current_module" not in st.session_state:
    st.session_state.current_module = "Accueil R.485"

# Ton menu exactement comme tu le voulais
menu_485 = st.sidebar.radio("Modules R.485 :", 
    ["Accueil R.485", 
     "0. Tronc Commun (Aléatoire)",
     "1. Réglementation (Vrai/Faux)",
     "2. Catégories (p.12)", 
     "3. Causes Accidents (Auto-Test)", 
     "4. Acteurs (Auto-Test)", 
     "5. Organes (Auto-Test)", 
     "6. Stabilité (p.34)", 
     "7. Circulation (Vrai/Faux)",
     "8. Vérifications (Vrai/Faux)",
     "9. Pictogrammes (Auto-Test)"])

# Si on change de module, on nettoie la mémoire
if st.session_state.current_module != menu_485:
    st.session_state.clear()
    st.session_state.current_module = menu_485
    st.rerun()

# ==============================================================================
# ZONE R.485 (GERBEURS)
# ==============================================================================
if livret == "CACES R.485 (Gerbeurs)":

    # --- ACCUEIL ---
    if menu_485 == "Accueil R.485":
        st.title("🏗️ Formation Gerbeurs R.485")
        st.info("Bienvenue. Sélectionnez un module à gauche.")
        st.write("Les réponses se remettent à zéro automatiquement quand vous changez de module.")

    # --- MODULE 0 : TRONC COMMUN (ALÉATOIRE - 10 QUESTIONS) ---
    elif menu_485 == "0. Tronc Commun (Aléatoire)":
        st.header("🎲 Test Aléatoire (10 Questions)")
        st.write("Ce module pioche 10 questions au hasard.")
        
        # BANQUE DE QUESTIONS (Complétée à 10)
        banque_questions = [
            {"question": "Distance sécu entre 2 chariots ?", "options": ["1 m", "3 longueurs (5m)", "10 m"], "reponse": "3 longueurs (5m)", "explication": "Pour éviter les collisions."},
            {"question": "Qui délivre l'autorisation de conduite ?", "options": ["Formateur", "Médecin", "Employeur"], "reponse": "Employeur", "explication": "Le CACES est délivré par le testeur, l'autorisation par le chef d'entreprise."},
            {"question": "Fuite d'acide sur batterie, je rince avec ?", "options": ["Eau", "Sable", "Chiffon"], "reponse": "Eau", "explication": "Abondamment."},
            {"question": "Validité CACES ?", "options": ["1 an", "5 ans", "10 ans"], "reponse": "5 ans", "explication": "À renouveler."},
            {"question": "Cause principale renversement ?", "options": ["Vitesse virage", "Panne", "Klaxon"], "reponse": "Vitesse virage", "explication": "Force centrifuge."},
            {"question": "Téléphone au volant ?", "options": ["Jamais", "Si doucement", "Avec écouteurs"], "reponse": "Jamais", "explication": "Tolérance zéro."},
            {"question": "Quand consulter la plaque de charge ?", "options": ["1x/an", "Avant levage lourd", "Jamais"], "reponse": "Avant levage lourd", "explication": "Pour vérifier la capacité."},
            {"question": "Vérifications prise de poste ?", "options": ["Facultatives", "Obligatoires", "Hebdomadaires"], "reponse": "Obligatoires", "explication": "Tous les jours."},
            {"question": "EPI obligatoires ?", "options": ["Chaussures sécu", "Casquette", "Gants laine"], "reponse": "Chaussures sécu", "explication": "Protection des pieds."},
            {"question": "Fumer en chargeant batterie ?", "options": ["Oui", "Non", "Si fenêtre ouverte"], "reponse": "Non", "explication": "Risque explosion hydrogène."}
        ]

        if "questions_du_jour" not in st.session_state:
            # On pioche 10 questions (ou le max dispo)
            nb = min(10, len(banque_questions))
            st.session_state.questions_du_jour = random.sample(banque_questions, nb)
        
        if st.button("🔄 NOUVEAU TIRAGE"):
            nb = min(10, len(banque_questions))
            st.session_state.questions_du_jour = random.sample(banque_questions, nb)
            st.rerun()

        st.markdown("---")

        for i, q in enumerate(st.session_state.questions_du_jour):
            st.subheader(f"Question {i+1}")
            st.write(f"**{q['question']}**")
            choix = st.radio(f"Réponse :", q['options'], key=f"rd_{i}", index=None)
            
            if choix:
                if choix == q['reponse']:
                    st.success(f"✅ BRAVO ! {q['explication']}")
                else:
                    st.error(f"❌ FAUX. Réponse : {q['reponse']}")
            st.markdown("---")

    # --- MODULE 1 : RÉGLEMENTATION ---
    elif menu_485 == "1. Réglementation (Vrai/Faux)":
        st.header("📋 Réglementation")
        init_state("reg_q1"); init_state("reg_q2"); init_state("reg_q3"); init_state("reg_q4"); init_state("reg_q5")
        st.markdown("---")

        st.subheader("1. Formation Obligatoire ?")
        c1, c2 = st.columns(2)
        if c1.button("VRAI", key="rg1_v") or st.session_state.reg_q1:
            st.session_state.reg_q1 = True
            st.success("✅ VRAI")
        if c2.button("FAUX", key="rg1_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("2. Cariste responsable matériel ?")
        c3, c4 = st.columns(2)
        if c3.button("VRAI", key="rg2_v") or st.session_state.reg_q2:
            st.session_state.reg_q2 = True
            st.success("✅ VRAI")
        if c4.button("FAUX", key="rg2_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("3. Autorisation par l'organisme ?")
        c5, c6 = st.columns(2)
        if c5.button("VRAI", key="rg3_v"): st.error("❌ FAUX")
        if c6.button("FAUX", key="rg3_f") or st.session_state.reg_q3:
            st.session_state.reg_q3 = True
            st.success("✅ FAUX (C'est l'employeur)")
        st.markdown("---")

        st.subheader("4. 18 ans minimum ?")
        c7, c8 = st.columns(2)
        if c7.button("VRAI", key="rg4_v") or st.session_state.reg_q4:
            st.session_state.reg_q4 = True
            st.success("✅ VRAI")
        if c8.button("FAUX", key="rg4_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("5. Pas de formation pour occasionnel ?")
        c9, c10 = st.columns(2)
        if c9.button("VRAI", key="rg5_v"): st.error("❌ FAUX")
        if c10.button("FAUX", key="rg5_f") or st.session_state.reg_q5:
            st.session_state.reg_q5 = True
            st.success("✅ FAUX")

    # --- MODULE 2 : CATÉGORIES ---
    elif menu_485 == "2. Catégories (p.12)":
        st.header("🔍 Quiz : Reconnaissance des Engins")
        init_state("cat_q1"); init_state("cat_q2"); init_state("cat_q3"); init_state("cat_q4")

        col1, col2 = st.columns(2)
        with col1:
            try: st.image("images/Image1.png") # Gerbeur Jaune
            except: st.error("Image manquante")
            if st.button("Est-ce un R.485 ? (1)") or st.session_state.cat_q1:
                st.session_state.cat_q1 = True
                st.success("✅ OUI (Catégorie 1 ou 2)")
            st.markdown("---")
            try: st.image("images/Image3.png") # Gerbeur Orange
            except: st.error("Image manquante")
            if st.button("Est-ce un R.485 ? (3)") or st.session_state.cat_q3:
                st.session_state.cat_q3 = True
                st.success("✅ OUI (Catégorie 1 ou 2)")
        with col2:
            try: st.image("images/Image2.png") # Transpalette
            except: st.error("Image manquante")
            if st.button("Est-ce un R.485 ? (2)") or st.session_state.cat_q2:
                st.session_state.cat_q2 = True
                st.error("❌ NON (R.366 - Transpalette)")
            st.markdown("---")
            try: st.image("images/Image4.png") # Porté
            except: st.error("Image manquante")
            if st.button("Est-ce un R.485 ? (4)") or st.session_state.cat_q4:
                st.session_state.cat_q4 = True
                st.error("❌ NON (R.489 - Porté)")

    # --- MODULE 3 : CAUSES ACCIDENTS ---
    elif menu_485 == "3. Causes Accidents (Auto-Test)":
        st.header("⚠️ Causes d'accidents")
        for i in range(1, 11): init_state(f"cause_q{i}")
        st.markdown("---")

        q_data = [
            ("1. Mauvais positionnement bras", "Conducteur", "c1"),
            ("2. Mauvaise stabilisation", "Conducteur", "c2"),
            ("3. Problème de direction", "Matériel", "m3"),
            ("4. Manque de visibilité", "Environnement", "e4"),
            ("5. Trou dans le sol", "Environnement", "e5"),
            ("6. Vitesse excessive", "Conducteur", "c6"),
            ("7. Roue défectueuse", "Matériel", "m7"),
            ("8. Mauvaise évaluation charge", "Conducteur", "c8"),
            ("9. Stockage dangereux", "Environnement", "e9"),
            ("10. Problème de frein", "Matériel", "m10")
        ]

        for i, (q_text, bon_choix, key_suffix) in enumerate(q_data):
            st.markdown(f"#### {q_text}")
            c1, c2, c3 = st.columns(3)
            key_q = f"cause_q{i+1}"
            
            if c1.button("Conducteur", key=f"btn_{i}_c"):
                if bon_choix == "Conducteur": 
                    st.session_state[key_q] = True
                    st.success("✅ CORRECT")
                else: st.error("❌ Non")
            
            if c2.button("Matériel", key=f"btn_{i}_m"):
                if bon_choix == "Matériel":
                    st.session_state[key_q] = True
                    st.success("✅ CORRECT")
                else: st.error("❌ Non")
            
            if c3.button("Environnement", key=f"btn_{i}_e"):
                if bon_choix == "Environnement":
                    st.session_state[key_q] = True
                    st.success("✅ CORRECT")
                else
