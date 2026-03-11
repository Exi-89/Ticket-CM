import streamlit as st
import sqlite3
import json
from datetime import datetime

# --- KONFIGURACE STRÁNKY ---
st.set_page_config(page_title="Community RP - Admin Panel", layout="wide")

# --- SESSION STATE (PAMĚŤ APLIKACE) ---
if "page" not in st.session_state:
    st.session_state.page = "Tikety"  # Výchozí stránka
if "selected_ticket" not in st.session_state:
    st.session_state.selected_ticket = None

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    
    /* Styl pro řádky v tabulce */
    .ticket-row {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 12px 20px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        transition: 0.2s;
    }
    .ticket-row:hover { border-color: #a855f7; background-color: #1c2128; }
    
    .status-badge {
        padding: 2px 10px;
        border-radius: 10px;
        font-size: 11px;
        font-weight: bold;
        border: 1px solid;
    }
    .status-resise { background: #f1c40f22; color: #f1c40f; border-color: #f1c40f; }
    .status-novy { background: #2ecc7122; color: #2ecc71; border-color: #2ecc71; }
    
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (LEVÝ PANEL) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>💜 CRP</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Funkční tlačítka menu
    if st.button("🏠 Přehled", use_container_width=True):
        st.session_state.page = "Přehled"
        st.session_state.selected_ticket = None
        st.rerun()
        
    if st.button("🎫 Tikety", type="primary" if st.session_state.page == "Tikety" else "secondary", use_container_width=True):
        st.session_state.page = "Tikety"
        st.session_state.selected_ticket = None
        st.rerun()
        
    if st.button("📁 Archiv", use_container_width=True):
        st.session_state.page = "Archiv"
        st.rerun()

    st.write("---")
    st.caption("STAV SERVERU: ● ONLINE")
    st.progress(0.02) # 1/64

# --- LOGIKA STRÁNEK ---

# 1. STRÁNKA: PŘEHLED
if st.session_state.page == "Přehled":
    st.title("Vítejte v Admin Panelu")
    st.write("Zde uvidíte statistiky (počet tiketů, aktivní adminy atd.).")

# 2. STRÁNKA: TIKETY
elif st.session_state.page == "Tikety":
    if st.session_state.selected_ticket is None:
        st.title("Tikety podpory")
        
        # Simulace dat (v reálu SELECT * FROM tickets)
        tickets = [
            {"id": 6, "hrac": "xxexitusxx", "kat": "frakce", "stav": "Řeší se", "cas": "17:02"},
            {"id": 5, "hrac": "razor_21", "kat": "razor", "stav": "Řeší se", "cas": "16:28"},
            {"id": 2, "hrac": "CopRoleplay", "kat": "Frakce", "stav": "Nový", "cas": "08:09"},
        ]

        # Hlavička tabulky
        st.markdown("<div style='display: flex; color: gray; padding: 10px 20px;'> <div style='flex: 0.5;'>ID</div> <div style='flex: 1.5;'>HRÁČ</div> <div style='flex: 1;'>STAV</div> <div style='flex: 1; text-align: right;'>AKCE</div> </div>", unsafe_allow_html=True)

        for t in tickets:
            s_class = "status-resise" if t['stav'] == "Řeší se" else "status-novy"
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.markdown(f"""
                <div class="ticket-row">
                    <div style='flex: 0.5;'>#{t['id']}</div>
                    <div style='flex: 1.5;'>{t['hrac']}</div>
                    <div style='flex: 1;'><span class="status-badge {s_class}">{t['stav']}</span></div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                if st.button("Otevřít", key=f"btn_{t['id']}"):
                    st.session_state.selected_ticket = t['id']
                    st.rerun()
    
    else:
        # DETAIL TIKETU (CHAT)
        if st.button("← Zpět na seznam"):
            st.session_state.selected_ticket = None
            st.rerun()
            
        st.title(f"Detail tiketu #{st.session_state.selected_ticket}")
        st.info("Zde bude historie chatu z databáze a políčko pro odpověď.")
        # Sem vložíme ten chatovací kód, co jsme dělali minule

# 3. STRÁNKA: ARCHIV
elif st.session_state.page == "Archiv":
    st.title("Archiv tiketů")
    st.write("Zde jsou uzavřené případy.")
