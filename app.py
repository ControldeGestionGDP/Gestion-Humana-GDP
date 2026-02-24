import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="⚡")

# 2. CREDENCIALES
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. EL "OUTFIT" DE LA WEB (CSS PREMIUM REPARADO)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {{
        font-family: 'Inter', sans-serif !important;
    }}

    .stApp {{
        background: radial-gradient(circle at top right, #ffffff, #f0f4f8);
    }}

    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: -50px;
        margin-bottom: 10px;
    }}

    /* REPARACIÓN DEL CLIC: El botón ahora contiene el diseño del círculo */
    div.stButton > button {{
        width: 280px !important;
        height: 280px !important;
        border-radius: 50% !important;
        background: white !important;
        border: 1px solid rgba(16, 113, 184, 0.2) !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05) !important;
        transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1) !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        margin: auto !important;
        padding: 0 !important;
    }}

    div.stButton > button:hover {{
        transform: translateY(-15px) scale(1.05) !important;
        border-color: #c4579b !important;
        box-shadow: 0 20px 50px rgba(196, 87, 155, 0.2) !important;
    }}

    /* Estilo para los textos dentro del botón-círculo */
    .btn-emoji {{ font-size: 70px; margin-bottom: 5px; display: block; }}
    .btn-text {{ 
        font-weight: 700; 
        color: #2e3788; 
        font-size: 1.1rem; 
        letter-spacing: 1px; 
        text-transform: uppercase;
        font-family: 'Inter', sans-serif;
    }}

    /* Tarjetas de Datos (Vista Interna) */
    .card {{
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,0.4);
        padding: 40px 25px;
        text-align: center;
        transition: 0.4s;
        height: 360px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }}
    .card:hover {{
        transform: translateY(-10px);
        background: white;
        border-color: #c4579b;
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    }}

    .launch-btn {{
        background: linear-gradient(135deg, #1071b8, #2e3788);
        color: white !important;
        padding: 12px 28px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        margin-top: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

def navigate_to(area):
    st.session_state.view = area
    st.session_state.auth = False

# =========================================================
# VISTA 1: HOME
# =========================================================
if st.session_state.view == 'home':
    st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; letter-spacing:2px; font-weight:300; margin-bottom:60px;'>INTELIGENCIA DE DATOS | DON POLLO</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        # Inyectamos el diseño dentro del botón nativo
        if st.button("💼", key="nom_btn"):
            navigate_to('nominas')
            st.rerun()
        st.markdown('<p style="text-align:center; font-weight:700; color:#2e3788; margin-top:-140px; pointer-events:none; position:relative; z-index:20;">NÓMINAS</p>', unsafe_allow_html=True)

    with c2:
        if st.button("🦺", key="sst_btn"):
            navigate_to('sst')
            st.rerun()
        st.markdown('<p style="text-align:center; font-weight:700; color:#2e3788; margin-top:-140px; pointer-events:none; position:relative; z-index:20;">SEGURIDAD</p>', unsafe_allow_html=True)

    with c3:
        if st.button("📈", key="dev_btn"):
            navigate_to('desarrollo')
            st.rerun()
        st.markdown('<p style="text-align:center; font-weight:700; color:#2e3788; margin-top:-140px; pointer-events:none; position:relative; z-index:20;">DESARROLLO</p>', unsafe_allow_html=True)

    # Espaciador para corregir el layout debido al margen negativo
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)

# =========================================================
# VISTA 2: LOGIN Y DASHBOARDS
# =========================================================
else:
    if st.button("⬅️ INICIO"):
        st.session_state.view = 'home'
        st.rerun()

    area = st.session_state.view
    
    if not st.session_state.auth:
        st.markdown(f"<h2 style='text-align:center; font-weight:800; color:#2e3788; margin-top:40px;'>🔐 ACCESO RESTRINGIDO</h2>", unsafe_allow_html=True)
        col_x, col_login, col_z = st.columns([1.2, 1, 1.2])
        with col_login:
            pw = st.text_input(f"Clave para {area.upper()}", type="password")
            if st.button("AUTENTICAR"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Clave incorrecta")
    
    else:
        st.markdown(f"<h2 style='font-weight:800; color:#2e3788;'>Gestión de {area.upper()}</h2>", unsafe_allow_html=True)
        st.write("---")
        
        def render_card(icon, title, desc, link):
            st.markdown(f"""
                <div class="card">
                    <div style="font-size:55px; margin-bottom:15px;">{icon}</div>
                    <h3 style="color:#2e3788; font-weight:800; margin:0;">{title}</h3>
                    <p style="color:#64748b; font-size:0.95rem; margin-top:15px;">{desc}</p>
                    <a href="{link}" target="_blank" class="launch-btn">VER REPORTE BI</a>
                </div>
            """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        if area == "nominas":
            with c1: render_card("🏖️", "VACACIONES", "Análisis de saldos y programación.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            with c2: render_card("🚑", "DESCANSOS", "Trazabilidad de licencias médicas.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with c3: render_card("⏰", "ASISTENCIA", "Monitor de puntualidad.", "#")
        elif area == "sst":
            with c1: render_card("⚠️", "ACCIDENTES", "Reporte de incidentes.", "#")
            with c2: render_card("🩹", "SST CORE", "Cumplimiento legal.", "#")
            with c3: render_card("🏢", "AUDITORÍAS", "Inspecciones sedes.", "#")
        elif area == "desarrollo":
            with c1: render_card("🎓", "FORMACIÓN", "Avance Plan de Capacitación.", "#")
            with c2: render_card("😊", "CULTURA", "Clima y compromiso.", "#")
            with c3: render_card("🎯", "KPIS", "Evaluación de desempeño.", "#")

# FOOTER
st.markdown(f"""
    <div style="margin-top: 80px; text-align: center; border-top: 1px solid #eef2f6; padding-top: 30px;">
        <p style="color: #94a3b8; font-size: 0.8rem; font-weight: 500; letter-spacing: 1px;">
            GRUPO <span style="color:#1071b8">DON POLLO</span> | 2026
        </p>
    </div>
""", unsafe_allow_html=True)
