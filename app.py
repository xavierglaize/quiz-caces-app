import streamlit as st
from PIL import Image

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
# ZONE R.485 (GERBEURS)
# ==============================================================================
if livret == "CACES R.485 (Gerbeurs)":
    
    # LISTE DES MODULES (Mise à jour avec 13 modules)
    menu_485 = st.sidebar.radio("Modules R.485 :", 
        ["Accueil R.485", 
         "1. Catégories (p.12)", 
         "2. Technique (p.23)", 
         "3. Stabilité (p.34)", 
         "4. Conduite (p.54)", 
         "5. Signalisation (p.58)", 
         "6. Organes (Auto-Test)", 
         "7. Acteurs (Auto-Test)",
         "8. Causes Accidents (Auto-Test)",
         "9. Réglementation (Vrai/Faux)",
         "10. Vérifications (Vrai/Faux)",
         "11. Gerbage (Vrai/Faux)",
         "12. Circulation (Vrai/Faux)",
         "13. Pictogrammes (Auto-Test)"])

    # --- ACCUEIL ---
    if menu_485 == "Accueil R.485":
        st.title("🏗️ Formation Gerbeurs R.485")
        st.info("Bienvenue. Ce module utilise la méthode de la **Photo Mentale**.")
        st.write("Les réponses correctes resteront affichées pour faciliter votre mémorisation.")

    # --- MODULE 1 : CATÉGORIES ---
    elif menu_485 == "1. Catégories (p.12)":
        st.header("🔍 Quiz : Reconnaissance des Engins")
        init_state("cat_q1"); init_state("cat_q2"); init_state("cat_q3"); init_state("cat_q4")

        col1, col2 = st.columns(2)
        with col1:
            st.warning("🖼️ [IMAGE GERBEUR JAUNE]") 
            if st.button("Est-ce un R.485 ? (1)") or st.session_state.cat_q1:
                st.session_state.cat_q1 = True
                st.success("✅ OUI (Catégorie 1 ou 2)")
            st.markdown("---")
            st.warning("🖼️ [IMAGE GERBEUR ORANGE]")
            if st.button("Est-ce un R.485 ? (3)") or st.session_state.cat_q3:
                st.session_state.cat_q3 = True
                st.success("✅ OUI (Catégorie 1 ou 2)")

        with col2:
            st.info("🖼️ [IMAGE TRANSPALETTE]")
            if st.button("Est-ce un R.485 ? (2)") or st.session_state.cat_q2:
                st.session_state.cat_q2 = True
                st.error("❌ NON (R.366 - Transpalette)")
            st.markdown("---")
            st.error("🖼️ [IMAGE CHARIOT PORTÉ]")
            if st.button("Est-ce un R.485 ? (4)") or st.session_state.cat_q4:
                st.session_state.cat_q4 = True
                st.error("❌ NON (R.489 - Porté)")

    # --- MODULE 2 : TECHNIQUE ---
    elif menu_485 == "2. Technique (p.23)":
        st.header("⚡ Technique & Batteries")
        init_state("tech_bat")
        st.write("❓ **Question : Peut-on fumer en chargeant une batterie Plomb Ouvert ?**")
        c1, c2 = st.columns(2)
        if c1.button("OUI (si fenêtre ouverte)"): st.error("💥 BOUM ! Explosion.")
        if c2.button("NON (Jamais)") or st.session_state.tech_bat:
            st.session_state.tech_bat = True
            st.success("✅ BRAVO. Interdiction formelle.")

    # --- MODULE 3 : STABILITÉ ---
    elif menu_485 == "3. Stabilité (p.34)":
        st.header("⚖️ Exercice : Plaques de Charge")
        st.write("Analysez les documents pour répondre (Réponses p.59).")
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
            if st.button("4300 mm", key="btn_q1_b"):
                st.error("❌ Non")
            st.write("---")
            st.markdown("#### 2. Poids max ?")
            st.write("À **4300 mm** (Charge longue) :")
            if st.button("330 kg", key="btn_q2_a") or st.session_state.plaque_q2:
                st.session_state.plaque_q2 = True
                st.success("✅ 330 kg")
            if st.button("550 kg", key="btn_q2_b"):
                st.error("❌ Non")
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
            if st.button("4224 mm", key="btn_q3_b"):
                st.error("❌ Trop haut")
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
            if st.button("1556kg à 300mm", key="btn_q4_b"):
                st.error("❌ Non")

    # --- MODULE 4 : CONDUITE ---
    elif menu_485 == "4. Conduite (p.54)":
        st.header("🚦 Règles de Conduite")
        init_state("cond_q1"); init_state("cond_q2")
        
        st.write("**1. Distance de sécurité entre 2 gerbeurs ?**")
        c1, c2 = st.columns(2)
        if c1.button("1 mètre"): st.error("❌ Trop près !")
        if c2.button("3 gerbeurs") or st.session_state.cond_q1:
            st.session_state.cond_q1 = True
            st.success("✅ CORRECT")
        st.markdown("---")
        
        st.write("**2. Dans une pente, la charge doit être...**")
        c3, c4 = st.columns(2)
        if c3.button("Vers le bas (Aval)"): st.error("❌ DANGER !")
        if c4.button("Vers l'AMONT (Haut)") or st.session_state.cond_q2:
            st.session_state.cond_q2 = True
            st.success("✅ CORRECT")

    # --- MODULE 5 : SIGNALISATION ---
    elif menu_485 == "5. Signalisation (p.58)":
        st.header("🚧 Panneaux")
        st.write("Cliquez pour révéler la signification.")
        init_state("sig_tox"); init_state("sig_epi")
        
        c1, c2 = st.columns(2)
        with c1:
            st.write("☠️ **Tête de Mort**")
            if st.button("Révéler ##1") or st.session_state.sig_tox:
                st.session_state.sig_tox = True
                st.success("✅ TOXIQUE")
        with c2:
            st.write("🔵 **Rond Bleu (Chaussure)**")
            if st.button("Révéler ##2") or st.session_state.sig_epi:
                st.session_state.sig_epi = True
                st.success("✅ OBLIGATION EPI")

    # --- MODULE 6 : ORGANES ---
    elif menu_485 == "6. Organes (Auto-Test)":
        st.header("🔧 Identification des Organes")
        init_state("org_q1"); init_state("org_q2"); init_state("org_q3"); init_state("org_q4"); init_state("org_q5")

        st.markdown("---")
        col1, col2 = st.columns([1, 2])
        with col1:
            try: st.image("Image1.png", use_column_width=True)
            except: st.error("Manque Image1.png")
        with col2:
            st.markdown("#### 1. Quel est cet élément ?")
            if st.button("Dispositif de condamnation", key="btn_o1_a"): st.error("❌ Non")
            if st.button("Commande anti-écrasement", key="btn_o1_b") or st.session_state.org_q1:
                st.session_state.org_q1 = True
                st.success("✅ EXACT (Sécurité ventrale)")
            if st.button("Avertisseur sonore", key="btn_o1_c"): st.error("❌ Non")
        st.markdown("---")

        col3, col4 = st.columns([1, 2])
        with col3:
            try: st.image("Image2.png", use_column_width=True)
            except: st.error("Manque Image2.png")
        with col4:
            st.markdown("#### 2. Quel est cet élément ?")
            if st.button("Digicode / Clé", key="btn_o2_a") or st.session_state.org_q2:
                st.session_state.org_q2 = True
                st.success("✅ EXACT (Condamnation)")
            if st.button("Sélecteur de programme", key="btn_o2_b"): st.error("❌ Non")
            if st.button("Indicateur de décharge", key="btn_o2_c"): st.error("❌ Non")
        st.markdown("---")

        col5, col6 = st.columns([1, 2])
        with col5:
            try: st.image("Image3.png", use_column_width=True)
            except: st.error("Manque Image3.png")
        with col6:
            st.markdown("#### 3. Quel est cet élément ?")
            if st.button("Roue directrice", key="btn_o3_a"): st.error("❌ Non")
            if st.button("Galet porteur", key="btn_o3_b"): st.error("❌ Non")
            if st.button("Roue stabilisatrice", key="btn_o3_c") or st.session_state.org_q3:
                st.session_state.org_q3 = True
                st.success("✅ EXACT (Stabilité)")
        st.markdown("---")

        col7, col8 = st.columns([1, 2])
        with col7:
            try: st.image("Image4.png", use_column_width=True)
            except: st.error("Manque Image4.png")
        with col8:
            st.markdown("#### 4. Bouton Tortue ?")
            if st.button("Vitesse lente (Timon vertical)", key="btn_o4_a") or st.session_state.org_q4:
                st.session_state.org_q4 = True
                st.success("✅ EXACT")
            if st.button("Klaxon", key="btn_o4_b"): st.error("❌ Non")
            if st.button("Levée", key="btn_o4_c"): st.error("❌ Non")
        st.markdown("---")

        col9, col10 = st.columns([1, 2])
        with col9:
            try: st.image("Image5.png", use_column_width=True)
            except: st.error("Manque Image5.png")
        with col10:
            st.markdown("#### 5. Quel est cet élément ?")
            if st.button("Roue directrice", key="btn_o5_a") or st.session_state.org_q5:
                st.session_state.org_q5 = True
                st.success("✅ EXACT (Motrice)")
            if st.button("Roue stabilisatrice", key="btn_o5_b"): st.error("❌ Non")
            if st.button("Roue libre", key="btn_o5_c"): st.error("❌ Non")

    # --- MODULE 7 : ACTEURS ---
    elif menu_485 == "7. Acteurs (Auto-Test)":
        st.header("🤝 Les Acteurs de la Prévention")
        init_state("act_q1"); init_state("act_q2"); init_state("act_q3"); init_state("act_q4"); init_state("act_q5")
        st.markdown("---")

        st.subheader("1. Droit d'entrée partout ?")
        c1, c2 = st.columns([2, 1])
        with c1:
            if st.button("La CARSAT", key="btn_a1_a"): st.error("❌ Non")
            if st.button("L'Inspecteur du Travail", key="btn_a1_b") or st.session_state.act_q1:
                st.session_state.act_q1 = True
                st.success("✅ EXACT")
                try: st.image("Acteur_Inspecteur.png", width=150)
                except: st.write("Manque img")
            if st.button("Le Fabricant", key="btn_a1_c"): st.error("❌ Non")
        st.markdown("---")

        st.subheader("2. Responsable Marquage CE ?")
        c3, c4 = st.columns([2, 1])
        with c3:
            if st.button("Le Chef d'équipe", key="btn_a2_a"): st.error("❌ Non")
            if st.button("Le Fabricant", key="btn_a2_b") or st.session_state.act_q2:
                st.session_state.act_q2 = True
                st.success("✅ EXACT")
                try: st.image("Acteur_Fabricant.png", width=150)
                except: st.write("Manque img")
            if st.button("L'Inspecteur", key="btn_a2_c"): st.error("❌ Non")
        st.markdown("---")

        st.subheader("3. Organisme Prévention (Assurance) ?")
        c5, c6 = st.columns([2, 1])
        with c5:
            if st.button("Le CSE", key="btn_a3_a"): st.error("❌ Non")
            if st.button("La CARSAT", key="btn_a3_b") or st.session_state.act_q3:
                st.session_state.act_q3 = True
                st.success("✅ EXACT")
                try: st.image("Acteur_CARSAT.png", width=150)
                except: st.write("Manque img")
        st.markdown("---")

        st.subheader("4. Enquêtes après accident ?")
        c7, c8 = st.columns([2, 1])
        with c7:
            if st.button("Le CSE / CSSCT", key="btn_a4_a") or st.session_state.act_q4:
                st.session_state.act_q4 = True
                st.success("✅ EXACT")
                try: st.image("Acteur_CSE.png", width=150)
                except: st.write("Manque img")
            if st.button("Médecine du travail", key="btn_a4_b"): st.error("❌ Non")
        st.markdown("---")

        st.subheader("5. Responsable sécurité entreprise ?")
        c9, c10 = st.columns([2, 1])
        with c9:
            if st.button("Le Fabricant", key="btn_a5_a"): st.error("❌ Non")
            if st.button("L'employeur / Personnel", key="btn_a5_b") or st.session_state.act_q5:
                st.session_state.act_q5 = True
                st.success("✅ EXACT")
                try: st.image("Acteur_Personnel.png", width=150)
                except: st.write("Manque img")

    # --- MODULE 8 : CAUSES ACCIDENTS ---
    elif menu_485 == "8. Causes Accidents (Auto-Test)":
        st.header("⚠️ Causes d'accidents")
        st.write("Classez la cause : **Conducteur**, **Matériel** ou **Environnement** ?")
        for i in range(1, 11): init_state(f"cause_q{i}")
        st.markdown("---")

        st.markdown("#### 1. Mauvais positionnement des bras")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c1") or st.session_state.cause_q1:
            st.session_state.cause_q1 = True
            st.success("✅ CORRECT")
        if c2.button("Matériel", key="m1"): st.error("❌ Non")
        if c3.button("Environnement", key="e1"): st.error("❌ Non")
        st.markdown("---")

        st.markdown("#### 2. Mauvaise stabilisation")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c2") or st.session_state.cause_q2:
            st.session_state.cause_q2 = True
            st.success("✅ CORRECT")
        if c2.button("Matériel", key="m2"): st.error("❌ Non")
        if c3.button("Environnement", key="e2"): st.error("❌ Non")
        st.markdown("---")

        st.markdown("#### 3. Problème de direction")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c3"): st.error("❌ Non")
        if c2.button("Matériel", key="m3") or st.session_state.cause_q3:
            st.session_state.cause_q3 = True
            st.success("✅ CORRECT")
        if c3.button("Environnement", key="e3"): st.error("❌ Non")
        st.markdown("---")

        st.markdown("#### 4. Manque de visibilité (éclairage/obstacles)")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c4"): st.error("❌ Non")
        if c2.button("Matériel", key="m4"): st.error("❌ Non")
        if c3.button("Environnement", key="e4") or st.session_state.cause_q4:
            st.session_state.cause_q4 = True
            st.success("✅ CORRECT")
        st.markdown("---")

        st.markdown("#### 5. Trou dans le sol")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c5"): st.error("❌ Non")
        if c2.button("Matériel", key="m5"): st.error("❌ Non")
        if c3.button("Environnement", key="e5") or st.session_state.cause_q5:
            st.session_state.cause_q5 = True
            st.success("✅ CORRECT")
        st.markdown("---")

        st.markdown("#### 6. Vitesse excessive")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c6") or st.session_state.cause_q6:
            st.session_state.cause_q6 = True
            st.success("✅ CORRECT")
        if c2.button("Matériel", key="m6"): st.error("❌ Non")
        if c3.button("Environnement", key="e6"): st.error("❌ Non")
        st.markdown("---")

        st.markdown("#### 7. Roue défectueuse")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c7"): st.error("❌ Non")
        if c2.button("Matériel", key="m7") or st.session_state.cause_q7:
            st.session_state.cause_q7 = True
            st.success("✅ CORRECT")
        if c3.button("Environnement", key="e7"): st.error("❌ Non")
        st.markdown("---")

        st.markdown("#### 8. Mauvaise évaluation des charges")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c8") or st.session_state.cause_q8:
            st.session_state.cause_q8 = True
            st.success("✅ CORRECT")
        if c2.button("Matériel", key="m8"): st.error("❌ Non")
        if c3.button("Environnement", key="e8"): st.error("❌ Non")
        st.markdown("---")

        st.markdown("#### 9. Stockage dangereux (instable)")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c9"): st.error("❌ Non")
        if c2.button("Matériel", key="m9"): st.error("❌ Non")
        if c3.button("Environnement", key="e9") or st.session_state.cause_q9:
            st.session_state.cause_q9 = True
            st.success("✅ CORRECT")
        st.markdown("---")

        st.markdown("#### 10. Problème de frein")
        c1, c2, c3 = st.columns(3)
        if c1.button("Conducteur", key="c10"): st.error("❌ Non")
        if c2.button("Matériel", key="m10") or st.session_state.cause_q10:
            st.session_state.cause_q10 = True
            st.success("✅ CORRECT")
        if c3.button("Environnement", key="e10"): st.error("❌ Non")

    # --- MODULE 9 : RÉGLEMENTATION ---
    elif menu_485 == "9. Réglementation (Vrai/Faux)":
        st.header("📋 Réglementation & Responsabilités")
        init_state("reg_q1"); init_state("reg_q2"); init_state("reg_q3"); init_state("reg_q4"); init_state("reg_q5")
        st.markdown("---")

        st.subheader("1. Formation")
        st.write("🏗️ **« L'employeur a l'obligation de former ses salariés. »**")
        c1, c2 = st.columns(2)
        if c1.button("VRAI", key="rg1_v") or st.session_state.reg_q1:
            st.session_state.reg_q1 = True
            st.success("✅ VRAI (Obligation légale)")
        if c2.button("FAUX", key="rg1_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("2. Responsabilité Matériel")
        st.write("🔧 **« Le cariste est responsable du matériel. »**")
        c3, c4 = st.columns(2)
        if c3.button("VRAI", key="rg2_v") or st.session_state.reg_q2:
            st.session_state.reg_q2 = True
            st.success("✅ VRAI")
        if c4.button("FAUX", key="rg2_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("3. Autorisation de Conduite")
        st.write("📄 **« Délivrée par l'organisme de formation ? »**")
        c5, c6 = st.columns(2)
        if c5.button("VRAI", key="rg3_v"): st.error("❌ FAUX ! C'est l'EMPLOYEUR.")
        if c6.button("FAUX", key="rg3_f") or st.session_state.reg_q3:
            st.session_state.reg_q3 = True
            st.success("✅ FAUX (CACES = Organisme / Autorisation = Employeur)")
        st.markdown("---")

        st.subheader("4. Âge Minimum")
        st.write("🔞 **« 18 ans minimum ? »**")
        c7, c8 = st.columns(2)
        if c7.button("VRAI", key="rg4_v") or st.session_state.reg_q4:
            st.session_state.reg_q4 = True
            st.success("✅ VRAI")
        if c8.button("FAUX", key="rg4_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("5. Conducteur Occasionnel")
        st.write("👷 **« Pas de formation pour un occasionnel ? »**")
        c9, c10 = st.columns(2)
        if c9.button("VRAI", key="rg5_v"): st.error("❌ FAUX ! Formation OBLIGATOIRE.")
        if c10.button("FAUX", key="rg5_f") or st.session_state.reg_q5:
            st.session_state.reg_q5 = True
            st.success("✅ FAUX")

    # --- MODULE 10 : VÉRIFICATIONS ---
    elif menu_485 == "10. Vérifications (Vrai/Faux)":
        st.header("🔍 Vérifications & Entretien")
        init_state("verif_q1"); init_state("verif_q2"); init_state("verif_q3"); init_state("verif_q4"); init_state("verif_q5")
        st.markdown("---")

        st.subheader("1. VGP")
        st.write("📅 **« VGP tous les 6 mois ? »**")
        c1, c2 = st.columns(2)
        if c1.button("VRAI", key="vf1_v") or st.session_state.verif_q1:
            st.session_state.verif_q1 = True
            st.success("✅ VRAI (Obligatoire)")
        if c2.button("FAUX", key="vf1_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("2. Carnet d'entretien")
        st.write("📘 **« Je consulte le carnet d'entretien 1 fois par semaine ? »**")
        c3, c4 = st.columns(2)
        if c3.button("VRAI", key="vf2_v"): st.error("❌ FAUX.")
        if c4.button("FAUX", key="vf2_f") or st.session_state.verif_q2:
            st.session_state.verif_q2 = True
            st.success("✅ FAUX (Quotidien)")
        st.markdown("---")

        st.subheader("3. Niveau Électrolyte")
        st.write("🔋 **« Contrôle niveau d'eau à chaque poste ? »**")
        c5, c6 = st.columns(2)
        if c5.button("VRAI", key="vf3_v"): st.error("❌ FAUX.")
        if c6.button("FAUX", key="vf3_f") or st.session_state.verif_q3:
            st.session_state.verif_q3 = True
            st.success("✅ FAUX (Hebdomadaire)")
        st.markdown("---")

        st.subheader("4. Recharge Batterie")
        st.write("🚬 **« Fumer en chargeant si aéré ? »**")
        c7, c8 = st.columns(2)
        if c7.button("VRAI", key="vf4_v"): st.error("💥 DANGER !")
        if c8.button("FAUX", key="vf4_f") or st.session_state.verif_q4:
            st.session_state.verif_q4 = True
            st.success("✅ FAUX")
        st.markdown("---")

        st.subheader("5. Panne")
        st.write("🛑 **« Attendre fin de poste pour signaler panne ? »**")
        c9, c10 = st.columns(2)
        if c9.button("VRAI", key="vf5_v"): st.error("❌ NON !")
        if c10.button("FAUX", key="vf5_f") or st.session_state.verif_q5:
            st.session_state.verif_q5 = True
            st.success("✅ FAUX (Arrêt immédiat)")

    # --- MODULE 11 : GERBAGE ---
    elif menu_485 == "11. Gerbage (Vrai/Faux)":
        st.header("📦 Gerbage & Chargement")
        init_state("gerb_q1"); init_state("gerb_q2"); init_state("gerb_q3"); init_state("gerb_q4"); init_state("gerb_q5")
        st.markdown("---")

        st.subheader("1. Stabilité Pile")
        st.write("📦 **« Le plus lourd EN BAS. »**")
        c1, c2 = st.columns(2)
        if c1.button("VRAI", key="gb1_v") or st.session_state.gerb_q1:
            st.session_state.gerb_q1 = True
            st.success("✅ VRAI")
        if c2.button("FAUX", key="gb1_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("2. Contrôle Palettier")
        st.write("👀 **« PAS au conducteur de vérifier l'état ? »**")
        c3, c4 = st.columns(2)
        if c3.button("VRAI", key="gb2_v"): st.error("❌ FAUX ! Responsabilité cariste.")
        if c4.button("FAUX", key="gb2_f") or st.session_state.gerb_q2:
            st.session_state.gerb_q2 = True
            st.success("✅ FAUX")
        st.markdown("---")

        st.subheader("3. Poids")
        st.write("⚖️ **« Connaître le poids AVANT. »**")
        c5, c6 = st.columns(2)
        if c5.button("VRAI", key="gb3_v") or st.session_state.gerb_q3:
            st.session_state.gerb_q3 = True
            st.success("✅ VRAI")
        if c6.button("FAUX", key="gb3_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("4. Pont de liaison")
        st.write("🚚 **« Vérifier capacité du pont ? »**")
        c7, c8 = st.columns(2)
        if c7.button("VRAI", key="gb4_v") or st.session_state.gerb_q4:
            st.session_state.gerb_q4 = True
            st.success("✅ VRAI")
        if c8.button("FAUX", key="gb4_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("5. Capacité Palettier")
        st.write("🏗️ **« Contrôler capacité avant de poser. »**")
        c9, c10 = st.columns(2)
        if c9.button("VRAI", key="gb5_v") or st.session_state.gerb_q5:
            st.session_state.gerb_q5 = True
            st.success("✅ VRAI")
        if c10.button("FAUX", key="gb5_f"): st.error("❌ Erreur")

    # --- MODULE 12 : CIRCULATION ---
    elif menu_485 == "12. Circulation (Vrai/Faux)":
        st.header("🚦 Règles de Circulation")
        init_state("circ_q1"); init_state("circ_q2"); init_state("circ_q3"); init_state("circ_q4"); init_state("circ_q5")
        st.markdown("---")

        st.subheader("1. Charge en hauteur")
        st.write("📦 **« Je ne dois pas circuler avec une charge en hauteur. »**")
        c1, c2 = st.columns(2)
        if c1.button("VRAI", key="cr1_v") or st.session_state.circ_q1:
            st.session_state.circ_q1 = True
            st.success("✅ VRAI")
        if c2.button("FAUX", key="cr1_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("2. Transport de personnes")
        st.write("👥 **« Autorisé si le chef demande ? »**")
        c3, c4 = st.columns(2)
        if c3.button("VRAI", key="cr2_v"): st.error("❌ FAUX !")
        if c4.button("FAUX", key="cr2_f") or st.session_state.circ_q2:
            st.session_state.circ_q2 = True
            st.success("✅ FAUX")
        st.markdown("---")

        st.subheader("3. Arrêt temporaire")
        st.write("🛑 **« Arrêt = Fourches au sol ? »**")
        c5, c6 = st.columns(2)
        if c5.button("VRAI", key="cr3_v") or st.session_state.circ_q3:
            st.session_state.circ_q3 = True
            st.success("✅ VRAI")
        if c6.button("FAUX", key="cr3_f"): st.error("❌ Erreur")
        st.markdown("---")

        st.subheader("4. Téléphone")
        st.write("📱 **« Autorisé si je roule lentement ? »**")
        c7, c8 = st.columns(2)
        if c7.button("VRAI", key="cr4_v"): st.error("❌ NON !")
        if c8.button("FAUX", key="cr4_f") or st.session_state.circ_q4:
            st.session_state.circ_q4 = True
            st.success("✅ FAUX")
        st.markdown("---")

        st.subheader("5. Distance")
        st.write("↔️ **« Distance = 3 gerbeurs ? »**")
        c9, c10 = st.columns(2)
        if c9.button("VRAI", key="cr5_v") or st.session_state.circ_q5:
            st.session_state.circ_q5 = True
            st.success("✅ VRAI")
        if c10.button("FAUX", key="cr5_f"): st.error("❌ Erreur")

    # --- MODULE 13 : PICTOGRAMMES (NOUVEAU) ---
    elif menu_485 == "13. Pictogrammes (Auto-Test)":
        st.header("🛑 Pictogrammes & Panneaux")
        st.write("Regardez le document ci-dessous et trouvez la bonne correspondance.")
        
        try: st.image("quizz_pictogrammes.png", use_column_width=True)
        except: st.error("⚠️ Manque l'image 'quizz_pictogrammes.png'")
        
        for i in range(1, 11): init_state(f"pic_q{i}")
        st.markdown("---")

        st.subheader("PARTIE 1 : Étiquettes")
        
        # Q1
        st.write("☠️ **1. Toxique ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("A (Croix colis)", key="p1_a"): st.error("❌ Non")
        if c2.button("D (Tête de mort)", key="p1_d") or st.session_state.pic_q1:
             st.session_state.pic_q1 = True
             st.success("✅ VRAI")
        if c3.button("C (Verre)", key="p1_c"): st.error("❌ Non")
        st.markdown("---")

        # Q2
        st.write("🎯 **2. Centre de gravité ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("E (Cible/Rond)", key="p2_e") or st.session_state.pic_q2:
             st.session_state.pic_q2 = True
             st.success("✅ VRAI")
        if c2.button("B (Gaz)", key="p2_b"): st.error("❌ Non")
        if c3.button("A (Croix)", key="p2_a"): st.error("❌ Non")
        st.markdown("---")
        
        # Q3
        st.write("🍷 **3. Fragile ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("C (Verre)", key="p3_c") or st.session_state.pic_q3:
             st.session_state.pic_q3 = True
             st.success("✅ VRAI")
        if c2.button("E (Cible)", key="p3_e"): st.error("❌ Non")
        if c3.button("D (Tête mort)", key="p3_d"): st.error("❌ Non")
        st.markdown("---")

        # Q4
        st.write("📦 **4. Ne pas empiler ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("A (Boîte barrée)", key="p4_a") or st.session_state.pic_q4:
             st.session_state.pic_q4 = True
             st.success("✅ VRAI")
        if c2.button("B (Gaz)", key="p4_b"): st.error("❌ Non")
        if c3.button("C (Verre)", key="p4_c"): st.error("❌ Non")
        st.markdown("---")

        # Q5
        st.write("🧨 **5. Gaz sous pression ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("B (Bouteille gaz)", key="p5_b") or st.session_state.pic_q5:
             st.session_state.pic_q5 = True
             st.success("✅ VRAI")
        if c2.button("A (Boîte)", key="p5_a"): st.error("❌ Non")
        if c3.button("E (Cible)", key="p5_e"): st.error("❌ Non")
        st.markdown("---")

        st.subheader("PARTIE 2 : Panneaux")

        # Q6
        st.write("🚜 **1. Interdit aux chariots ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("D (Rond rouge chariot)", key="p6_d") or st.session_state.pic_q6:
             st.session_state.pic_q6 = True
             st.success("✅ VRAI")
        if c2.button("C (30)", key="p6_c"): st.error("❌ Non")
        if c3.button("A (Piéton)", key="p6_a"): st.error("❌ Non")
        st.markdown("---")

        # Q7
        st.write("🚶 **2. Passage Piétons Obligatoire ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("A (Rond bleu piéton)", key="p7_a") or st.session_state.pic_q7:
             st.session_state.pic_q7 = True
             st.success("✅ VRAI")
        if c2.button("D (Interdit)", key="p7_d"): st.error("❌ Non")
        if c3.button("E (Secours)", key="p7_e"): st.error("❌ Non")
        st.markdown("---")

        # Q8
        st.write("⚡ **3. Vitesse minimale ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("C (Rond bleu 30)", key="p8_c") or st.session_state.pic_q8:
             st.session_state.pic_q8 = True
             st.success("✅ VRAI")
        if c2.button("B (Incendie)", key="p8_b"): st.error("❌ Non")
        if c3.button("A (Piéton)", key="p8_a"): st.error("❌ Non")
        st.markdown("---")

        # Q9
        st.write("💚 **4. Premiers secours ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("E (Croix verte)", key="p9_e") or st.session_state.pic_q9:
             st.session_state.pic_q9 = True
             st.success("✅ VRAI")
        if c2.button("D (Interdit)", key="p9_d"): st.error("❌ Non")
        if c3.button("B (Incendie)", key="p9_b"): st.error("❌ Non")
        st.markdown("---")

        # Q10
        st.write("🔥 **5. Lance à incendie ?**")
        c1, c2, c3 = st.columns(3)
        if c1.button("B (Carré rouge)", key="p10_b") or st.session_state.pic_q10:
             st.session_state.pic_q10 = True
             st.success("✅ VRAI")
        if c2.button("C (30)", key="p10_c"): st.error("❌ Non")
        if c3.button("E (Secours)", key="p10_e"): st.error("❌ Non")

# ==============================================================================
# AUTRES LIVRETS
# ==============================================================================
else:
    st.title(f"🚧 {livret}")
    st.info("Module en construction.")
