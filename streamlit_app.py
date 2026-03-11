import streamlit as st

# 1. NASTAVENÍ STRÁNKY (Musí být hned na začátku)
st.set_page_config(
    page_title="CRP Admin Panel",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. STYLOVÁNÍ (Vzhled tvého panelu) ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    header {visibility: hidden;}
    .ticket-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BOČNÍ PANEL (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>💜 CRP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Tlačítka navigace
    st.button("🏠 Přehled", use_container_width=True)
    st.button("🎫 Tikety", type="primary", use_container_width=True)
    st.button("👤 Moje Tikety", use_container_width=True)
    st.button("📁 Archiv", use_container_width=True)
    st.button("⚙️ Nastavení", use_container_width=True)
    
    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)
    st.progress(0.02)
    st.caption("1 / 64 Hráčů")

# --- 4. HLAVNÍ OBSAH (TABULKA) ---
st.title("Tikety podpory")

# Hlavička tabulky
col_id, col_hrac, col_kat, col_stav, col_akce = st.columns([0.5, 1.5, 1.5, 1, 1])
with col_id: st.caption("ID")
with col_hrac: st.caption("HRÁČ")
with col_kat: st.caption("KATEGORIE")
with col_stav: st.caption("STAV")
with col_akce: st.caption("AKCE")

# Ukázkový řádek (přesně podle tvého vzoru)
st.markdown("---")
c1, c2, c3, c4, c5 = st.columns([0.5, 1.5, 1.5, 1, 1])
with c1: st.write("#6")
with c2: st.write("xxexitusxx")
with c3: st.write("frakce")
with c4: st.markdown("<span style='color:#f1c40f'>Řeší se</span>", unsafe_allow_html=True)
with c5: 
    if st.button("Otevřít →", key="opt6"):
        st.info("Otevírám tiket #6...")
