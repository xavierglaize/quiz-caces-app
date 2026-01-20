import streamlit as st
from PIL import Image

# --- CONFIGURATION ---
st.set_page_config(page_title="Formation CACES R.485", layout="centered")

# --- STYLE CSS (Pour faire joli) ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #009999;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
    }
    .stError {
        background-color: #f8d7da;
        color: #721c24;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- MENU LATÉRAL ---
st.sidebar.title("📚 Navigation")
menu = st.sidebar.radio("Aller à :", 
    ["Accueil", "1. Catégories", "2. Signalisation", "3. Prise de Poste", "4. Stabilité"])

# --- PAGE D'ACCUEIL ---
if menu == "Accueil":
    st.title("🎓 Formation CACES R.485")
    st.info("Bienvenue dans votre application de révision interactive.")
    st.write("Utilisez le menu à gauche pour accéder aux différents modules de test.")
    st.success("👨‍🏫 Formateur : Prêt à tester vos connaissances ?")

# --- MODULE 1 : CATÉGORIES (Le Quiz Visuel) ---
elif menu == "1. Catégories":
    st.header("🔍 Identifiez les Gerbeurs R.485")
    st.write("Parmi ces photos, lesquelles nécessitent le CACES R.485 ?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📸 IMAGE 1 (Gerbeur Jaune)")
        if st.button("Est-ce un R.485 ? (1)"):
            st.balloons()
            st.success("✅ OUI ! C'est un gerbeur à conducteur accompagnant.")
            
        st.warning("📸 IMAGE 3 (Gerbeur Orange)")
        if st.button("Est-ce un R.485 ? (3)"):
            st.success("✅ OUI ! Bravo.")

    with col2:
        st.error("📸 IMAGE 2 (Transpalette)")
        if st.button("Est-ce un R.485 ? (2)"):
            st.error("❌ NON ! C'est un transpalette (R.366). Pas de mât élévateur.")
            
        st.error("📸 IMAGE 4 (Chariot Porté)")
        if st.button("Est-ce un R.485 ? (4)"):
            st.error("❌ NON ! Le conducteur est assis dessus (R.489).")

# --- MODULE 2 : SIGNALISATION ---
elif menu == "2. Signalisation":
    st.header("🚧 Panneaux & Pictogrammes")
    
    st.subheader("1. Que signifie ce panneau ? 💀")
    # Astuce : Mettez ici st.image("votre_image.png") si vous l'avez uploadée
    rep = st.radio("Votre réponse :", ["Corrosif", "Toxique", "Irritant"], key="q1")
    
    if st.button("Valider la réponse"):
        if rep == "Toxique":
            st.success("✅ EXACT ! Danger de mort.")
        else:
            st.error("❌ FAUX. La tête de mort signifie TOXIQUE.")

# --- MODULE 3 : VRAI / FAUX RAPIDE ---
elif menu == "3. Prise de Poste":
    st.header("⚡ Vrai ou Faux : Vérifications")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("1. La VGP est tous les 6 mois.")
        if st.button("VRAI", key="v1"): st.success("✅ CORRECT !")
        if st.button("FAUX", key="f1"): st.error("❌ ERREUR.")
        
    with col2:
        st.write("2. Je peux fumer en chargeant.")
        if st.button("VRAI", key="v2"): st.error("❌ BOUM ! Explosion.")
        if st.button("FAUX", key="f2"): st.success("✅ CORRECT ! Gaz explosif.")

# --- MODULE 4 : STABILITÉ ---
elif menu == "4. Stabilité":
    st.header("⚖️ La Plaque de Charge")
    st.write("Si le centre de gravité de ma charge s'éloigne du talon des fourches (Distance D augmente)...")
    
    rep_stab = st.selectbox("La capacité de levage du chariot :", ["Augmente", "Reste la même", "Diminue"])
    
    if st.button("Vérifier"):
        if rep_stab == "Diminue":
            st.success("✅ BRAVO ! Plus c'est long, moins on lève lourd (Effet levier).")
        else:
            st.error("❌ ATTENTION ! Risque de basculement vers l'avant.")
