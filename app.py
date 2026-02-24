import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="⚡")

# 2. CREDENCIALES
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. CSS DE ALTO NIVEL (Diseño Web Limpio)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif !important; }}
    .stApp {{ background: radial-gradient(circle at top right, #ffffff, #f0f4f8); }}

    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem; font-weight: 800; text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-top: -30px; margin-bottom: 5px;
    }}

    /* CONTENEDOR DE CÍRCULOS */
    .menu-container {{
        display: flex;
        justify-content: center;
        gap: 40px;
        padding-top: 50px;
    }}

    /* ESTILO DEL CÍRCULO (Como una web moderna) */
    .circle-card {{
        width: 280px; height: 280px;
        background: white;
        border-radius: 50%;
        border: 1px solid rgba(16, 113, 184, 0.2);
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        transition: all 0.5s ease;
        text-decoration: none !important;
    }}

    .circle-card:hover {{
        transform: translateY(-15px);
        border-color: #c4579b;
        box-shadow: 0 20px 50px rgba(196, 87, 155, 0.2);
    }}

    .circle-emoji {{ font-size: 70px; margin-bottom: 10px; }}
    .circle-label {{ 
        font-weight: 800; color: #2e3788; 
        letter-spacing: 1px; font-size: 1.1rem;
    }}

    /* TARJETAS INTERNAS */
    .card {{
        background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px);
        border-radius: 24px; padding: 40px; text-align: center;
        height: 350px; display: flex; flex-direction: column; justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03); border: 1px solid #eef2f6;
    }}
    .launch-btn {{
        background: linear-gradient(135deg, #1071b8, #2e3788);
        color: white !important; padding: 12px 25px; border-radius: 50px;
        text-decoration: none !important; font-weight: 600; margin-top: 20px;
        display: inline-block;
    }}
</style>
""", unsafe_allow_html=True)

# 4. INICIALIZACIÓN DE ESTADOS
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# =========================================================
# VISTA 1: HOME (PORTAL WEB)
# =========================================================
if st.session_state.view == 'home':
    st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; letter-spacing:2px;'>INTELIGENCIA DE DATOS | DON POLLO</p>", unsafe_allow_html=True)
    
    # Usamos columnas nativas pero inyectamos el HTML limpio
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="circle-card"><span class="circle-emoji">💼</span><span class="circle-label">NÓMINAS</span></div>', unsafe_allow_html=True)
        if st.button("ENTRAR A NÓMINAS", use_container_width=True):
            st.session_state.view = 'nominas'
            st.rerun()

    with col2:
        st.markdown('<div class="circle-card"><span class="circle-emoji">🦺</span><span class="circle-label">SEGURIDAD</span></div>', unsafe_allow_html=True)
        if st.button("ENTRAR A SEGURIDAD", use_container_width=True):
            st.session_state.view = 'sst'
            st.rerun()

    with col3:
        st.markdown('<div class="circle-card"><span class="circle-emoji">📈</span><span class="circle-label">DESARROLLO</span></div>', unsafe_allow_html=True)
        if st.button("ENTRAR A DESARROLLO", use_container_width=True):
            st.session_state.view = 'desarrollo'
            st.rerun()

# =========================================================
# VISTA 2: LOGIN Y DASHBOARDS
# =========================================================
else:
    if st.button("⬅️ VOLVER AL PANEL PRINCIPAL"):
        st.session_state.view = 'home'
        st.session_state.auth = False
        st.rerun()

    area = st.session_state.view
    
    if not st.session_state.auth:
        st.markdown(f"<h2 style='text-align:center; font-weight:800; color:#2e3788;'>🔒 ACCESO PRIVADO: {area.upper()}</h2>", unsafe_allow_html=True)
        _, col_login, _ = st.columns([1, 0.8, 1])
        with col_login:
            pw = st.text_input("Contraseña Gerencial", type="password")
            if st.button("CONECTAR"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Credencial incorrecta")
    else:
        st.markdown(f"<h2 style='font-weight:800; color:#2e3788;'>Dashboard {area.upper()}</h2>", unsafe_allow_html=True)
        
        def render_card(icon, title, desc, link):
            st.markdown(f"""
                <div class="card">
                    <div style="font-size:55px;">{icon}</div>
                    <h3 style="color:#2e3788; font-weight:800;">{title}</h3>
                    <p style="color:#64748b;">{desc}</p>
                    <a href="{link}" target="_blank" class="launch-btn">ABRIR POWER BI</a>
                </div>
            """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        if area == "nominas":
            with c1: render_card("🏖️", "VACACIONES", "Gestión de saldos y flujos de descanso.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            with c2: render_card("🚑", "DESCANSOS", "Monitoreo de licencias y ausentismo.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with c3: render_card("⏰", "ASISTENCIA", "Control de horas y puntualidad.", "#")
        # ... (SST y Desarrollo se mantienen igual con sus iconos respectivos)

# FOOTER
st.markdown("<br><br><p style='text-align:center; color:#94a3b8; font-size:0.8rem;'>GRUPO DON POLLO | 2026</p>", unsafe_allow_html=True)
