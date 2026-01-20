import streamlit as st
from PIL import Image

# --- CONFIGURATION GÉNÉRALE ---
st.set_page_config(page_title="Hub Formation CACES", layout="centered", page_icon="🏗️")

# --- STYLE CSS (Design) ---
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
    /* Ces classes permettent de styliser les messages persistants */
    .element-container {
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FONCTION MAGIQUE (POUR LA MÉMOIRE)
# ==============================================================================
# Cette fonction permet de se souvenir si un bouton a été cliqué
def init_state(key):
    if key not in st.session_state:
        st.session_state[key] = False

# ==============================================================================
# MENU LATÉRAL
# ==============================================================================
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
    
    # On utilise des clés uniques pour chaque module pour éviter les conflits
    menu_485 = st.sidebar.radio("Modules R.485 :", 
        ["Accueil R.485", "1. Catégories (p.12)", "2. Technique (p.23)", 
         "3. Stabilité (p.34)", "4. Conduite (p.54)", "5. Signalisation (p.58)"])

    # --- ACCUEIL ---
    if menu_485 == "Accueil R.485":
        st.title("🏗️ Formation Gerbeurs R.485")
        st.info("Bienvenue. Ce module utilise la méthode de la **Photo Mentale**.")
        st.write("Les réponses correctes resteront affichées pour faciliter votre mémorisation.")

    # --- MODULE 1 : CATÉGORIES (PERSISTANT) ---
    elif menu_485 == "1. Catégories (p.12)":
        st.header("🔍 Quiz : Reconnaissance des Engins")
        st.write("Identifiez les engins R.485. Les réponses restent affichées.")
        
        # Initialisation de la mémoire pour ce quiz
        init_state("cat_q1")
        init_state("cat_q2")
        init_state("cat_q3")
        init_state("cat_q4")

        col1, col2 = st.columns(2)
        
        # --- IMAGE 1 ---
        with col1:
            st.warning("🖼️ [IMAGE GERBEUR JAUNE]") # Remplacer par st.image("img1.jpg")
            
            # Si on clique OU si on a déjà cliqué avant
            if st.button("Est-ce un R.485 ? (1)") or st.session_state.cat_q1:
                st.session_state.cat_q1 = True # On mémorise le clic
                st.success("✅ OUI (Catégorie 1 ou 2)")
            
            st.markdown("---")

            st.warning("🖼️ [IMAGE GERBEUR ORANGE]")
            if st.button("Est-ce un R.485 ? (3)") or st.session_state.cat_q3:
                st.session_state.cat_q3 = True
                st.success("✅ OUI (Catégorie 1 ou 2)")

        # --- IMAGE 2 ---
        with col2:
            st.info("🖼️ [IMAGE TRANSPALETTE]")
            if st.button("Est-ce un R.485 ? (2)") or st.session_state.cat_q2:
                st.session_state.cat_q2 = True
                st.error("❌ NON (R.366 - Transpalette)")
                st.write("Pas de mât élévateur = Pas de CACES R.485")
            
            st.markdown("---")
            
            st.error("🖼️ [IMAGE CHARIOT PORTÉ]")
            if st.button("Est-ce un R.485 ? (4)") or st.session_state.cat_q4:
                st.session_state.cat_q4 = True
                st.error("❌ NON (R.489 - Porté)")
                st.write("Le conducteur est assis = R.489")

    # --- MODULE 2 : TECHNIQUE (PERSISTANT) ---
    elif menu_485 == "2. Technique (p.23)":
        st.header("⚡ Technique & Batteries")
        init_state("tech_bat_plomb")
        
        st.write("❓ **Question : Peut-on fumer en chargeant une batterie Plomb Ouvert ?**")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("OUI (si fenêtre ouverte)") or st.session_state.tech_bat_plomb == "wrong":
                st.session_state.tech_bat_plomb = "wrong"
                st.error("💥 BOUM ! L'hydrogène est ultra-explosif.")
        
        with c2:
            if st.button("NON (Jamais)") or st.session_state.tech_bat_plomb == "correct":
                st.session_state.tech_bat_plomb = "correct"
                st.success("✅ BRAVO. Interdiction formelle.")

    # --- MODULE 3 : STABILITÉ ---
    elif menu_485 == "3. Stabilité (p.34)":
        st.header("⚖️ Plaque de Charge")
        init_state("stab_q1")
        
        st.write("**Si mon centre de gravité s'éloigne (la charge est longue), la capacité...**")
        
        c1, c2, c3 = st.columns(3)
        if c1.button("Augmente"):
            st.error("❌ Faux. Risque de basculement.")
        if c2.button("Diminue") or st.session_state.stab_q1:
            st.session_state.stab_q1 = True
            st.success("✅ CORRECT ! Plus c'est long, moins on lève lourd.")
        if c3.button("Reste pareille"):
            st.error("❌ Faux.")

    # --- MODULE 4 : CONDUITE ---
    elif menu_485 == "4. Conduite (p.54)":
        st.header("🚦 Règles de Conduite")
        init_state("cond_q1")
        init_state("cond_q2")
        
        st.write("**1. Distance de sécurité entre 2 gerbeurs ?**")
        if st.button("3 gerbeurs") or st.session_state.cond_q1:
            st.session_state.cond_q1 = True
            st.success("✅ CORRECT (env. 3 à 5m)")
        
        st.markdown("---")
        
        st.write("**2. Dans une pente, la charge doit être...**")
        if st.button("Vers l'AMONT (Haut)") or st.session_state.cond_q2:
            st.session_state.cond_q2 = True
            st.success("✅ CORRECT (Pour la plaquer au dosseret)")

    # --- MODULE 5 : SIGNALISATION ---
    elif menu_485 == "5. Signalisation (p.58)":
        st.header("🚧 Panneaux")
        st.write("Cliquez pour révéler la signification.")
        init_state("sig_tox")
        init_state("sig_epi")
        
        c1, c2 = st.columns(2)
        with c1:
            st.write("☠️ **Tête de Mort**")
            if st.button("Révéler ##1") or st.session_state.sig_tox:
                st.session_state.sig_tox = True
                st.success("✅ TOXIQUE (Danger de mort)")
            
        with c2:
            st.write("🔵 **Rond Bleu (Chaussure)**")
            if st.button("Révéler ##2") or st.session_state.sig_epi:
                st.session_state.sig_epi = True
                st.success("✅ OBLIGATION (Port des EPI)")

# ==============================================================================
# AUTRES LIVRETS (Vides pour l'instant)
# ==============================================================================
else:
    st.title(f"🚧 {livret}")
    st.info("Ce module sera disponible prochainement.")
