import streamlit as st

# 1. Konfigurace stránky
st.set_page_coimport streamlit as st

# 1. Čistý start bez okrajů
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 2. BRUTÁLNÍ CSS (Přepíše Streamlit na tvůj Dashboard)
st.markdown("""
    <style>
    /* Odstranění Streamlit prvků */
    [data-testid="stHeader"], [data-testid="stSidebar"], .stDeployButton, #MainMenu {display: none !important;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    .stApp {background-color: #0d1117;}

    /* DASHBOARD LAYOUT */
    .dashboard {
        display: flex;
        min-height: 100vh;
        font-family: 'Inter', sans-serif;
        color: #e6edf3;
    }

    /* SIDEBAR */
    .sidebar {
        width: 260px;
        background: #161b22;
        border-right: 1px solid #30363d;
        padding: 24px;
        display: flex;
        flex-direction: column;
    }

    .nav-item {
        padding: 12px 16px;
        border-radius: 6px;
        color: #8b949e;
        text-decoration: none;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        transition: 0.2s;
    }
    .nav-item:hover { background: #21262d; color: white; }
    .nav-item.active { background: #7c3aed22; color: #a855f7; border-left: 3px solid #a855f7; }

    /* OBSAH */
    .content {
        flex: 1;
        padding: 40px;
        background: #0d1117;
    }

    /* KARTA S TIKETY */
    .card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }

    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th { text-align: left; color: #8b949e; font-size: 12px; text-transform: uppercase; padding-bottom: 15px; border-bottom: 1px solid #30363d; }
    td { padding: 16px 0; border-bottom: 1px solid #21262d; font-size: 14px; }

    /* STATUSY */
    .badge { padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
    .resise { color: #f1c40f; background: rgba(241,196,15,0.1); border: 1px solid #f1c40f; }
    .novy { color: #2ecc71; background: rgba(46,204,113,0.1); border: 1px solid #2ecc71; }
    
    .action-btn { color: #a855f7; cursor: pointer; font-weight: bold; }
    </style>

    <div class="dashboard">
        <div class="sidebar">
            <div style="margin-bottom: 40px; text-align: center;">
                <h2 style="margin:0; font-size: 20px;">Community RP</h2>
                <div style="color: #a855f7; font-size: 10px; font-weight: bold; letter-spacing: 2px;">ADMIN PANEL</div>
            </div>
            
            <div class="nav-item">🏠 Přehled</div>
            <div class="nav-item active">🎫 Tikety</div>
            <div class="nav-item">👤 Moje Tikety</div>
            <div class="nav-item">📁 Archiv</div>
            <div class="nav-item">⚙️ Nastavení</div>

            <div style="margin-top: auto; background: #0d1117; padding: 16px; border-radius: 12px; border: 1px solid #30363d;">
                <div style="display:flex; justify-content: space-between; font-size: 10px; color: #8b949e; margin-bottom: 8px;">
                    <span>STAV SERVERU</span>
                    <span style="color: #2ecc71;">● ONLINE</span>
                </div>
                <div style="font-size: 16px; font-weight: bold; margin-bottom: 8px;">1 / 64 Hráčů</div>
                <div style="width: 100%; background: #30363d; height: 4px; border-radius: 2px;">
                    <div style="width: 2%; background: #a855f7; height: 100%; border-radius: 2px;"></div>
                </div>
            </div>
        </div>

        <div class="content">
            <h1 style="margin-bottom: 24px; font-size: 28px;">Tikety podpory</h1>
            
            <div class="card">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>HRÁČ</th>
                            <th>KATEGORIE</th>
                            <th>STAV</th>
                            <th>VYTVOŘENO</th>
                            <th style="text-align: right;">AKCE</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>#6</td>
                            <td>xxexitusxx</td>
                            <td><span style="background: #21262d; padding: 4px 8px; border-radius: 4px;">frakce</span></td>
                            <td><span class="badge resise">Řeší se</span></td>
                            <td style="color: #8b949e;">2026-03-07 17:02:50</td>
                            <td style="text-align: right;"><span class="action-btn">Otevřít →</span></td>
                        </tr>
                        <tr>
                            <td>#5</td>
                            <td>razor_21</td>
                            <td><span style="background: #21262d; padding: 4px 8px; border-radius: 4px;">razor</span></td>
                            <td><span class="badge resise">Řeší se</span></td>
                            <td style="color: #8b949e;">2026-03-07 16:28:02</td>
                            <td style="text-align: right;"><span class="action-btn">Otevřít →</span></td>
                        </tr>
                        <tr>
                            <td>#2</td>
                            <td>CopRoleplay</td>
                            <td><span style="background: #21262d; padding: 4px 8px; border-radius: 4px;">Frakce</span></td>
                            <td><span class="badge novy">Nový</span></td>
                            <td style="color: #8b949e;">2026-03-07 08:09:41</td>
                            <td style="text-align: right;"><span class="action-btn">Otevřít →</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)nfig(page_title="CRP Admin", layout="wide", initial_sidebar_state="expanded")

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
