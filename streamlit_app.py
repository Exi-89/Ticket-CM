import streamlit as st
import sqlite3
from datetime import datetime

# --- 1. KONFIGURACE (TOTO MUSÍ BÝT NA ZAČÁTKU) ---
st.set_page_config(
    page_title="CRP Admin Panel",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. KOMPLETNÍ FIALOVÝ DESIGN (CSS) ---
st.markdown("""
    <style>
    /* Hlavní tmavé pozadí */
    .stApp { background-color: #0d1117; color: #e6edf3; }
    
    /* Levý panel (Sidebar) - Fialové prvky */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 2px solid #7c3aed;
    }
    
    /* Horní lišta pryč */
    header { visibility: hidden; }

    /* Fialová tlačítka v menu */
    .stButton > button {
        width: 100%;
        background-color: transparent;
        color: #a855f7;
        border: 1px solid #7c3aed;
        border-radius: 8px;
        font-weight: bold;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #7c3aed22;
        box-shadow: 0 0 10px #7c3aed;
    }

    /* Vzhled tabulky (karty tiketů) */
    .ticket-row {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABÁZE ---
def init_db():
    conn = sqlite3.connect('tickets.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS tickets 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  hrac TEXT, kat TEXT, stav TEXT, cas TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- 4. BOČNÍ MENU (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #a855f7;'>💜 COMMUNITY RP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Navigační tlačítka
    if st.button("🏠 Přehled"): st.session_state.p = "p"
    if st.button("🎫 Tikety"): st.session_state.p = "t"
    if st.button("📁 Archiv"): st.session_state.p = "a"
    if st.button("⚙️ Nastavení"): st.session_state.p = "n"
    
    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)
    st.progress(0.02)
    st.caption("1 / 64 Hráčů")

# --- 5. HLAVNÍ OBSAH (TABULKA) ---
st.title("🎫 Tikety podpory")

# Pokud je databáze prázdná, přidáme jeden testovací tiket, ať to vidíš
conn = sqlite3.connect('tickets.db')
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM tickets")
if c.fetchone()[0] == 0:
    c.execute("INSERT INTO tickets (hrac, kat, stav, cas) VALUES (?, ?, ?, ?)", 
              ('xxexitusxx', 'frakce', 'Řeší se', '2026-03-07 17:02:50'))
    conn.commit()

# Načtení tiketů
c.execute("SELECT * FROM tickets ORDER BY id DESC")
tickets = c.fetchall()
conn.close()

# Hlavička tabulky
col_id, col_hrac, col_kat, col_stav, col_akce = st.columns([0.5, 1.5, 1.5, 1, 1])
col_id.caption("ID")
col_hrac.caption("HRÁČ")
col_kat.caption("KATEGORIE")
col_stav.caption("STAV")
col_akce.caption("AKCE")

st.write("---")

# Výpis tiketů
for t in tickets:
    c1, c2, c3, c4, c5 = st.columns([0.5, 1.5, 1.5, 1, 1])
    c1.write(f"#{t[0]}")
    c2.write(t[1])
    c3.markdown(f"<span style='background:#30363d; padding:2px 8px; border-radius:4px;'>{t[2]}</span>", unsafe_allow_html=True)
    c4.markdown(f"<span style='color:#f1c40f'>● {t[3]}</span>", unsafe_allow_html=True)
    if c5.button("Otevřít →", key=f"btn_{t[0]}"):
        st.info(f"Otevírám tiket hráče {t[1]}...")
