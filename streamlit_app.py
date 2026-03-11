import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import requests

# --- KONFIGURACE ---
# Pokud chceš, aby zprávy z webu okamžitě pípaly na DC, vlož sem Webhook URL
DISCORD_WEBHOOK_URL = "" 

st.set_page_config(page_title="Admin Panel - Tickets", layout="wide")

# --- PROPOJENÍ S TVOJI DB (Dle database.py) ---
def query_db(query, params=(), one=False):
    conn = sqlite3.connect('tickets.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# --- CSS PRO IDENTICKÝ VZHLED ---
st.markdown("""
<style>
    /* Hlavní barvy */
    .stApp { background-color: #0b0b15; color: #e1e1e6; }
    [data-testid="stSidebar"] { background-color: #0f0f1e; border-right: 1px solid #1e1e2f; }
    
    /* Karty a kontejnery */
    .main-card { background-color: #121225; padding: 25px; border-radius: 15px; border: 1px solid #1e1e2f; }
    
    /* Tabulka */
    .stDataFrame { border: none !important; }
    .ticket-row { border-bottom: 1px solid #1e1e2f; padding: 10px 0; transition: 0.3s; }
    .ticket-row:hover { background-color: #1a1a35; }

    /* Badge statusy */
    .badge { padding: 4px 12px; border-radius: 6px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .status-resi { background-color: rgba(255, 193, 7, 0.1); color: #ffc107; border: 1px solid #ffc107; }
    .status-novy { background-color: rgba(40, 167, 69, 0.1); color: #28a745; border: 1px solid #28a745; }
    
    /* Chat sekce (Pravá strana) */
    .chat-container { background-color: #0f0f1e; border-radius: 12px; padding: 15px; border: 1px solid #1e1e2f; height: 500px; overflow-y: auto; }
    .msg-admin { align-self: flex-end; background-color: #6c5ce7; color: white; padding: 8px 12px; border-radius: 10px 10px 0 10px; margin: 5px; }
    .msg-player { align-self: flex-start; background-color: #1e1e2f; color: white; padding: 8px 12px; border-radius: 10px 10px 10px 0; margin: 5px; border: 1px solid #2d2d44; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("logo.jpg", width=100)
    st.markdown("### Community RP\n**ADMIN PANEL**")
    st.divider()
    st.button("🏠 Přehled", use_container_width=True)
    st.button("🎫 Tikety", use_container_width=True)
    st.button("📁 Archiv", use_container_width=True)
    st.divider()
    st.markdown("🟢 **Server Online** (1/64)")

# --- HLAVNÍ ROZHRANÍ ---
col_main, col_chat = st.columns([2, 1])

with col_main:
    st.title("Tikety podpory")
    
    # Načtení dat z tvé DB (předpokládám sloupce z tvého bot.py)
    tickets = query_db("SELECT * FROM tickets WHERE status != 'Uzavřen' ORDER BY id DESC")
    
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # Hlavička tabulky
    t_h1, t_h2, t_h3, t_h4 = st.columns([1, 2, 2, 2])
    t_h1.caption("ID")
    t_h2.caption("HRÁČ")
    t_h3.caption("STAV")
    t_h4.caption("AKCE")
    st.divider()

    for t in tickets:
        r1, r2, r3, r4 = st.columns([1, 2, 2, 2])
        r1.write(f"#{t['id']}")
        r2.write(f"**{t['player']}**")
        
        # Status Badge
        st_class = "status-resi" if t['status'] == "Řeší se" else "status-novy"
        r3.markdown(f'<span class="badge {st_class}">{t["status"]}</span>', unsafe_allow_html=True)
        
        if r4.button("Detail →", key=f"t_{t['id']}"):
            st.session_state.active_id = t['id']
            st.session_state.active_player = t['player']
    st.markdown('</div>', unsafe_allow_html=True)

# --- DETAIL TIKETU (CHAT) ---
with col_chat:
    if 'active_id' in st.session_state:
        t_id = st.session_state.active_id
        st.subheader(f"Chat: #{t_id}")
        
        # Načtení zpráv
        msgs = query_db("SELECT * FROM messages WHERE ticket_id = ? ORDER BY id ASC", (t_id,))
        
        # Chat box
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for m in msgs:
            is_admin = (m['sender'] == "Admin")
            div_class = "msg-admin" if is_admin else "msg-player"
            st.markdown(f'''
                <div style="display: flex; flex-direction: column;">
                    <div class="{div_class}">
                        <small style="opacity: 0.7;">{m['sender']}</small><br>{m['content']}
                    </div>
                </div>
            ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input
        with st.form("msg_form", clear_on_submit=True):
            user_input = st.text_input("Napište odpověď...")
            col_s1, col_s2 = st.columns(2)
            if col_s1.form_submit_button("Odeslat 🚀"):
                if user_input:
                    # 1. Uložit do DB
                    query_db("INSERT INTO messages (ticket_id, sender, content) VALUES (?, ?, ?)", 
                             (t_id, "Admin", user_input))
                    query_db("UPDATE tickets SET status = 'Řeší se' WHERE id = ?", (t_id,))
                    
                    # 2. Odeslat na Discord (pokud máš Webhook)
                    if DISCORD_WEBHOOK_URL:
                        requests.post(DISCORD_WEBHOOK_URL, json={"content": f"**Admin:** {user_input}"})
                    
                    st.rerun()
            
            if col_s2.form_submit_button("❌ Zavřít"):
                query_db("UPDATE tickets SET status = 'Uzavřen' WHERE id = ?", (t_id,))
                del st.session_state.active_id
                st.rerun()
    else:
        st.info("Vyberte tiket ze seznamu pro zobrazení chatu.")
