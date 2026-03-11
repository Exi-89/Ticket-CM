import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# --- KONFIGURACE STRÁNKY ---
st.set_page_config(
    page_title="Community Roleplay - Admin Panel",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PROPOJENÍ S TVOJI DATABÁZÍ ---
def get_db_connection():
    # Používáme tvůj soubor tickets.db
    conn = sqlite3.connect('tickets.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Funkce pro odeslání zprávy (ukládá do tvé tabulky messages)
def send_admin_message(ticket_id, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Vložíme zprávu jako 'Admin' - tvůj bot.py si ji odtud může brát nebo ji posílat dál
    cursor.execute(
        "INSERT INTO messages (ticket_id, sender, content) VALUES (?, ?, ?)",
        (ticket_id, "Admin", content)
    )
    # Aktualizujeme stav ticketu na 'Řeší se'
    cursor.execute("UPDATE tickets SET status = 'Řeší se' WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()

# --- CUSTOM CSS (Vzhled dashboard.html) ---
st.markdown("""
<style>
    .stApp { background-color: #0e0e1a; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #121225; border-right: 1px solid #2d2d44; }
    
    /* Kontejner pro tabulku */
    .main-card {
        background-color: #16162d;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #2d2d44;
    }
    
    /* Stylování statusů */
    .status-badge {
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .status-resi { background-color: rgba(241, 196, 15, 0.2); color: #f1c40f; }
    .status-novy { background-color: rgba(46, 204, 113, 0.2); color: #2ecc71; }
    .status-uzavren { background-color: rgba(231, 76, 60, 0.2); color: #e74c3c; }

    /* Sidebar tlačítka */
    .sidebar-btn {
        display: block;
        width: 100%;
        padding: 10px;
        color: #8888a0;
        text-decoration: none;
        border-radius: 5px;
        margin-bottom: 5px;
    }
    .active-nav { background-color: #1d1d3b; color: #6c5ce7; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Dle tvého loga a menu) ---
with st.sidebar:
    st.image("logo.jpg", width=120)
    st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>ADMIN PANEL</h3>", unsafe_allow_html=True)
    
    st.markdown("---")
    # Navigace
    if st.button("🏙️ Přehled", use_container_width=True): st.session_state.page = "dashboard"
    if st.button("🎫 Tikety", use_container_width=True): st.session_state.page = "tickets"
    if st.button("👤 Moje Tikety", use_container_width=True): pass
    if st.button("📁 Archiv", use_container_width=True): st.session_state.page = "archive"
    if st.button("⚙️ Nastavení", use_container_width=True): pass
    
    st.markdown("---")
    st.markdown("**STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>**", unsafe_allow_html=True)
    st.write("1 / 64 Hráčů")
    
    col1, col2 = st.columns(2)
    col1.button("Web", key="web")
    col2.button("Discord", key="dc")

# --- HLAVNÍ PLOCHA ---
st.title("Tikety podpory")

# Načtení dat z DB
conn = get_db_connection()
# Načítáme tikety (pokud máš v DB sloupec 'category', 'player', 'status', 'created_at')
tickets_df = pd.read_sql_query("SELECT * FROM tickets WHERE status != 'Uzavřen' ORDER BY id DESC", conn)
conn.close()

# Filtry a hledání
col_s, col_f = st.columns([3, 1])
with col_s:
    search = st.text_input("🔍 Hledat...", placeholder="Hledat podle jména hráče...", label_visibility="collapsed")

# Tabulka tiketů
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("Nedávné tikety")

# Hlavička
h1, h2, h3, h4, h5, h6 = st.columns([0.5, 1.5, 1.5, 1.5, 2.5, 1.5])
h1.write("**ID**")
h2.write("**HRÁČ**")
h3.write("**KATEGORIE**")
h4.write("**STAV**")
h5.write("**VYTVOŘENO**")
h6.write("**AKCE**")
st.divider()

for idx, row in tickets_df.iterrows():
    # Jednoduchý filtr
    if search and search.lower() not in row['player'].lower():
        continue
        
    c1, c2, c3, c4, c5, c6 = st.columns([0.5, 1.5, 1.5, 1.5, 2.5, 1.5])
    c1.write(f"#{row['id']}")
    c2.write(row['player'])
    c3.markdown(f"`{row['category']}`")
    
    # Badge pro stav
    status = row['status']
    st_class = "status-resi" if status == "Řeší se" else "status-novy"
    c4.markdown(f'<span class="status-badge {st_class}">{status}</span>', unsafe_allow_html=True)
    
    c5.write(row['created_at'])
    
    if c6.button("Otevřít →", key=f"btn_{row['id']}"):
        st.session_state.active_ticket_id = row['id']
        st.session_state.active_ticket_player = row['player']

st.markdown('</div>', unsafe_allow_html=True)

# --- MODUL CHATU (Detail tiketu) ---
if 'active_ticket_id' in st.session_state:
    t_id = st.session_state.active_ticket_id
    st.markdown("---")
    st.subheader(f"💬 Chat: {st.session_state.active_ticket_player} (Ticket #{t_id})")
    
    # Načtení historie zpráv pro tento tiket
    conn = get_db_connection()
    messages_df = pd.read_sql_query("SELECT * FROM messages WHERE ticket_id = ? ORDER BY id ASC", conn, params=(t_id,))
    conn.close()

    # Zobrazení chatu
    chat_box = st.container(height=400, border=True)
    for _, msg in messages_df.iterrows():
        is_admin = msg['sender'] == "Admin"
        with chat_box.chat_message("assistant" if is_admin else "user"):
            st.write(f"**{msg['sender']}**")
            st.write(msg['content'])
            st.caption(msg['timestamp'] if 'timestamp' in msg else "")

    # Odesílání
    if prompt := st.chat_input("Napište odpověď hráči..."):
        send_admin_message(t_id, prompt)
        st.rerun()
