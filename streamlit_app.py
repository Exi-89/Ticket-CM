import streamlit as st

# 1. Konfigurace stránky
st.set_page_config(page_title="CRP Admin", layout="wide", initial_sidebar_state="expanded")

# 2. KOMPLETNÍ DASHBOARD DESIGN (CSS + HTML)
st.markdown("""
    <style>
    /* Základní reset */
    .stApp { background-color: #0d1117; color: white; }
    header, footer { visibility: hidden; }
    [data-testid="stSidebar"] { display: none; } /* Schováme ten nefunkční default sidebar */
    
    /* Naše vlastní rozvržení */
    .main-wrapper {
        display: flex;
        margin-left: -5rem;
        margin-top: -5rem;
    }

    /* VLASTNÍ SIDEBAR */
    .custom-sidebar {
        width: 260px;
        height: 100vh;
        background: #161b22;
        border-right: 1px solid #30363d;
        position: fixed;
        display: flex;
        flex-direction: column;
        padding: 20px;
    }

    .nav-item {
        padding: 12px 15px;
        margin: 4px 0;
        border-radius: 8px;
        color: #8b949e;
        cursor: pointer;
        display: flex;
        align-items: center;
        text-decoration: none;
        transition: 0.2s;
    }
    .nav-item:hover { background: #21262d; color: white; }
    .nav-item.active { background: #7c3aed22; color: #a855f7; border-left: 3px solid #a855f7; }

    /* HLAVNÍ PLOCHA */
    .main-content {
        margin-left: 280px;
        padding: 40px;
        width: 100%;
    }

    /* KARTA S TIKETY */
    .ticket-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 24px;
    }

    .ticket-table { width: 100%; border-collapse: collapse; }
    .ticket-table th { text-align: left; color: #8b949e; padding-bottom: 15px; border-bottom: 1px solid #30363d; font-size: 13px; }
    .ticket-table td { padding: 15px 0; border-bottom: 1px solid #21262d; font-size: 14px; }

    .status-badge {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }
    .status-resise { color: #f1c40f; background: rgba(241, 196, 15, 0.1); border: 1px solid #f1c40f; }
    .status-novy { color: #2ecc71; background: rgba(46, 204, 113, 0.1); border: 1px solid #2ecc71; }
    
    .btn-open { color: #a855f7; text-decoration: none; font-weight: bold; cursor: pointer; }
    </style>

    <div class="main-wrapper">
        <div class="custom-sidebar">
            <div style="text-align:center; margin-bottom: 30px;">
                <h2 style="margin:0;">Community RP</h2>
                <small style="color: #a855f7; letter-spacing: 2px;">ADMIN PANEL</small>
            </div>
            
            <a class="nav-item">🏠 Přehled</a>
            <a class="nav-item active">🎫 Tikety</a>
            <a class="nav-item">👤 Moje Tikety</a>
            <a class="nav-item">📁 Archiv</a>
            <a class="nav-item">⚙️ Nastavení</a>

            <div style="margin-top: auto; background: #0d1117; padding: 15px; border-radius: 10px; border: 1px solid #30363d;">
                <div style="display:flex; justify-content: space-between; font-size: 11px; color: gray;">
                    <span>STAV SERVERU</span>
                    <span style="color: #2ecc71;">● ONLINE</span>
                </div>
                <div style="margin: 10px 0; font-weight: bold;">1 / 64 Hráčů</div>
                <div style="background:#30363d; height:4px; border-radius:2px;"><div style="width:2%; background:#a855f7; height:100%;"></div></div>
            </div>
        </div>

        <div class="main-content">
            <h1>Tikety podpory</h1>
            <div class="ticket-card">
                <h3 style="margin-top:0;">Nedávné tikety</h3>
                <table class="ticket-table">
                    <tr>
                        <th>ID</th>
                        <th>HRÁČ</th>
                        <th>KATEGORIE</th>
                        <th>STAV</th>
                        <th>VYTVOŘENO</th>
                        <th style="text-align:right;">AKCE</th>
                    </tr>
                    <tr>
                        <td>#6</td>
                        <td>xxexitusxx</td>
                        <td><span style="background:#30363d; padding:2px 6px; border-radius:4px;">frakce</span></td>
                        <td><span class="status-badge status-resise">Řeší se</span></td>
                        <td>2026-03-07 17:02:50</td>
                        <td style="text-align:right;"><span class="btn-open">Otevřít →</span></td>
                    </tr>
                    <tr>
                        <td>#5</td>
                        <td>razor_21</td>
                        <td><span style="background:#30363d; padding:2px 6px; border-radius:4px;">razor</span></td>
                        <td><span class="status-badge status-resise">Řeší se</span></td>
                        <td>2026-03-07 16:28:02</td>
                        <td style="text-align:right;"><span class="btn-open">Otevřít →</span></td>
                    </tr>
                    <tr>
                        <td>#2</td>
                        <td>CopRoleplay</td>
                        <td><span style="background:#30363d; padding:2px 6px; border-radius:4px;">Frakce</span></td>
                        <td><span class="status-badge status-novy">Nový</span></td>
                        <td>2026-03-07 08:09:41</td>
                        <td style="text-align:right;"><span class="btn-open">Otevřít →</span></td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
