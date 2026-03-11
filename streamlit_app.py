import streamlit as st
import sqlite3
import json
from datetime import datetime

# --- KONFIGURACE ---
st.set_page_config(page_title="Admin Panel", layout="wide")

DB_NAME = "tickets.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #0d0d17; color: #e0e0e0; }
    [data-testid="stSidebar"] { background-color: #111121; border-right: 1px solid #2d2d44; }
    
    /* Levý panel s tikety */
    .ticket-list { background-color: #16162d; padding: 15px; border-radius: 12px; border: 1px solid #2d2d44; }
    .ticket-item { 
        padding: 12px; border-bottom: 1px solid #23233d; cursor: pointer; transition: 0.2s;
    }
    .ticket-item:hover { background-color: #1d1d3b; }

    /* Pravý chat panel */
    .chat-window { background-color: #111121; border-radius: 12px; border: 1px solid #2d2d44; display: flex; flex-direction: column; height: 80vh; }
    .chat-messages { flex-grow: 1; overflow-y: auto; padding: 20px; }
    
    /* Bubliny */
    .msg-bubble { padding: 10px 15px; border-radius: 15px; margin-bottom: 10px; max-width: 80%; }
    .msg-user { background-color: #23233d; align-self: flex-start; border: 1px solid #3a3a5a; }
    .msg-admin { background-color: #6c5ce7; color: white; align-self: flex-end; margin-left: auto; }
    
    /* Statusy */
    .st-novy { color: #2ecc71; font-weight: bold; }
    .st-resi { color: #f1c40f; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("logo.jpg", width=120)
    st.markdown("### Community Roleplay\n**ADMIN PANEL**")
    st.divider()
    st.button("🎫 Tikety", use_container_width=True)
    st.button("📁 Archiv", use_container_width=True)
    st.button("⚙️ Nastavení", use_container_width=True)
    st.spacer(height=250)
    st.info("🟢 Server: Online")

# --- DATA LOGIC ---
conn = get_db_connection()
tickets = conn.execute("SELECT * FROM tickets WHERE status != 'Uzavřen' ORDER BY id DESC").fetchall()

# --- LAYOUT: 2 SLOUPCE (Seznam | Chat) ---
col_list, col_chat = st.columns([1, 2])

with col_list:
    st.subheader("Tikety")
    search = st.text_input("🔍 Hledat hráče...", placeholder="Jméno...", label_visibility="collapsed")
    
    for t in tickets:
        if search.lower() in t['player'].lower():
            # Simulace výběru kliknutím (pomocí tlačítka, co vypadá jako řádek)
            if st.button(f"#{t['id']} | {t['player']}\n{t['category']}", key=f"t_{t['id']}", use_container_width=True):
                st.session_state.active_ticket = dict(t)

with col_chat:
    if 'active_ticket' in st.session_state:
        act = st.session_state.active_ticket
        st.subheader(f"Detail tiketu #{act['id']} - {act['player']}")
        
        # Okno chatu
        with st.container(height=500):
            # Načtení historie (z tvého sloupce 'history', který je JSON)
            history = json.loads(act['history']) if act['history'] else []
            
            for msg in history:
                is_admin = msg['sender'] == "Admin"
                bubble_type = "msg-admin" if is_admin else "msg-user"
                st.markdown(f"""
                    <div class="msg-bubble {bubble_type}">
                        <strong>{msg['sender']}</strong> <small style='opacity:0.6'>({msg['time']})</small><br>
                        {msg['text']}
                    </div>
                """, unsafe_allow_html=True)

        # Odesílání zprávy
        with st.form("reply_form", clear_on_submit=True):
            reply_text = st.text_input("Napište zprávu hráči...")
            c1, c2 = st.columns([1, 1])
            if c1.form_submit_button("Odeslat zprávu 🚀", use_container_width=True):
                if reply_text:
                    # Aktualizace historie v DB
                    new_msg = {"sender": "Admin", "text": reply_text, "time": datetime.now().strftime("%H:%M")}
                    history.append(new_msg)
                    
                    new_conn = get_db_connection()
                    new_conn.execute("UPDATE tickets SET history = ?, status = 'Řeší se' WHERE id = ?", 
                                     (json.dumps(history), act['id']))
                    new_conn.commit()
                    
                    # Refresh dat v session state
                    st.session_state.active_ticket['history'] = json.dumps(history)
                    st.rerun()
            
            if c2.form_submit_button("❌ Uzavřít tiket", use_container_width=True):
                new_conn = get_db_connection()
                new_conn.execute("UPDATE tickets SET status = 'Uzavřen' WHERE id = ?", (act['id'],))
                new_conn.commit()
                del st.session_state.active_ticket
                st.rerun()
    else:
        st.info("Vyberte tiket ze seznamu pro zobrazení podrobností.")

conn.close()
