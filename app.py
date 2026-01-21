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
    
   menu_485 = st.sidebar.radio("Modules R.485 :", 
        ["Accueil R.485", "1. Catégories (p.12)", "2. Technique (p.23)", 
         "3. Stabilité (p.34)", "4. Conduite (p.54)", "5. Signalisation (p.58)", "6. Organes (Auto-Test)"])

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
            st.warning("🖼️ [IMAGE GERBEUR JAUNE]") # Remplacer par st.image("votre_image.jpg")
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

    # --- MODULE 3 : STABILITÉ (VERSION PLAQUES [3,1]) ---
    elif menu_485 == "3. Stabilité (p.34)":
        st.header("⚖️ Exercice : Plaques de Charge")
        st.write("Analysez les documents pour répondre (Réponses p.59).")
        
        # Initialisation des mémoires
        init_state("plaque_q1"); init_state("plaque_q2"); init_state("plaque_q3"); init_state("plaque_q4")

        st.markdown("---")

        # BLOC 1 : TABLEAU DU HAUT
        col_img1, col_txt1 = st.columns([3, 1])
        with col_img1:
            try: st.image("quizz_plaque_de_charge_gerbeur_haut.png", use_column_width=True)
            except: st.error("⚠️ Image 'quizz_plaque_de_charge_gerbeur_haut.png' manquante.")
        with col_txt1:
            st.markdown("#### 1. Hauteur max ?")
            st.write("Pour **630 kg** (L=1200mm) :")
            if st.button("4000 mm", key="btn_q1_a") or st.session_state.plaque_q1:
                st.session_state.plaque_q1 = True
                st.success("✅ 4000 mm")
            if st.button("4300 mm", key="btn_q1_b"):
                st.error("❌ Non (Max 550kg)")
            st.write("---")
            st.markdown("#### 2. Poids max ?")
            st.write("À **4300 mm** (Charge longue) :")
            if st.button("330 kg", key="btn_q2_a") or st.session_state.plaque_q2:
                st.session_state.plaque_q2 = True
                st.success("✅ 330 kg")
            if st.button("550 kg", key="btn_q2_b"):
                st.error("❌ Non")
        st.markdown("---")

        # BLOC 2 : GRAPHIQUE DU MILIEU
        col_img2, col_txt2 = st.columns([3, 1])
        with col_img2:
            try: st.image("quizz_plaque_de_charge_gerbeur_milieu.png", use_column_width=True)
            except: st.error("⚠️ Image 'quizz_plaque_de_charge_gerbeur_milieu.png' manquante.")
        with col_txt2:
            st.markdown("#### 3. Graphique")
            st.write("**1400 kg** à **400 mm**. Hauteur ?")
            if st.button("3884 mm", key="btn_q3_a") or st.session_state.plaque_q3:
                st.session_state.plaque_q3 = True
                st.success("✅ 3884 mm")
            if st.button("4224 mm", key="btn_q3_b"):
                st.error("❌ Trop haut !")
        st.markdown("---")

        # BLOC 3 : PLAQUE DU BAS
        col_img3, col_txt3 = st.columns([3, 1])
        with col_img3:
            try: st.image("quizz_plaque_de_charge_gerbeur_bas.png", use_column_width=True)
            except: st.error("⚠️ Image 'quizz_plaque_de_charge_gerbeur_bas.png' manquante.")
        with col_txt3:
            st.markdown("#### 4. Constructeur")
            st.write("Je peux déplacer :")
            if st.button("1200kg à 600mm", key="btn_q4_a") or st.session_state.plaque_q4:
                st.session_state.plaque_q4 = True
                st.success("✅ EXACT")
            if st.button("1556kg à 300mm", key="btn_q4_b"):
                st.error("❌ Non (Poids à vide)")

