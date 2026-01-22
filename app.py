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
                else: st.error("❌ Non")
            
            if st.session_state[key_q]:
                st.success("✅ DÉJÀ TROUVÉ")
            st.markdown("---")

    # --- MODULE 4 : ACTEURS ---
    elif menu_485 == "4. Acteurs (Auto-Test)":
        st.header("🤝 Les Acteurs")
        init_state("act_q1"); init_state("act_q2"); init_state("act_q3"); init_state("act_q4"); init_state("act_q5")
        st.markdown("---")

        st.subheader("1. Droit d'entrée partout ?")
        c1, c2 = st.columns([2, 1])
        with c1:
            if st.button("La CARSAT", key="btn_a1_a"): st.error("❌ Non")
            if st.button("Inspecteur Travail", key="btn_a1_b") or st.session_state.act_q1:
                st.session_state.act_q1 = True
                st.success("✅ EXACT")
                try: st.image("images/Acteur_Inspecteur.png", width=150)
                except: st.write("Manque img")
            if st.button("Le Fabricant", key="btn_a1_c"): st.error("❌ Non")
        st.markdown("---")

        st.subheader("2. Marquage CE ?")
        c3, c4 = st.columns([2, 1])
        with c3:
            if st.button("Le Chef d'équipe", key="btn_a2_a"): st.error("❌ Non")
            if st.button("Le Fabricant", key="btn_a2_b") or st.session_state.act_q2:
                st.session_state.act_q2 = True
                st.success("✅ EXACT")
                try: st.image("images/Acteur_Fabricant.png", width=150)
                except: st.write("Manque img")
            if st.button("L'Inspecteur", key="btn_a2_c"): st.error("❌ Non")
        st.markdown("---")

        st.subheader("3. Organisme Prévention ?")
        c5, c6 = st.columns([2, 1])
        with c5:
            if st.button("Le CSE", key="btn_a3_a"): st.error("❌ Non")
            if st.button("La CARSAT", key="btn_a3_b") or st.session_state.act_q3:
                st.session_state.act_q3 = True
                st.success("✅ EXACT")
                try: st.image("images/Acteur_CARSAT.png", width=150)
                except: st.write("Manque img")
        st.markdown("---")

        st.subheader("4. Enquêtes accident ?")
        c7, c8 = st.columns([2, 1])
        with c7:
            if st.button("Le CSE / CSSCT", key="btn_a4_a") or st.session_state.act_q4:
                st.session_state.act_q4 = True
                st.success("✅ EXACT")
                try: st.image("images/Acteur_CSE.png", width=150)
                except: st.write("Manque img")
            if st.button("Médecine travail", key="btn_a4_b"): st.error("❌ Non")
        st.markdown("---")

        st.subheader("5. Responsable sécurité ?")
        c9, c10 = st.columns([2, 1])
        with c9:
            if st.button("Le Fabricant", key="btn_a5_a"): st.error("❌ Non")
            if st.button("L'employeur", key="btn_a5_b") or st.session_state.act_q5:
                st.session_state.act_q5 = True
                st.success("✅ EXACT")
                try: st.image("images/Acteur_Personnel.png", width=150)
                except: st.write("Manque img")

    # --- MODULE 5 : ORGANES ---
    elif menu_485 == "5. Organes (Auto-Test)":
        st.header("🔧 Identification des Organes")
        init_state("org_q1"); init_state("org_q2"); init_state("org_q3"); init_state("org_q4"); init_state("org_q5")
        st.markdown("---")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            try: st.image("images/Image1.png", use_column_width=True)
            except: st.error("Manque Image1.png")
        with col2:
            st.markdown("#### 1. Élément ?")
            if st.button("Dispositif condamnation", key="btn_o1_a"): st.error("❌ Non")
            if st.button("Commande anti-écrasement", key="btn_o1_b") or st.session_state.org_q1:
                st.session_state.org_q1 = True
                st.success("✅ EXACT")
            if st.button("Avertisseur sonore", key="btn_o1_c"): st.error("❌ Non")
        st.markdown("---")

        col3, col4 = st.columns([1, 2])
        with col3:
            try: st.image("images/Image2.png", use_column_width=True)
            except: st.error("Manque Image2.png")
        with col4:
            st.markdown("#### 2. Élément ?")
            if st.button("Digicode / Clé", key="btn_o2_a") or st.session_state.org_q2:
                st.session_state.org_q2 = True
                st.success("✅ EXACT")
            if st.button("Sélecteur", key="btn_o2_b"): st.error("❌ Non")
            if st.button("Indicateur décharge", key="btn_o2_c"): st.error("❌ Non")
        st.markdown("---")

        col5, col6 = st.columns([1, 2])
        with col5:
            try: st.image("images/Image3.png", use_column_width=True)
            except: st.error("Manque Image3.png")
        with col6:
            st.markdown("#### 3. Élément ?")
            if st.button("Roue directrice", key="btn_o3_a"): st.error("❌ Non")
            if st.button("Galet porteur", key="btn_o3_b"): st.error("❌ Non")
            if st.button("Roue stabilisatrice", key="btn_o3_c") or st.session_state.org_q3:
                st.session_state.org_q3 = True
                st.success("✅ EXACT")
        st.markdown("---")

        col7, col8 = st.columns([1, 2])
        with col7:
            try: st.image("images/Image4.png", use_column_width=True)
            except: st.error("Manque Image4.png")
        with col8:
            st.markdown("#### 4. Bouton Tortue ?")
            if st.button("Vitesse lente", key="btn_o4_a") or st.session_state.org_q4:
                st.session_state.org_q4 = True
                st.success("✅ EXACT")
            if st.button("Klaxon", key="btn_o4_b"): st.error("❌ Non")
            if st.button("Levée", key="btn_o4_c"): st.error("❌ Non")
        st.markdown("---")

        col9, col10 = st.columns([1, 2])
        with col9:
            try: st.image("images/Image5.png", use_column_width=True)
            except: st.error("Manque Image5.png")
        with col10:
            st.markdown("#### 5. Élément ?")
            if st.button("Roue directrice", key="btn_o5_a") or st.session_state.org_q5:
                st.session_state.org_q5 = True
                st.success("✅ EXACT")
            if st.button("Roue stabilisatrice", key="btn_o5_b"): st.error("❌ Non")
            if st.button("Roue libre", key="btn_o5_c"): st.error("❌ Non")

    # --- MODULE 6 : STABILITÉ ---
    elif menu_485 == "6. Stabilité (p.34)":
        st.header("⚖️ Exercice : Plaques de Charge")
        init_state("plaque_q1"); init_state("plaque_q2"); init_state("plaque_q3"); init_state("plaque_q4")
        st.markdown("---")

        col_img1, col_txt1 = st.columns([3, 1])
        with col_img1:
            try: st.image("quizz_plaque_de_charge_gerbeur_haut.png", use_column_width=True)
            except: st.error("⚠️ Manque: quizz_plaque_de_charge_gerbeur_haut.png")
        with col_txt1:
            st.markdown("#### 1. Hauteur max ?")
            st.write("Pour **630 kg** (L=1200mm) :")
            if st.button("4000 mm", key="btn_q1_a") or st.session_state.plaque_q1:
                st.session_state.plaque_q1 = True
                st.success("✅ 4000 mm")
            if st.button("4300 mm", key="btn_q1_b"): st.error("❌ Non")
            st.write("---")
            st.markdown("#### 2. Poids max ?")
            st.write("À **4300 mm** (Charge longue) :")
            if st.button("330 kg", key="btn_q2_a") or st.session_state.plaque_q2:
                st.session_state.plaque_q2 = True
                st.success("✅ 330 kg")
            if st.button("550 kg", key="btn_q2_b"): st.error("❌ Non")
        st.markdown("---")

        col_img2, col_txt2 = st.columns([3, 1])
        with col_img2:
            try: st.image("quizz_plaque_de_charge_gerbeur_milieu.png", use_column_width=True)
            except: st.error("⚠️ Manque: quizz_plaque_de_charge_gerbeur_milieu.png")
        with col_txt2:
            st.markdown("#### 3. Graphique")
            st.write("**1400 kg** à **400 mm**. Hauteur ?")
            if st.button("3884 mm", key="btn_q3_a") or st.session_state.plaque_q3:
                st.session_state.plaque_q3 = True
                st.success("✅ 3884 mm")
            if st.button("4224 mm", key="btn_q3_b"): st.error("❌ Trop haut")
        st.markdown("---")

        col_img3, col_txt3 = st.columns([3, 1])
        with col_img3:
            try: st.image("quizz_plaque_de_charge_gerbeur_bas.png", use_column_width=True)
            except: st.error("⚠️ Manque: quizz_plaque_de_charge_gerbeur_bas.png")
        with col_txt3:
            st.markdown("#### 4. Constructeur")
            st.write("Je peux déplacer :")
            if st.button("1200kg à 600mm", key="btn_q4_a") or st.session_state.plaque_q4:
                st.session_state.plaque_q4 = True
                st.success("✅ EXACT")
            if st.button("1556kg à 300mm", key="btn_q4_b"): st.error("❌ Non")

    # --- MODULE 7 : CIRCULATION ---
    elif menu_485 == "7. Circulation (Vrai/Faux)":
        st.header("🚦 Circulation")
        init_state("circ_q1"); init_state("circ_q2"); init_state("circ_q3"); init_state("circ_q4"); init_state("circ_q5")
        st.markdown("---")

        st.subheader("1. Interdit charge haute ?")
        c1, c2 = st.columns(2)
        if c1.button("VRAI", key="cr1_v") or st.session_state.circ_q1:
            st.session_state.circ_q1 = True
            st.success("✅ VRAI")
        if c2.button("FAUX", key="cr1_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("2. Transport collègue ?")
        c3, c4 = st.columns(2)
        if c3.button("VRAI", key="cr2_v"): st.error("❌ FAUX")
        if c4.button("FAUX", key="cr2_f") or st.session_state.circ_q2:
            st.session_state.circ_q2 = True
            st.success("✅ FAUX")
        st.markdown("---")

        st.subheader("3. Arrêt = Fourches au sol ?")
        c5, c6 = st.columns(2)
        if c5.button("VRAI", key="cr3_v") or st.session_state.circ_q3:
            st.session_state.circ_q3 = True
            st.success("✅ VRAI")
        if c6.button("FAUX", key="cr3_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("4. Téléphone en roulant ?")
        c7, c8 = st.columns(2)
        if c7.button("VRAI", key="cr4_v"): st.error("❌ NON")
        if c8.button("FAUX", key="cr4_f") or st.session_state.circ_q4:
            st.session_state.circ_q4 = True
            st.success("✅ FAUX")
        st.markdown("---")

        st.subheader("5. Distance 3 gerbeurs ?")
        c9, c10 = st.columns(2)
        if c9.button("VRAI", key="cr5_v") or st.session_state.circ_q5:
            st.session_state.circ_q5 = True
            st.success("✅ VRAI")
        if c10.button("FAUX", key="cr5_f"): st.error("❌ Erreur")

    # --- MODULE 8 : VÉRIFICATIONS ---
    elif menu_485 == "8. Vérifications (Vrai/Faux)":
        st.header("🔍 Vérifications")
        init_state("verif_q1"); init_state("verif_q2"); init_state("verif_q3"); init_state("verif_q4"); init_state("verif_q5")
        st.markdown("---")

        st.subheader("1. VGP tous les 6 mois ?")
        c1, c2 = st.columns(2)
        if c1.button("VRAI", key="vf1_v") or st.session_state.verif_q1:
            st.session_state.verif_q1 = True
            st.success("✅ VRAI")
        if c2.button("FAUX", key="vf1_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("2. Carnet entretien hebdo ?")
        c3, c4 = st.columns(2)
        if c3.button("VRAI", key="vf2_v"): st.error("❌ FAUX")
        if c4.button("FAUX", key="vf2_f") or st.session_state.verif_q2:
            st.session_state.verif_q2 = True
            st.success("✅ FAUX (Quotidien)")
        st.markdown("---")

        st.subheader("3. Niveau eau à chaque poste ?")
        c5, c6 = st.columns(2)
        if c5.button("VRAI", key="vf3_v"): st.error("❌ FAUX")
        if c6.button("FAUX", key="vf3_f") or st.session_state.verif_q3:
            st.session_state.verif_q3 = True
            st.success("✅ FAUX (Hebdo)")
        st.markdown("---")

        st.subheader("4. Fumer en chargeant ?")
        c7, c8 = st.columns(2)
        if c7.button("VRAI", key="vf4_v"): st.error("💥 DANGER !")
        if c8.button("FAUX", key="vf4_f") or st.session_state.verif_q4:
            st.session_state.verif_q4 = True
            st.success("✅ FAUX")
        st.markdown("---")

        st.subheader("5. Attendre fin poste si panne ?")
        c9, c10 = st.columns(2)
        if c9.button("VRAI", key="vf5_v"): st.error("❌ NON")
        if c10.button("FAUX", key="vf5_f") or st.session_state.verif_q5:
            st.session_state.verif_q5 = True
            st.success("✅ FAUX (Arrêt immédiat)")

    # --- MODULE 9 : PICTOGRAMMES ---
    elif menu_485 == "9. Pictogrammes (Auto-Test)":
        st.header("🛑 Pictogrammes")
        st.write("Trouvez la bonne correspondance.")
        try: st.image("images/quizz_pictogrammes.png", use_column_width=True)
        except: st.error("⚠️ Manque: quizz_pictogrammes.png")
        
        for i in range(1, 11): init_state(f"pic_q{i}")
        st.markdown("---")

        quiz_data = [
            ("1. Toxique ?", "D (Tête de mort)"),
            ("2. Centre de gravité ?", "E (Cible)"),
            ("3. Fragile ?", "C (Verre)"),
            ("4. Ne pas empiler ?", "A (Boîte barrée)"),
            ("5. Gaz sous pression ?", "B (Bouteille)"),
            ("6. Interdit chariots ?", "D (Rond rouge)"),
            ("7. Passage Piétons ?", "A (Rond bleu)"),
            ("8. Vitesse mini ?", "C (30)"),
            ("9. Premiers secours ?", "E (Croix verte)"),
            ("10. Lance incendie ?", "B (Carré rouge)")
        ]
        
        for i, (q_txt, rep) in enumerate(quiz_data):
            st.write(f"**{q_txt}**")
            k_suffix = f"p{i+1}"
            
            c1, c2, c3 = st.columns(3)
            # Bouton 1 (Faux)
            if c1.button("Mauvais", key=f"{k_suffix}_bad1"): st.error("❌ Non")
            # Bouton 2 (Bon)
            if c2.button(rep, key=f"{k_suffix}_good") or st.session_state[f"pic_q{i+1}"]:
                st.session_state[f"pic_q{i+1}"] = True
                st.success("✅ VRAI")
            # Bouton 3 (Faux)
            if c3.button("Autre", key=f"{k_suffix}_bad2"): st.error("❌ Non")
            st.markdown("---")

# ==============================================================================
# AUTRES LIVRETS
# ==============================================================================
else:
    st.title(f"🚧 {livret}")
    st.info("Module en construction.")
