import streamlit as st
import sqlite3
from datetime import datetime

# --- 1. KONFIGURACE (MUSÍ BÝT PRVNÍ) ---
st.set_page_config(
    page_title="Community Roleplay - Admin Panel",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. KOMPLETNÍ STYLING (PODLE NGROK PŘEDLOHY) ---
st.markdown("""
    <style>
    /* Hlavní pozadí a písmo */
    .stApp { background-color: #0d1117; color: #e6edf3; }
    
    /* Levý Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    
    /* Schovat horní lištu Streamlitu */
    header { visibility: hidden; }
    
    /* Fialové akcenty pro tlačítka v menu */
    .stButton > button {
        width: 100%;
        background-color: transparent;
        color: #8b949e;
        border: none;
        text-align: left;
        padding: 10px 15px;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background-color: #21262d;
        color: #7c3aed;
    }
    
    /* Speciální styl pro aktivní tlačítko "Tikety" */
    .active-nav {
        background-color: #7c3aed22 !important;
        color: #a855f7 !important;
        border-left: 3px solid #a855f7 !important;
        border-radius: 4px;
    }

    /* Tabulkový kontejner */
    .main-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BOČNÍ MENU ---
with st.sidebar:
    # Logo a název
    st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <h2 style='color: white; margin-bottom: 0;'>Community Roleplay</h2>
            <p style='color: #a855f7; font-size: 0.8em; font-weight: bold;'>ADMIN PANEL</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Navigace
    st.button("⊞ Přehled")
    st.markdown('<div class="active-nav">', unsafe_allow_html=True)
    st.button("🎫 Tikety")
    st.markdown('</div>', unsafe_allow_html=True)
    st.button("👤 Moje Tikety")
    st.button("📁 Archiv")
    st.button("⚙ Nastavení")

    # Status serveru dole
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        <div style='background: #0d1117; padding: 15px; border-radius: 10px; border: 1px solid #30363d;'>
            <div style='display: flex; justify-content: space-between;'>
                <span style='font-size: 0.8em;'>STAV SERVERU</span>
                <span style='color: #2ecc71; font-size: 0.8em;'>● ONLINE</span>
            </div>
            <h3 style='margin: 10px 0;'>1 <span style='color: gray; font-size: 0.5em;'>/ 64 Hráčů</span></h3>
            <div style='background: #30363d; height: 4px; border-radius: 2px;'>
                <div style='background: #a855f7; width: 2%; height: 100%; border-radius: 2px;'></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. HLAVNÍ OBSAH (TIKETY) ---
st.title("Tikety podpory")

# Horní filtry a vyhledávání
c1, c2, c3 = st.columns([2, 1, 1])
with c2: st.selectbox("Stav", ["Všechny stavy", "Nový", "Řeší se"], label_visibility="collapsed")
with c3: st.text_input("Hledat tikety...", label_visibility="collapsed", placeholder="Hledat...")

# Tabulka tiketů
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("""
    <div style='display: flex; color: #8b949e; font-weight: bold; border-bottom: 1px solid #30363d; padding-bottom: 10px; margin-bottom: 10px;'>
        <div style='flex: 0.5;'>ID</div>
        <div style='flex: 1.5;'>HRÁČ</div>
        <div style='flex: 1;'>KATEGORIE</div>
        <div style='flex: 1;'>STAV</div>
        <div style='flex: 1.5;'>VYTVOŘENO</div>
        <div style='flex: 1; text-align: right;'>AKCE</div>
    </div>
""", unsafe_allow_html=True)

# Ukázková data (v budoucnu SQL)
demo_tickets = [
    {"id": "#6", "hrac": "xxexitusxx", "kat": "frakce", "stav": "Řeší se", "stav_col": "#f1c40f", "cas": "2026-03-07 17:02:50"},
    {"id": "#5", "hrac": "razor_21", "kat": "razor", "stav": "Řeší se", "stav_col": "#f1c40f", "cas": "2026-03-07 16:28:02"},
    {"id": "#2", "hrac": "CopRoleplay", "kat": "Frakce", "stav": "Nový", "stav_col": "#2ecc71", "cas": "2026-03-07 08:09:41"},
]

for t in demo_tickets:
    col_data, col_btn = st.columns([0.85, 0.15])
    with col_data:
        st.markdown(f"""
            <div style='display: flex; align-items: center; padding: 10px 0; border-bottom: 1px solid #21262d;'>
                <div style='flex: 0.5;'>{t['id']}</div>
                <div style='flex: 1.5;'>{t['hrac']}</div>
                <div style='flex: 1;'><span style='background: #30363d; padding: 2px 8px; border-radius: 4px; font-size: 0.8em;'>{t['kat']}</span></div>
                <div style='flex: 1;'><span style='color: {t['stav_col']}; background: {t['stav_col']}22; padding: 2px 8px; border-radius: 10px; font-size: 0.8em;'>{t['stav']}</span></div>
                <div style='flex: 1.5; color: #8b949e; font-size: 0.9em;'>{t['cas']}</div>
            </div>
        """, unsafe_allow_html=True)
    with col_btn:
        st.write("") # Vyrovnání
        if st.button("Otevřít →", key=f"btn_{t['id']}"):
            st.toast(f"Načítám tiket {t['id']}")

st.markdown('</div>', unsafe_allow_html=True)
