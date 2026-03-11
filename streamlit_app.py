import streamlit as st
import sqlite3
import json
from datetime import datetime

# --- KONFIGURACE ---
st.set_page_config(page_title="Community RP - Admin", layout="wide")

# --- STYLOVÁNÍ (Neon Purple) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: white;
    }
    /* Styl pro karty tiketů v seznamu */
    .ticket-card {
        background: rgba(124, 58, 237, 0.1);
        border: 1px solid #7c3aed;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        transition: 0.3s;
    }
    .ticket-card:hover {
        background: rgba(124, 58, 237, 0.2);
        box-shadow: 0 0 15px #7c3aed;
    }
    /* Skrytí menu Streamlitu */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- FUNKCE DATABÁZE ---
def get_db():
    conn = sqlite3.connect("tickets.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS tickets 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, player TEXT, category TEXT, 
                  status TEXT, discord_id TEXT, created_at TIMESTAMP, history TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- DASHBOARD ---
st.title("💜 Community RP - Admin Panel")

col_list, col_detail = st.columns([0.4, 0.6])

with col_list:
    st.subheader("🎫 Aktivní vstupenky")
    
    conn = get_db()
    tickets = conn.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
    conn.close()

    if not tickets:
        st.info("Zatím žádné tikety. Zkus vytvořit testovací níže! 👇")
        if st.button("➕ Vytvořit testovací tiket"):
            conn = get_db()
            test_history = json.dumps([{"sender": "Hráč", "text": "Ahoj, potřebuju pomoc.", "time": "12:00"}])
            conn.execute("INSERT INTO tickets (player, category, status, history) VALUES (?, ?, ?, ?)",
                        ("TestHrac_89", "Podpora", "Otevřeno", test_history))
            conn.commit()
            conn.close()
            st.rerun()

    for t in tickets:
        # Vytvoření "klikatelné" karty pomocí buttonu
        if st.button(f"🆔 #{t['id']} | {t['player']}\n📂 {t['category']}", key=f"t_{t['id']}", use_container_width=True):
            st.session_state.active_id = t['id']
            st.rerun()

with col_detail:
    if "active_id" in st.session_state:
        conn = get_db()
        t = conn.execute("SELECT * FROM tickets WHERE id = ?", (st.session_state.active_id,)).fetchone()
        conn.close()

        st.markdown(f"### Detail tiketu #{t['id']}")
        st.write(f"**Hráč:** {t['player']} | **Kategorie:** {t['category']}")
        
        # CHAT
        st.markdown("---")
        history = json.loads(t['history']) if t['history'] else []
        for msg in history:
            align = "right" if msg['sender'] == "Admin" else "left"
            color = "#7c3aed" if msg['sender'] == "Admin" else "#374151"
            st.markdown(f'''
                <div style="text-align: {align}; margin-bottom: 10px;">
                    <div style="background: {color}; display: inline-block; padding: 10px; border-radius: 10px; max-width: 80%;">
                        <b>{msg['sender']}:</b> {msg['text']}<br>
                        <small style="opacity: 0.5;">{msg['time']}</small>
                    </div>
                </div>
            ''', unsafe_allow_html=True)

        # ODPOVĚĎ
        with st.form("reply", clear_on_submit=True):
            msg_text = st.text_input("Napiš odpověď...")
            if st.form_submit_button("Odeslat"):
                if msg_text:
                    history.append({"sender": "Admin", "text": msg_text, "time": datetime.now().strftime("%H:%M")})
                    conn = get_db()
                    conn.execute("UPDATE tickets SET history = ? WHERE id = ?", (json.dumps(history), t['id']))
                    conn.commit()
                    conn.close()
                    st.rerun()
    else:
        st.write("Vyberte tiket ze seznamu vlevo pro zobrazení chatu.")

# --- AUTO REFRESH ---
if st.button("🔄 Aktualizovat"):
    st.rerun()
