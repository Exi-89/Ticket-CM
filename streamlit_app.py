import streamlit as st
import json

# --- 1. ZÁKLADNÍ NASTAVENÍ (MUSÍ BÝT PRVNÍ) ---
st.set_page_config(
    page_title="Community RP - Admin",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PAMĚŤ APLIKACE (SESSION STATE) ---
if "stranka" not in st.session_state:
    st.session_state.stranka = "Tikety"
if "vybrany_tiket" not in st.session_state:
    st.session_state.vybrany_tiket = None

# --- 3. STYLOVÁNÍ (Vzhled tvého ngrok dashboardu) ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    
    /* Vzhled bočního panelu */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    
    /* Úprava tlačítek v menu */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        text-align: left;
        background-color: transparent;
        border: none;
        color: #8b949e;
        padding: 10px;
    }
    .stButton > button:hover {
        background-color: #21262d;
        color: white;
    }
    
    /* Aktivní tlačítko v menu */
    .active-btn > div > button {
        background-color: #7c3aed33 !important;
        color: #a855f7 !important;
        border-left: 3px solid #a855f7 !important;
    }

    /* Tabulka tiketů */
    .row-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    
    header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. BOČNÍ PANEL (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>💜 CRP</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; margin-top: -15px;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Navigace - Tlačítka mění st.session_state.stranka
    def navigace(nazev):
        st.session_state.stranka = nazev
        st.session_state.vybrany_tiket = None
        st.rerun()

    if st.button("🏠 Přehled"): navigace("Přehled")
    
    # Zvýrazníme tlačítko Tikety, pokud jsme na nich
    st.markdown('<div class="active-btn">', unsafe_allow_html=True) if st.session_state.stranka == "Tikety" else None
    if st.button("🎫 Tikety"): navigace("Tikety")
    st.markdown('</div>', unsafe_allow_html=True) if st.session_state.stranka == "Tikety" else None
    
    if st.button("👤 Moje Tikety"): navigace("Moje Tikety")
    if st.button("📁 Archiv"): navigace("Archiv")
    if st.button("⚙️ Nastavení"): navigace("Nastavení")

    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)

# --- 5. LOGIKA STRÁNEK ---

# --- STRÁNKA TIKETY ---
if st.session_state.stranka == "Tikety":
    if st.session_state.vybrany_tiket is None:
        st.title("Tikety podpory")
        
        # Simulace dat z databáze
        data = [
            {"id": 6, "hrac": "xxexitusxx", "kat": "frakce", "stav": "Řeší se", "vytvoreno": "17:02:50"},
            {"id": 5, "hrac": "razor_21", "kat": "razor", "stav": "Řeší se", "vytvoreno": "16:28:02"},
            {"id": 2, "hrac": "CopRoleplay", "kat": "Frakce", "stav": "Nový", "vytvoreno": "08:09:41"}
        ]

        # Hlavička
        st.markdown("<div style='display:flex; color:gray; padding:0 20px;'> <div style='flex:1'>ID</div> <div style='flex:2'>HRÁČ</div> <div style='flex:2'>STAV</div> <div style='flex:1; text-align:right;'>AKCE</div> </div>", unsafe_allow_html=True)

        for t in data:
            col_info, col_btn = st.columns([0.85, 0.15])
            with col_info:
                color = "#f1c40f" if t['stav'] == "Řeší se" else "#2ecc71"
                st.markdown(f"""
                    <div class="row-card">
                        <div style="flex:1">#{t['id']}</div>
                        <div style="flex:2">{t['hrac']}</div>
                        <div style="flex:2"><span style="color:{color}; border:1px solid {color}; padding:2px 8px; border-radius:10px; font-size:12px;">{t['stav']}</span></div>
                    </div>
                """, unsafe_allow_html=True)
            with col_btn:
                st.write("") # Odsazení
                if st.button("Otevřít →", key=f"btn_{t['id']}"):
                    st.session_state.vybrany_tiket = t['id']
                    st.rerun()
    else:
        # DETAIL TIKETU (Když klikneš na Otevřít)
        if st.button("← Zpět na seznam"):
            st.session_state.vybrany_tiket = None
            st.rerun()
            
        st.title(f"Detail tiketu #{st.session_state.vybrany_tiket}")
        st.chat_message("user").write("Potřebuji pomoct s frakcí, nefunguje mi menu.")
        st.chat_input("Napiš admin odpověď...")

# --- OSTATNÍ STRÁNKY ---
else:
    st.title(st.session_state.stranka)
    st.info(f"Tato sekce ({st.session_state.stranka}) je ve vývoji.")
