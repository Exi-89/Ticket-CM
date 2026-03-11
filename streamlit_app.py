import streamlit as st
import sqlite3
import json
import os
from datetime import datetime

# --- KONFIGURACE STRÁNKY ---
st.set_page_config(page_title="Community RP - Admin Panel", layout="wide")

# --- DESIGN (Identický s tvým původním login.html a dashboard.html) ---
st.markdown("""
    <style>
    /* Temné pozadí s fialovým nádechem */
    .stApp {
        background-color: #050505;
        background-image: 
            radial-gradient(at 0% 0%, rgba(168, 85, 247, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(168, 85, 247, 0.15) 0px, transparent 50%);
        color: white;
    }
    
    /* Karty tiketů */
    .ticket-card {
        background: rgba(17, 24, 39, 0.8);
        border: 1px solid rgba(168, 85, 247, 0.2);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        backdrop-filter: blur(10px);
    }
    
    /* Bubliny chatu */
    .chat-bubble-admin {
        background: #7c3aed;
        color: white;
        padding: 10px 15px;
        border-radius: 15px 15px 0px 15px;
        margin: 5px;
        text-align: right;
        display: inline-block;
        float: right;
        width: fit-content;
    }
    .chat-bubble-player {
        background: #374151;
        color: white;
        padding: 10px 15px;
        border-radius: 15px 15px 15px 0px;
        margin: 5px;
        text-align: left;
        display: inline-block;
        width: fit-content;
    }
    
    /* Skrytí standardních Streamlit prvků */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- DATABÁZE (Propojení se tvým systémem) ---
DB_NAME = "tickets.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tickets 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, player TEXT, category TEXT, 
                  status TEXT, discord_id TEXT, created_at TIMESTAMP, history TEXT)''')
    conn.commit()
    conn.close()

init_db()

def load_tickets():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    data = conn.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
    conn.close()
    return data

# --- LOGIKA DASHBOARDU ---
st.title("💜 Community Roleplay - Admin Panel")

# Rozvržení: Seznam tiketů vlevo, Detail vpravo
col_list, col_detail = st.columns([0.4, 0.6])

with col_list:
    st.subheader("🎫 Aktivní tikety")
    tickets = load_tickets()
    
    for t in tickets:
        with st.container():
            # Klikací karta tiketu
            if st.button(f"#{t['id']} | {t['player']} - {t['category']}", key=f"t_{t['id']}", use_container_width=True):
                st.session_state.active_id = t['id']
                st.rerun()

with col_detail:
    if "active_id" in st.session_state:
        # Načtení detailu vybraného tiketu
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        t = conn.execute("SELECT * FROM tickets WHERE id = ?", (st.session_state.active_id,)).fetchone()
        conn.close()
        
        st.subheader(f"Detail tiketu #{t['id']}")
        st.info(f"Hráč: {t['player']} | Kategorie: {t['category']} | Status: {t['status']}")
        
        # CHAT OKNO
        chat_container = st.container(height=400)
        history = json.loads(t['history']) if t['history'] else []
        
        with chat_container:
            for msg in history:
                div_class = "chat-bubble-admin" if msg['sender'] == "Admin" else "chat-bubble-player"
                st.markdown(f'<div class="{div_class}">{msg["text"]} <br><small>{msg["time"]}</small></div><div style="clear:both;"></div>', unsafe_allow_html=True)
        
        # ODESLÁNÍ ODPOVĚDI
        with st.form("reply_form", clear_on_submit=True):
            reply_text = st.text_input("Vaše odpověď (odešle se na Discord)...")
            if st.form_submit_content("Odeslat"):
                if reply_text:
                    history.append({
                        "sender": "Admin",
                        "text": reply_text,
                        "time": datetime.now().strftime("%H:%M"),
                        "to_discord": True  # Příznak pro tvého bota
                    })
                    conn = sqlite3.connect(DB_NAME)
                    conn.execute("UPDATE tickets SET history = ? WHERE id = ?", (json.dumps(history), t['id']))
                    conn.commit()
                    conn.close()
                    st.rerun()
    else:
        st.write("Vyberte tiket ze seznamu vlevo.")

# --- AUTO REFRESH (Každých 5 sekund zkontroluje nové zprávy) ---
if st.button("🔄 Aktualizovat"):
    st.rerun()
