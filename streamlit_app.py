import streamlit as st

# 1. NASTAVENÍ STRÁNKY (MUSÍ BÝT PRVNÍ A NA SAMOSTATNÉM ŘÁDKU)
st.set_page_config(
    page_title="CRP Admin",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. KOMPLETNÍ FIALOVÝ DESIGN (CSS)
st.markdown("""
    <style>
    /* Hlavní barvy pozadí */
    .stApp { background-color: #0d1117; color: #e6edf3; }
    
    /* Postranní panel - Fialové ohraničení a tmavá barva */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 2px solid #7c3aed;
    }
    
    /* Schování defaultních lišt Streamlitu */
    header { visibility: hidden; }
    
    /* Styl pro tlačítka (fialová neonová) */
    .stButton > button {
        width: 100%;
        background-color: transparent;
        color: #a855f7;
        border: 1px solid #7c3aed;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #7c3aed22;
        border-color: #a855f7;
        box-shadow: 0 0 10px #7c3aed;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. POSTRANNÍ PANEL (SIDEBAR)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: white;'>💜 CRP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; margin-top: -15px;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.button("🏠 Přehled")
    st.button("🎫 Tikety")
    st.button("👤 Moje Tikety")
    st.button("📁 Archiv")
    
    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)
    st.progress(0.02)
    st.caption("1 / 64 Hráčů")

# 4. HLAVNÍ PLOCHA (TIKETY)
st.title("Tikety podpory")

# Horní filtry
c1, c2, c3 = st.columns([2, 1, 1])
with c2: st.selectbox("Stav", ["Všechny stavy", "Nové", "Řeší se"], label_visibility="collapsed")
with c3: st.text_input("Hledat...", label_visibility="collapsed", placeholder="Hledat...")

# Tabulka (Vypadá jako na tvém odkazu)
st.markdown("""
<div style='background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px;'>
    <div style='display: flex; color: gray; font-size: 12px; border-bottom: 1px solid #30363d; padding-bottom: 10px; margin-bottom: 15px;'>
        <div style='flex: 0.5;'>ID</div>
        <div style='flex: 2;'>HRÁČ</div>
        <div style='flex: 1;'>KATEGORIE</div>
        <div style='flex: 1;'>STAV</div>
        <div style='flex: 1.5;'>VYTVOŘENO</div>
        <div style='flex: 1; text-align: right;'>AKCE</div>
    </div>
    <div style='display: flex; align-items: center; padding: 10px 0; border-bottom: 1px solid #21262d;'>
        <div style='flex: 0.5;'>#6</div>
        <div style='flex: 2;'>xxexitusxx</div>
        <div style='flex: 1;'><span style='background: #30363d; padding: 2px 8px; border-radius: 4px;'>frakce</span></div>
        <div style='flex: 1;'><span style='color: #f1c40f; background: rgba(241,196,15,0.1); border: 1px solid #f1c40f; padding: 2px 8px; border-radius: 10px; font-size: 12px;'>Řeší se</span></div>
        <div style='flex: 1.5; color: #8b949e;'>2026-03-07 17:02:50</div>
        <div style='flex: 1; text-align: right; color: #a855f7; cursor: pointer; font-weight: bold;'>Otevřít →</div>
    </div>
</div>
""", unsafe_allow_html=True)
