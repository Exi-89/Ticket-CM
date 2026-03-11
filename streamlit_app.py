import streamlit as st

# 1. Musí být úplně první věc v souboru
st.set_page_config(page_title="CRP Admin", layout="wide", initial_sidebar_state="expanded")

# 2. CSS pro barvy a vzhled (aby to vypadalo jako tvůj ngrok dashboard)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    
    /* Vynucení tmavého sidebaru */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    
    /* Skrytí horní lišty Streamlitu */
    header { visibility: hidden; }
    
    /* Styl pro tabulku tiketů */
    .ticket-container {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BOČNÍ PANEL (SIDEBAR) - Tady jsou ty tlačítka
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: white;'>💜 CRP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>ADMIN PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Navigační tlačítka - každé má svou akci
    if st.button("🏠 Přehled", use_container_width=True):
        st.toast("Načítám přehled...")
        
    if st.button("🎫 Tikety", type="primary", use_container_width=True):
        st.toast("Načítám tikety...")
        
    if st.button("👤 Moje Tikety", use_container_width=True):
        st.toast("Načítám tvoje tikety...")
        
    if st.button("📁 Archiv", use_container_width=True):
        st.toast("Otevírám archiv...")

    st.write("---")
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)

# 4. HLAVNÍ OBSAH (To, co vidíš teď na screenshotu)
st.title("Tikety podpory")

# Horní filtry
col1, col2 = st.columns([3, 1])
with col2:
    st.selectbox("", ["Všechny stavy", "Nové", "Řeší se"], label_visibility="collapsed")

# Tabulka
st.markdown("""
<div class="ticket-container">
    <table style="width:100%; border-collapse: collapse; color: #8b949e;">
        <tr style="border-bottom: 1px solid #30363d; text-align: left;">
            <th style="padding: 10px;">ID</th>
            <th>HRÁČ</th>
            <th>STAV</th>
            <th style="text-align: right;">AKCE</th>
        </tr>
        <tr style="border-bottom: 1px solid #30363d;">
            <td style="padding: 15px 10px;">#6</td>
            <td>xxexitusxx</td>
            <td><span style="color: #f1c40f; background: #f1c40f22; padding: 2px 8px; border-radius: 10px;">Řeší se</span></td>
            <td style="text-align: right; color: #a855f7;">Otevřít →</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)
