import streamlit as st
import sqlite3

# 1. Musí být jako první řádek
st.set_page_config(page_title="CRP Admin", layout="wide", initial_sidebar_state="expanded")

# 2. Fialový design (vynucení barev podle tvého vzoru)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    [data-testid="stSidebar"] { 
        background-color: #161b22 !important; 
        border-right: 2px solid #7c3aed !important; 
    }
    .stButton>button {
        background-color: #7c3aed22;
        color: #a855f7;
        border: 1px solid #7c3aed;
        width: 100%;
        border-radius: 8px;
    }
    header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 3. Boční menu (Sidebar)
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #a855f7;'>💜 CRP ADMIN</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Tlačítka menu (zatím jen vizuální, aby tam byla)
    st.button("🏠 Přehled")
    st.button("🎫 Tikety", type="primary")
    st.button("👤 Moje Tikety")
    st.button("📁 Archiv")
    
    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)
    st.progress(0.02) # Ukazatel hráčů

# 4. Hlavní obsah - Tabulka tiketů
st.title("Tikety podpory")

# Vytvoření tabulky (sloupce jako na tvém obrázku)
col1, col2, col3, col4, col5 = st.columns([0.5, 1.5, 1.5, 1, 1])
col1.caption("ID")
col2.caption("HRÁČ")
col3.caption("KATEGORIE")
col4.caption("STAV")
col5.caption("AKCE")

st.markdown("---")

# Ukázka tiketu (přesně podle tvého screenshotu #6)
c1, c2, c3, c4, c5 = st.columns([0.5, 1.5, 1.5, 1, 1])
c1.write("#6")
c2.write("xxexitusxx")
c3.write("frakce")
c4.markdown("<span style='color:#f1c40f'>Řeší se</span>", unsafe_allow_html=True)
if c5.button("Otevřít →", key="t6"):
    st.success("Otevírám tiket #6... (Tady se pak napojí chat)")

# Ukázka dalšího tiketu
c1, c2, c3, c4, c5 = st.columns([0.5, 1.5, 1.5, 1, 1])
c1.write("#2")
c2.write("CopRoleplay")
c3.write("Frakce")
c4.markdown("<span style='color:#2ecc71'>Nový</span>", unsafe_allow_html=True)
if c5.button("Otevřít →", key="t2"):
    st.info("Otevírám tiket #2...")
