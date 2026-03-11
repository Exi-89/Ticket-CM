import streamlit as st
import sqlite3
import json
from datetime import datetime

# --- KONFIGURACE STRÁNKY ---
st.set_page_config(page_title="Community RP - Admin Panel", layout="wide")

# --- CUSTOM CSS PRO IDENTICKÝ VZHLED ---
st.markdown("""
    <style>
    /* Temné pozadí celé aplikace */
    .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    
    /* Úprava bočního panelu */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
        padding-top: 20px;
    }
    
    /* Styl pro tabulku a řádky */
    .ticket-row {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Tagy pro statusy (Barvy podle tvého obrázku) */
    .status-badge {
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
    }
    .status-resise { background-color: #f1c40f33; color: #f1c40f; border: 1px solid #f1c40f; }
    .status-novy { background-color: #2ecc7133; color: #2ecc71; border: 1px solid #2ecc71; }
    
    /* Skrytí horní lišty Streamlitu */
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (LEVÝ PANEL) ---
with st.sidebar:
    # Logo a název (nahraď URL tvým logem)
    st.image("logo.jpg", width=100)
    st.markdown("### Community Roleplay\n**ADMIN PANEL**")
    st.write("---")
    
    # Menu (Tlačítka)
    st.button("🏠 Přehled", use_container_width=True)
    st.button("🎫 Tikety", type="primary", use_container_width=True)
    st.button("👤 Moje Tikety", use_container_width=True)
    st.button("📁 Archiv", use_container_width=True)
    st.button("⚙️ Nastavení", use_container_width=True)
    
    st.write("---")
    # Stav serveru (spodní část)
    st.markdown("STAV SERVERU: <span style='color:#2ecc71'>● ONLINE</span>", unsafe_allow_html=True)
    st.progress(1/64)
    st.caption("1 / 64 Hráčů")

# --- HLAVNÍ OBSAH (TABULKA TIKETŮ) ---
st.title("Tikety podpory")

# Horní lišta s filtrem a hledáním
col_title, col_filter, col_search = st.columns([2, 1, 1])
with col_filter:
    st.selectbox("", ["Všechny stavy", "Nové", "Řeší se", "Uzavřené"], label_visibility="collapsed")
with col_search:
    st.text_input("", placeholder="Hledat tikety...", label_visibility="collapsed")

# Záhlaví tabulky
st.markdown("""
<div style='display: flex; color: #8b949e; font-size: 12px; font-weight: bold; padding: 10px 20px;'>
    <div style='flex: 0.5;'>ID</div>
    <div style='flex: 1.5;'>HRÁČ</div>
    <div style='flex: 1.5;'>KATEGORIE</div>
    <div style='flex: 1;'>STAV</div>
    <div style='flex: 2;'>VYTVOŘENO</div>
    <div style='flex: 1; text-align: right;'>AKCE</div>
</div>
""", unsafe_allow_html=True)

# Funkce pro simulaci/načtení dat
def show_ticket_row(id, hrac, kat, stav, datum):
    status_class = "status-resise" if stav == "Řeší se" else "status-novy"
    st.markdown(f"""
    <div class="ticket-row">
        <div style='flex: 0.5;'>#{id}</div>
        <div style='flex: 1.5;'>{hrac}</div>
        <div style='flex: 1.5;'><span style='background:#30363d; padding:2px 8px; border-radius:4px;'>{kat}</span></div>
        <div style='flex: 1;'><span class="status-badge {status_class}">{stav}</span></div>
        <div style='flex: 2;'>{datum}</div>
        <div style='flex: 1; text-align: right; color: #a855f7; cursor: pointer;'>Otevřít →</div>
    </div>
    """, unsafe_allow_html=True)

# Zobrazení testovacích dat (pak se nahradí databází)
show_ticket_row(6, "xxexitusxx", "frakce", "Řeší se", "2026-03-07 17:02:50")
show_ticket_row(5, "razor_21", "razor", "Řeší se", "2026-03-07 16:28:02")
show_ticket_row(3, "xxexitusxx", "Frakce", "Řeší se", "2026-03-07 10:59:33")
show_ticket_row(2, "CopRoleplay", "Frakce", "Nový", "2026-03-07 08:09:41")

if st.button("Zobrazit vše", use_container_width=True):
    pass
