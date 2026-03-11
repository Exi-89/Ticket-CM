import streamlit as st
import sqlite3

# --- 1. ZÁKLADNÍ NASTAVENÍ ---
st.set_page_config(
    page_title="Community RP - Admin",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. FIALOVÝ DESIGN (CSS) ---
st.markdown("""
    <style>
    /* Temné pozadí */
    .stApp { background-color: #0d1117; color: #e6edf3; }
    
    /* Boční panel s fialovým okrajem */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #7c3aed;
    }
    
    /* Fialová tlačítka */
    .stButton>button {
        background-color: #7c3aed22;
        color: #a855f7;
        border: 1px solid #7c3aed;
        width: 100%;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #7c3aed44;
        border-color: #a855f7;
        box-shadow: 0 0 10px #7c3aed;
    }
    
    header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABÁZE ---
def init_db():
    conn = sqlite3.connect('tickets.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS tickets 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  player TEXT, category TEXT, status TEXT DEFAULT 'Nový')''')
    conn.commit()
    conn.close()

init_db()

# --- 4. BOČNÍ MENU (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #a855f7;'>💜 CRP</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🏠 Přehled"): st.session_state.page = "Přehled"
    if st.button("🎫 Tikety"): st.session_state.page = "Tikety"
    if st.button("📁 Archiv"): st.session_state.page = "Archiv"
    
    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)

# --- 5. HLAVNÍ OBSAH ---
if "page" not in st.session_state:
    st.session_state.page = "Tikety"

st.title(f"{st.session_state.page}")

if st.session_state.page == "Tikety":
    # Načtení dat
    conn = sqlite3.connect('tickets.db')
    conn.row_factory = sqlite3.Row
    tickets = conn.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
    conn.close()

    # Tabulka (Design podle tvého vzoru)
    st.markdown("<div style='display:flex; color:gray; padding:10px;'> <div style='flex:0.5'>ID</div> <div style='flex:2'>HRÁČ</div> <div style='flex:1'>STAV</div> <div style='flex:1'>AKCE</div> </div>", unsafe_allow_html=True)
    
    if not tickets:
        st.info("Zatím žádné aktivní tikety.")
        if st.button("➕ Vytvořit testovací tiket pro ukázku"):
            c = sqlite3.connect('tickets.db')
            c.execute("INSERT INTO tickets (player, category) VALUES ('Test_Player', 'Podpora')")
            c.commit()
            c.close()
            st.rerun()

    for t in tickets:
        col1, col2, col3, col4 = st.columns([0.5, 2, 1, 1])
        col1.write(f"#{t['id']}")
        col2.write(t['player'])
        col3.markdown(f"<span style='color:#f1c40f'>{t['status']}</span>", unsafe_allow_html=True)
        if col4.button("Otevřít →", key=f"t_{t['id']}"):
            st.write(f"Otevírám tiket #{t['id']}")
