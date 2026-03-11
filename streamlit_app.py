import streamlit as st
import sqlite3
import json
from datetime import datetime

# --- 1. KONFIGURACE (MUSÍ BÝT PRVNÍ) ---
st.set_page_config(
    page_title="Community RP - Admin Panel",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DESIGN (CSS) ---
st.markdown("""
    <style>
    /* Pozadí a text */
    .stApp { background-color: #0d1117; color: #e6edf3; }
    
    /* VYNUCENÍ VZHLEDU SIDEBARU */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d !important;
    }
    
    /* Skrytí horní lišty a patičky */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Tabulka tiketů */
    .ticket-row {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 12px 20px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
    }
    .status-badge {
        padding: 2px 10px;
        border-radius: 10px;
        font-size: 11px;
        font-weight: bold;
        border: 1px solid;
    }
    .status-resise { background: #f1c40f22; color: #f1c40f; border-color: #f1c40f; }
    .status-novy { background: #2ecc7122; color: #2ecc71; border-color: #2ecc71; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "Tikety"
if "selected_ticket" not in st.session_state:
    st.session_state.selected_ticket = None

# --- 4. BOČNÍ PANEL (SIDEBAR) ---
# Používáme přímý zápis do sidebaru
st.sidebar.markdown("<h2 style='text-align: center; color: #a855f7;'>💜 CRP</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: gray; margin-top: -15px;'>ADMIN PANEL</p>", unsafe_allow_html=True)
st.sidebar.write("---")

# Tlačítka v navigaci
if st.sidebar.button("🏠 Přehled", use_container_width=True):
    st.session_state.page = "Přehled"
    st.session_state.selected_ticket = None
    st.rerun()

if st.sidebar.button("🎫 Tikety", type="primary" if st.session_state.page == "Tikety" else "secondary", use_container_width=True):
    st.session_state.page = "Tikety"
    st.session_state.selected_ticket = None
    st.rerun()

if st.sidebar.button("👤 Moje Tikety", use_container_width=True):
    st.session_state.page = "Moje Tikety"
    st.rerun()

if st.sidebar.button("📁 Archiv", use_container_width=True):
    st.session_state.page = "Archiv"
    st.rerun()

st.sidebar.write("---")
st.sidebar.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)
st.sidebar.progress(0.02)
st.sidebar.caption("1 / 64 Hráčů")

# --- 5. HLAVNÍ OBSAH ---
if st.session_state.page == "Tikety":
    if st.session_state.selected_ticket is None:
        st.title("Tikety podpory")
        
        # Testovací data
        tickets = [
            {"id": 6, "hrac": "xxexitusxx", "kat": "frakce", "stav": "Řeší se", "cas": "17:02"},
            {"id": 5, "hrac": "razor_21", "kat": "razor", "stav": "Řeší se", "cas": "16:28"},
            {"id": 2, "hrac": "CopRoleplay", "kat": "Frakce", "stav": "Nový", "cas": "08:09"},
        ]

        st.markdown("<div style='display: flex; color: gray; padding: 10px 20px; font-weight: bold;'> <div style='flex: 0.5;'>ID</div> <div style='flex: 1.5;'>HRÁČ</div> <div style='flex: 1;'>STAV</div> <div style='flex: 1; text-align: right;'>AKCE</div> </div>", unsafe_allow_html=True)

        for t in tickets:
            s_class = "status-resise" if t['stav'] == "Řeší se" else "status-novy"
            col_info, col_btn = st.columns([0.85, 0.15])
            with col_info:
                st.markdown(f"""
                <div class="ticket-row">
                    <div style='flex: 0.5;'>#{t['id']}</div>
                    <div style='flex: 1.5;'>{t['hrac']}</div>
                    <div style='flex: 1;'><span class="status-badge {s_class}">{t['stav']}</span></div>
                </div>
                """, unsafe_allow_html=True)
            with col_btn:
                if st.button("Otevřít →", key=f"tix_{t['id']}", use_container_width=True):
                    st.session_state.selected_ticket = t['id']
                    st.rerun()
    else:
        if st.button("← Zpět na seznam"):
            st.session_state.selected_ticket = None
            st.rerun()
        st.header(f"Detail tiketu #{st.session_state.selected_ticket}")
        st.info("Zde bude historie chatu...")
else:
    st.title(st.session_state.page)
    st.write(f"Vítejte na stránce {st.session_state.page}")