# --- MODULE 4 : CONDUITE ---
    elif menu_485 == "4. Conduite (p.54)":
        st.header("🚦 Règles de Conduite")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**1. Distance de sécurité entre 2 gerbeurs ?**")
            if st.button("1 mètre"): st.error("❌ Trop près !")
            if st.button("3 gerbeurs"): st.success("✅ CORRECT (env. 3 à 5m)")
            
        with col2:
            st.write("**2. Dans une pente, la charge doit être...**")
            if st.button("Vers le bas (Aval)"): st.error("❌ La charge risque de glisser !")
            if st.button("Vers le haut (Amont)"): st.success("✅ CORRECT (Pour la plaquer au dosseret)")

    # --- MODULE 5 : SIGNALISATION ---
    elif menu_485 == "5. Signalisation (p.58)":
        st.header("🚧 Panneaux")
        st.write("Reliez le panneau à sa signification.")
        
        c1, c2 = st.columns(2)
        with c1:
            st.write("☠️ **Tête de Mort**")
            if st.button("Toxique"): st.success("✅ VRAI")
            if st.button("Mortel"): st.warning("⚠️ C'est 'Toxique' le terme exact.")
            
        with c2:
            st.write("🔵 **Rond Bleu (Chaussure)**")
            if st.button("Conseillé"): st.error("❌ Bleu = OBLIGATION")
            if st.button("Obligatoire"): st.success("✅ VRAI (EPI)")
    # --- MODULE 6 : ORGANES & COMMANDES (NOUVEAU) ---
    elif menu_485 == "6. Organes (Auto-Test)":
        st.header("🔧 Identification des Organes")
        st.write("Reliez la photo à la bonne définition.")
        
        # Initialisation des mémoires
        init_state("org_q1"); init_state("org_q2"); init_state("org_q3"); init_state("org_q4"); init_state("org_q5")

        st.markdown("---")

        # --- IMAGE 1 (Anti-écrasement) ---
        col1, col2 = st.columns([1, 2])
        with col1:
            try: st.image("Image1.png", use_column_width=True)
            except: st.error("Manque Image1.png")
        with col2:
            st.markdown("#### 1. Quel est cet élément ?")
            if st.button("Dispositif de condamnation", key="btn_o1_a"):
                st.error("❌ Non. Ça c'est la clé ou le digicode.")
            if st.button("Commande anti-écrasement", key="btn_o1_b") or st.session_state.org_q1:
                st.session_state.org_q1 = True
                st.success("✅ EXACT (Sécurité ventrale)")
            if st.button("Avertisseur sonore", key="btn_o1_c"):
                st.error("❌ Non. C'est le bouton rouge au bout.")

        st.markdown("---")

        # --- IMAGE 2 (Digicode) ---
        col3, col4 = st.columns([1, 2])
        with col3:
            try: st.image("Image2.png", use_column_width=True)
            except: st.error("Manque Image2.png")
        with col4:
            st.markdown("#### 2. Quel est cet élément ?")
            if st.button("Dispositif de condamnation", key="btn_o2_a") or st.session_state.org_q2:
                st.session_state.org_q2 = True
                st.success("✅ EXACT (Empêche l'utilisation non autorisée)")
            if st.button("Sélecteur de programme", key="btn_o2_b"):
                st.error("❌ Non.")
            if st.button("Indicateur de décharge", key="btn_o2_c"):
                st.error("❌ Non.")

        st.markdown("---")

        # --- IMAGE 3 (Roue Stabilisatrice) ---
        col5, col6 = st.columns([1, 2])
        with col5:
            try: st.image("Image3.png", use_column_width=True)
            except: st.error("Manque Image3.png")
        with col6:
            st.markdown("#### 3. Quel est cet élément ?")
            if st.button("Roue directrice", key="btn_o3_a"):
                st.error("❌ Non, la directrice est plus grosse et au milieu.")
            if st.button("Galet porteur", key="btn_o3_b"):
                st.error("❌ Non, les galets sont sous les fourches.")
            if st.button("Roue stabilisatrice", key="btn_o3_c") or st.session_state.org_q3:
                st.session_state.org_q3 = True
                st.success("✅ EXACT (Pour la stabilité latérale)")

        st.markdown("---")

        # --- IMAGE 4 (Vitesse Lente / Tortue) ---
        col7, col8 = st.columns([1, 2])
        with col7:
            try: st.image("Image4.png", use_column_width=True)
            except: st.error("Manque Image4.png")
        with col8:
            st.markdown("#### 4. À quoi sert ce bouton ?")
            if st.button("Commande vitesse lente", key="btn_o4_a") or st.session_state.org_q4:
                st.session_state.org_q4 = True
                st.success("✅ EXACT (Mode Tortue : Timon vertical)")
            if st.button("Klaxon", key="btn_o4_b"):
                st.error("❌ Non.")
            if st.button("Levée des fourches", key="btn_o4_c"):
                st.error("❌ Non.")

        st.markdown("---")

        # --- IMAGE 5 (Roue Directrice) ---
        col9, col10 = st.columns([1, 2])
        with col9:
            try: st.image("Image5.png", use_column_width=True)
            except: st.error("Manque Image5.png")
        with col10:
            st.markdown("#### 5. Quel est cet élément ?")
            if st.button("Roue directrice", key="btn_o5_a") or st.session_state.org_q5:
                st.session_state.org_q5 = True
                st.success("✅ EXACT (Elle dirige et transmet la puissance)")
            if st.button("Roue stabilisatrice", key="btn_o5_b"):
                st.error("❌ Non, c'est la petite sur le côté.")
            if st.button("Roue libre", key="btn_o5_c"):
                st.error("❌ Non.")
# ==============================================================================
# AUTRES LIVRETS
# ==============================================================================
else:
    st.title(f"🚧 {livret}")
    st.info("Module en construction.")
