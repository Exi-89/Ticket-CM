import streamlit as st
import pandas as pd

# Nastavení stránky
st.set_page_config(
    page_title="Community Roleplay - Admin Panel",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS PRO VZHLED DLE OBRÁZKU ---
st.markdown("""
<style>
    /* Hlavní pozadí a barva textu */
    .stApp {
        background-color: #0e0e1a;
        color: #ffffff;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #121225;
        border-right: 1px solid #2d2d44;
    }
    
    /* Karty a kontejnery */
    .ticket-container {
        background-color: #16162d;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2d2d44;
    }
    
    /* Tlačítka a fialové prvky */
    .stButton>button {
        background-color: #6c5ce7;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
    }
    
    /* Status badges */
    .status-resi {
        background-color: #f1c40f33;
        color: #f1c40f;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
    }
    .status-novy {
        background-color: #2ecc7133;
        color: #2ecc71;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
    }

    /* Tabulka úpravy */
    thead tr th {
        color: #8888a0 !important;
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://via.placeholder.com/100", width=100) # Zde dejte své logo
    st.markdown("### Community Roleplay\n**ADMIN PANEL**")
    st.divider()
    
    st.button("🏠 Přehled", use_container_width=True)
    st.button("🎫 Tikety", use_container_width=True)
    st.button("👤 Moje Tikety", use_container_width=True)
    st.button("📁 Archiv", use_container_width=True)
    st.button("⚙️ Nastavení", use_container_width=True)
    
    st.spacer(height=200) # Odstup dolů
    
    # Status serveru spodní část
    st.info("STAV SERVERU: ● ONLINE\n\n1 / 64 Hráčů")
    col1, col2 = st.columns(2)
    col1.button("Web")
    col2.button("Discord")

# --- HLAVNÍ OBSAH ---
st.header("Tikety podpory")

# Horní lišta s filtry
col_a, col_b = st.columns([6, 2])
with col_b:
    st.selectbox("Stav", ["Všechny stavy", "Nové", "Řeší se", "Uzavřené"], label_visibility="collapsed")
    st.text_input("Hledat tikety...", placeholder="Hledat tikety...", label_visibility="collapsed")

# Tabulka tiketů (Demo data)
st.markdown('<div class="ticket-container">', unsafe_allow_html=True)
st.subheader("Nedávné tikety")

# Simulace dat jako na obrázku
data = [
    {"ID": "#6", "HRÁČ": "xxexitusxx", "KATEGORIE": "frakce", "STAV": "Řeší se", "VYTVOŘENO": "2026-03-07 17:02:50"},
    {"ID": "#5", "HRÁČ": "razor_21", "KATEGORIE": "razor", "STAV": "Řeší se", "VYTVOŘENO": "2026-03-07 16:28:02"},
    {"ID": "#3", "HRÁČ": "xxexitusxx", "KATEGORIE": "Frakce", "STAV": "Řeší se", "VYTVOŘENO": "2026-03-07 10:59:33"},
    {"ID": "#2", "HRÁČ": "CopRoleplay", "KATEGORIE": "Frakce", "STAV": "Nový", "VYTVOŘENO": "2026-03-07 08:09:41"},
]

# Vykreslení hlavičky tabulky
cols = st.columns([1, 2, 2, 2, 3, 2])
cols[0].write("**ID**")
cols[1].write("**HRÁČ**")
cols[2].write("**KATEGORIE**")
cols[3].write("**STAV**")
cols[4].write("**VYTVOŘENO**")
cols[5].write("**AKCE**")

st.divider()

# Vykreslení řádků
for row in data:
    c1, c2, c3, c4, c5, c6 = st.columns([1, 2, 2, 2, 3, 2])
    c1.write(row["ID"])
    c2.write(row["HRÁČ"])
    c3.markdown(f"`{row['KATEGORIE']}`")
    
    # Barevný status
    if row["STAV"] == "Řeší se":
        c4.markdown(f'<span class="status-resi">{row["STAV"]}</span>', unsafe_allow_html=True)
    else:
        c4.markdown(f'<span class="status-novy">{row["STAV"]}</span>', unsafe_allow_html=True)
        
    c5.write(row["VYTVOŘENO"])
    if c6.button("Otevřít →", key=row["ID"]):
        st.session_state.open_ticket = row["ID"]
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- CHATOVÉ ROZHRANÍ (Zobrazí se po kliknutí na tiket) ---
if 'open_ticket' in st.session_state:
    st.divider()
    st.subheader(f"Detail tiketu {st.session_state.open_ticket}")
    
    # Zde by byl výpis zpráv z databáze (z Discordu i Webu)
    st.text_area("Zpráva pro uživatele (odešle se na Discord):")
    if st.button("Odeslat zprávu"):
        st.success("Zpráva odeslána na Discord!")
