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
         "3. Stabilité (p.34)", "4. Conduite (p.54)", "5. Signalisation (p.58)"])

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

    # --- MODULE 3 : STABILITÉ (QUIZ PLAQUES) ---
    elif menu_485 == "3. Stabilité (p.34)":
        st.header("⚖️ Exercice : Plaques de Charge")
        st.write("Analysez le document ci-dessous (Réponses p.59).")
        
        # --- C'EST ICI QUE J'AI MIS LE BON NOM ---
        # Si votre image est en .jpg, changez juste .png en .jpg ci-dessous
        try:
            st.image("quizz_plaque_de_charge_gerbeur.png", caption="Exercice Auto-Test Livret", use_column_width=True)
        except:
            st.error("⚠️ Image introuvable. Vérifiez que le nom sur GitHub est bien 'quizz_plaque_de_charge_gerbeur.png'")

        st.markdown("---")
        
        # Initialisation des mémoires
        init_state("plaque_q1"); init_state("plaque_q2"); init_state("plaque_q3"); init_state("plaque_q4")

        # QUESTION 1
        st.subheader("1. Tableau du haut")
        st.write("Pour lever **630 kg** (Longueur 1200mm = CDG 600mm), quelle est la hauteur max ?")
        c1, c2 = st.columns(2)
        if c1.button("4000 mm") or st.session_state.plaque_q1:
            st.session_state.plaque_q1 = True
            st.success("✅ 4000 mm (Correct !)")
        if c2.button("4300 mm"):
            st.error("❌ Non. À 4300mm, la limite est de 550kg (voir case au-dessus).")

        st.markdown("---")

        # QUESTION 2
        st.subheader("2. Tableau du haut")
        st.write("À **4300 mm** de haut, avec une charge longue (1400mm = CDG 700mm), quel poids max ?")
        c3, c4 = st.columns(2)
        if c3.button("330 kg") or st.session_state.plaque_q2:
            st.session_state.plaque_q2 = True
            st.success("✅ 330 kg (Dernière colonne, ligne du haut)")
        if c4.button("550 kg"):
            st.error("❌ Non, 550kg c'est pour une charge standard (CDG 500/600).")

        st.markdown("---")

        # QUESTION 3
        st.subheader("3. Graphique (Milieu)")
        st.write("Charge de **1400 kg**, CDG à **400 mm**. Quelle hauteur max ?")
        c5, c6 = st.columns(2)
        if c5.button("3884 mm") or st.session_state.plaque_q3:
            st.session_state.plaque_q3 = True
            st.success("✅ 3884 mm (Intersection de la ligne 1400 et 400)")
        if c6.button("4224 mm"):
            st.error("❌ Non, ça c'est pour une charge plus légère (ex: 1000kg).")
            
        st.markdown("---")

        # QUESTION 4
        st.subheader("4. Plaque du bas (Constructeur)")
        st.write("D'après cette plaque, je peux déplacer :")
        c7, c8 = st.columns(2)
        if c7.button("1200 kg à 600 mm") or st.session_state.plaque_q4:
            st.session_state.plaque_q4 = True
            st.success("✅ EXACT (Capacité nominale)")
        if c8.button("1556 kg à 300 mm"):
            st.error("❌ Non, 1556kg c'est le poids du chariot à vide !")

    # --- MODULE 4 : CONDUITE ---
    elif menu_485 == "4. Conduite (p.54)":
        st.header("🚦 Règles de Conduite")
        init_state("cond_q1")
        st.write("**Distance de sécurité entre 2 gerbeurs ?**")
        if st.button("3 gerbeurs") or st.session_state.cond_q1:
            st.session_state.cond_q1 = True
            st.success("✅ CORRECT")

    # --- MODULE 5 : SIGNALISATION ---
    elif menu_485 == "5. Signalisation (p.58)":
        st.header("🚧 Panneaux")
        init_state("sig_tox")
        st.write("☠️ **Tête de Mort**")
        if st.button("Toxique") or st.session_state.sig_tox:
            st.session_state.sig_tox = True
            st.success("✅ VRAI")

# ==============================================================================
# AUTRES LIVRETS
# ==============================================================================
else:
    st.title(f"🚧 {livret}")
    st.info("Module en construction.")
