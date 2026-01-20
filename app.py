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
    }
    .stSuccess { background-color: #d4edda; color: #155724; }
    .stError { background-color: #f8d7da; color: #721c24; }
    h1 { color: #004085; }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 1. SÉLECTION DU LIVRET (LE "HUB")
# ==============================================================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/5360/5360937.png", width=100)
st.sidebar.title("📚 CHOIX DU LIVRET")

# C'est ici que vous ajoutez vos 4 livrets
livret = st.sidebar.selectbox(
    "Quelle formation suivez-vous ?",
    ["CACES R.485 (Gerbeurs)", "CACES R.489 (Chariots)", "CACES R.486 (PEMP)", "CACES R.482 (Engins)"]
)

st.sidebar.markdown("---")

# ==============================================================================
# ZONE A : CACES R.485 (GERBEURS) - C'est celui qu'on a bossé
# ==============================================================================
if livret == "CACES R.485 (Gerbeurs)":
    
    # --- Menu spécifique au R.485 ---
    menu_485 = st.sidebar.radio("Modules R.485 :", 
        ["Accueil R.485", "1. Catégories (p.12)", "2. Technique & Batteries (p.23)", 
         "3. Stabilité (p.34)", "4. Conduite (p.54)", "5. Signalisation (p.58)"])

    if menu_485 == "Accueil R.485":
        st.title("🏗️ Formation Gerbeurs R.485")
        st.info("Bienvenue. Sélectionnez un module à gauche pour lancer un Auto-Test.")
        st.write("Ce livret concerne les gerbeurs à conducteur accompagnant.")

    # --- MODULE 1 : CATÉGORIES ---
    elif menu_485 == "1. Catégories (p.12)":
        st.header("🔍 Quiz : Reconnaissance des Engins")
        st.write("Regardez vos images p.12 ou ci-dessous.")
        
        c1, c2 = st.columns(2)
        with c1:
            # Remplacer par st.image("img_cat1.jpg")
            st.warning("🖼️ [IMAGE GERBEUR JAUNE]") 
            if st.button("Est-ce un R.485 ? (G)"):
                st.success("✅ OUI (Catégorie 1 ou 2)")
                
        with c2:
            st.info("🖼️ [IMAGE TRANSPALETTE]")
            if st.button("Est-ce un R.485 ? (T)"):
                st.error("❌ NON (R.366 - Transpalette)")

    # --- MODULE 2 : TECHNIQUE & BATTERIES ---
    elif menu_485 == "2. Technique & Batteries (p.23)":
        st.header("⚡ Batteries & Organes")
        
        st.subheader("Les Technologies Batteries")
        b1, b2, b3 = st.columns(3)
        b1.metric("Plomb Ouvert", "Entretien : OUI", "Gaz Explosif")
        b2.metric("GEL", "Entretien : NON", "Charge Lente")
        b3.metric("Lithium-Ion", "Entretien : NON", "Charge Rapide")
        
        st.markdown("---")
        st.write("❓ **Question : Peut-on fumer en chargeant une batterie Plomb ?**")
        if st.button("OUI (si fenêtre ouverte)"):
            st.error("💥 BOUM ! L'hydrogène est ultra-explosif.")
        if st.button("NON (Jamais)"):
            st.success("✅ BRAVO. Interdiction formelle.")

    # --- MODULE 3 : STABILITÉ ---
    elif menu_485 == "3. Stabilité (p.34)":
        st.header("⚖️ Plaque de Charge")
        st.write("Analysez l'abaque de charge (p.34).")
        
        # st.image("abaque.jpg")
        
        st.write("**Si mon centre de gravité s'éloigne (la charge est longue)...**")
        rep = st.radio("La capacité de levage :", ["Augmente", "Reste pareille", "Diminue"])
        
        if st.button("Vérifier Stabilité"):
            if rep == "Diminue":
                st.success("✅ EXACT ! Effet levier = Danger.")
                st.balloons()
            else:
                st.error("❌ FAUX. Plus c'est loin, moins on peut lever lourd.")

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

# ==============================================================================
# ZONE B : CACES R.489 (Exemple pour plus tard)
# ==============================================================================
elif livret == "CACES R.489 (Chariots)":
    st.title("🚜 Formation R.489")
    st.warning("⚠️ Contenu en cours de construction...")
    # Ici, vous pourrez copier-coller la même structure que pour le 485
    # st.sidebar.radio(...)

# ==============================================================================
# ZONE C : AUTRES
# ==============================================================================
else:
    st.title("🚧 Formation en construction")
    st.write(f"Le contenu pour {livret} sera ajouté bientôt.")
