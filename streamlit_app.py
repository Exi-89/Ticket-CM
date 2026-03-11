import streamlit as st
import sqlite3
import pandas as pd
import requests
from datetime import datetime

# --- KONFIGURACE ---
DISCORD_WEBHOOK_URL = "TVUJ_DISCORD_WEBHOOK_ZDE" # Sem vlož URL webhooku z nastavení kanálu na DC

st.set_page_config(
    page_title="Community Roleplay - Admin Panel",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNKCE PRO DATABÁZI ---
def get_db_connection():
    conn = sqlite3.connect('tickets.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT,
            category TEXT,
            status TEXT,
            created_at DATETIME,
            discord_channel_id TEXT
        )
    ''')
    conn.commit()
    conn.close()

def send_to_discord(message):
    if DISCORD_WEBHOOK_URL != "TVUJ_DISCORD_WEBHOOK_ZDE":
        payload = {"content": message}
        requests.post(DISCORD_WEBHOOK_URL, json=payload)

# Inicializace DB
init_db()

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #0e0e1a; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #121225; border-right: 1px solid #2d2d44; }
    .ticket-container { background-color: #16162d; padding: 20px; border-radius: 10px; border: 1px solid #2d2d44; }
    
    /* Stylování tlačítek v menu */
    .stButton>button {
        width: 100%;
        background-color: transparent;
        color: #8888a0;
        border: none;
        text-align: left;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #1d1d3b;
        color: #6c5ce7;
    }
    
    /* Statusy */
    .status-badge {
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: bold;
    }
    .status-resi { background-color: rgba(241, 196, 15, 0.2); color: #f1c40f; }
    .status-novy { background-color: rgba(46, 204, 113, 0.2); color: #2ecc71; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    try:
        st.image("logo.jpg", width=150)
    except:
        st.write("🏙️ **Community Roleplay**")
    
    st.markdown("<h3 style='text-align: center; color: #6c5ce7;'>ADMIN PANEL</h3>", unsafe_allow_html=True)
    st.divider()
    
    st.button("🏙️ Přehled")
    st.button("🎫 Tikety")
    st.button("👤 Moje Tikety")
    st.button("📁 Archiv")
    st.button("⚙️ Nastavení")
    
    st.divider()
    st.markdown("**STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>**", unsafe_allow_html=True)
    st.write("1 / 64 Hráčů")
    
    col1, col2 = st.columns(2)
    col1.button("Web", key="web_btn")
    col2.button("Discord", key="dc_btn")
    
    st.markdown("---")
    st.caption("👤 xxexitusxx\nAdministrátor")

# --- HLAVNÍ OBSAH ---
st.title("Tikety podpory")

# Filtry
c_filter1, c_filter2 = st.columns([2, 5])
with c_filter1:
    search = st.text_input("🔍 Hledat tikety...", placeholder="Jméno hráče...")

# Načtení dat z DB
conn = get_db_connection()
query = "SELECT * FROM tickets ORDER BY created_at DESC"
df = pd.read_sql_query(query, conn)
conn.close()

st.markdown('<div class="ticket-container">', unsafe_allow_html=True)
st.subheader("Nedávné tikety")

# Hlavička tabulky
h1, h2, h3, h4, h5, h6 = st.columns([1, 2, 2, 2, 3, 2])
h1.write("**ID**")
h2.write("**HRÁČ**")
h3.write("**KATEGORIE**")
h4.write("**STAV**")
h5.write("**VYTVOŘENO**")
h6.write("**AKCE**")
st.divider()

# Iterace skrze data
for index, row in df.iterrows():
    if search.lower() in row['player'].lower():
        r1, r2, r3, r4, r5, r6 = st.columns([1, 2, 2, 2, 3, 2])
        r1.write(f"#{row['id']}")
        r2.write(row['player'])
        r3.markdown(f"`{row['category']}`")
        
        status_class = "status-resi" if row['status'] == "Řeší se" else "status-novy"
        r4.markdown(f'<span class="status-badge {status_class}">{row["status"]}</span>', unsafe_allow_html=True)
        
        r5.write(row['created_at'])
        
        if r6.button("Otevřít →", key=f"btn_{row['id']}"):
            st.session_state.active_ticket = row['id']
            st.session_state.active_player = row['player']

st.markdown('</div>', unsafe_allow_html=True)

# --- DETAIL TIKETU (Chat) ---
if 'active_ticket' in st.session_state:
    st.markdown("---")
    st.subheader(f"💬 Chat s hráčem: {st.session_state.active_player} (Ticket #{st.session_state.active_ticket})")
    
    with st.container():
        # Zde by se načítaly zprávy z DB pro daný ticket
        st.info("Zde se zobrazí historie zpráv z Discordu.")
        
        msg = st.text_input("Napište odpověď hráči na Discord:")
        if st.button("Odeslat odpověď"):
            if msg:
                send_to_discord(f"**Admin (Web):** {msg}")
                st.success("Zpráva byla odeslána do Discordu!")
            else:
                st.warning("Zpráva nemůže být prázdná.")
