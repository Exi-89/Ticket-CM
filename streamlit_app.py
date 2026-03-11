import streamlit as st
import sqlite3
import json
from datetime import datetime

# 1. MUSÍ BÝT JAKO PRVNÍ: Nastavení stránky a širokého režimu
st.set_page_config(
    page_title="Community RP - Admin Panel", 
    layout="wide", 
    initial_sidebar_state="expanded" # Toto vynutí otevření bočního panelu
)

# --- SESSION STATE (PAMĚŤ) ---
if "page" not in st.session_state:
    st.session_state.page = "Tikety"
if "selected_ticket" not in st.session_state:
    st.session_state.selected_ticket = None

# --- DESIGN (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    
    /* Vynucení barvy bočního panelu */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
        min-width: 250px !important;
    }

    /* Styl pro řádky tabulky */
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

    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- BOČNÍ PANEL (SIDEBAR) ---
with st.sidebar:
    # Zkusíme vložit logo (pokud ho máš v repozitáři jako logo.png nebo logo.jpg)
    try:
        st.image("logo.jpg", width=150)
    except:
        st.markdown("<h1 style='text-align: center;'>💜 CRP</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: #8b949e;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Navigační tlačítka
    if st.button("🏠 Přehled", use_container_width=True):
        st.session_state.page = "Přehled"
        st.session_state.selected_ticket = None
        st.rerun()
        
    if st.button("🎫 Tikety", type="primary" if st.session_state.page == "Tikety" else "secondary", use_container_width=True):
        st.session_state.page = "Tikety"
        st.session_state.selected_ticket = None
        st.rerun()
        
    if st.button("👤 Moje Tikety", use_container_width=True):
        st.session_state.page = "Moje Tikety"
        st.rerun()

    if st.button("📁 Archiv", use_container_width=True):
        st.session_state.page = "Archiv"
        st.rerun()

    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)
    st.progress(0.02)
    st.caption("1 / 64 Hráčů")

# --- OBSAH STRÁNEK ---

if st.session_state.page == "Tikety":
    if st.session_state.selected_ticket is None:
        st.title("Tikety podpory")
        
        # Testovací data
        tickets = [
            {"id": 6, "hrac": "xxexitusxx", "kat": "frakce", "stav": "Řeší se", "cas": "17:02"},
            {"id": 5, "hrac": "razor_21", "kat": "razor", "stav": "Řeší se", "cas": "16:28"},
            {"id": 2, "hrac": "CopRoleplay", "kat": "Frakce", "stav": "Nový", "cas": "08:09"},
        ]

        # Hlavička "tabulky"
        st.markdown("<div style='display: flex; color: gray; padding: 10px 20px; font-weight: bold;'> <div style='flex: 0.5;'>ID</div> <div style='flex: 1.5;'>HRÁČ</div> <div style='flex: 1;'>STAV</div> <div style='flex: 1; text-align: right;'>AKCE</div> </div>", unsafe_allow_html=True)

        for t in tickets:
            s_class = "status-resise" if t['stav'] == "Řeší se" else "status-novy"
            
            # Kontejner pro řádek
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
                # Tlačítko pro otevření
                if st.button("Otevřít →", key=f"tix_{t['id']}", use_container_width=True):
                    st.session_state.selected_ticket = t['id']
                    st.rerun()

    else:
        # DETAIL TIKETU
        if st.button("← Zpět na seznam"):
            st.session_state.selected_ticket = None
            st.rerun()
        st.header(f"Detail tiketu #{st.session_state.selected_ticket}")
        st.write("Tady bude brzy funkční chat...")

else:
    st.title(st.session_state.page)
    st.write(f"Obsah pro stránku {st.session_state.page} připravujeme.")
