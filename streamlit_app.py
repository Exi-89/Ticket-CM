import streamlit as st

# 1. KONFIGURACE (Musí být úplně nahoře)
st.set_page_config(
    page_title="CRP Admin",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. DESIGN (CSS) - Vynucení viditelnosti
st.markdown("""
    <style>
    /* Pozadí hlavní plochy */
    .stApp { background-color: #0d1117; color: white; }
    
    /* VYNUCENÍ BARVY SIDEBARU - Aby byl vidět rozdíl */
    section[data-testid="stSidebar"] {
        background-color: #1c2128 !important; /* Trochu světlejší než zbytek */
        border-right: 1px solid #30363d !important;
    }
    
    /* Styl pro tlačítka v menu */
    .stButton>button {
        border-radius: 5px;
        margin-bottom: 5px;
    }
    
    /* Skrytí zbytečností */
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. OBSAH BOČNÍHO PANELU (SIDEBAR)
# Používáme st.sidebar.xxx pro všechno, co má být vlevo
with st.sidebar:
    st.markdown("<h2 style='color: #a855f7;'>💜 CRP ADMIN</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Navigační menu
    st.subheader("Menu")
    btn_prehled = st.button("🏠 Přehled", use_container_width=True)
    btn_tikety = st.button("🎫 Tikety", use_container_width=True)
    btn_archiv = st.button("📁 Archiv", use_container_width=True)
    
    st.write("---")
    st.info("Server: Online")
    st.caption("Verze 1.0.2")

# 4. HLAVNÍ PLOCHA
st.title("Tikety podpory")

# Ukázka tabulky, kterou už tam máš
st.markdown("""
<div style='background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px;'>
    <div style='display: flex; justify-content: space-between; border-bottom: 1px solid #30363d; padding-bottom: 10px; color: gray;'>
        <span>ID</span><span>HRÁČ</span><span>STAV</span><span>AKCE</span>
    </div>
    <div style='display: flex; justify-content: space-between; padding: 15px 0;'>
        <span>#6</span><span>xxexitusxx</span><span style='color: #f1c40f;'>Řeší se</span><span style='color: #a855f7;'>Otevřít →</span>
    </div>
</div>
""", unsafe_allow_html=True)
