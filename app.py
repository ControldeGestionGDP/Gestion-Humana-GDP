import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="⚡")

# 2. CREDENCIALES
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. CSS MAESTRO (TODO EL ESTILO EN UN SOLO BLOQUE)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@300;400;600;800&display=swap');
    
    /* Fuente General */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
    }

    /* Fondo */
    .stApp {
        background: radial-gradient(circle at top right, #ffffff, #f0f4f8);
    }

    /* Título Principal */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        padding-top: 20px;
    }

    /* SUBTÍTULO */
    .sub-title {
        text-align: center;
        color: #64748b;
        letter-spacing: 3px;
        font-weight: 300;
        margin-bottom: 60px;
        text-transform: uppercase;
    }

    /* DISEÑO DE BOTONES TIPO CÍRCULO */
    div.stButton > button {
        width: 280px !important;
        height: 280px !important;
        border-radius: 50% !important;
        background-color: white !important;
        border: 2px solid rgba(16, 113, 184, 0.2) !important;
        color: #2e3788 !important;
        font-weight: 800 !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05) !important;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1) !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        margin: auto !important;
        white-space: pre-wrap !important; /* Permite saltos de línea */
        line-height: 1.2 !important;
    }

    /* HOVER DE LOS CÍRCULOS */
    div.stButton > button:hover {
        transform: translateY(-15px) scale(1.02) !important;
        border-color: #c4579b !important;
        box-shadow: 0 25px 50px rgba(196, 87, 155, 0.15) !important;
        color: #c4579b !important;
    }

    /* TARJETAS DE DASHBOARD INTERNO */
    .card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        border: 1px solid #eef2f6;
        padding: 40px 25px;
        text-align: center;
        transition: 0.4s;
        height: 380px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }
    .card:hover {
        transform: translateY(-10px);
        border-color: #c4579b;
        background: white;
    }

    /* BOTONES DE LANZAMIENTO POWER BI */
    .launch-btn {
        background: linear-gradient(135deg, #1071b8, #2e3788);
        color: white !important;
        padding: 12px 28px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        margin-top: 25px;
    }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN (Session State)
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

def navigate_to(area):
    st.session_state.view = area
    st.session_state.auth = False

# =========================================================
# VISTA 1: HOME (PANELES CIRCULARES)
# =========================================================
if st.session_state.view == 'home':
    st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">INTELIGENCIA ESTRATÉGICA | DON POLLO</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Usamos emojis y texto con saltos de línea para que se vean bien dentro del círculo
        if st.button("💼\n\nNÓMINAS", key="btn_nom"):
            navigate_to('nominas')
            st.rerun()

    with col2:
        if st.button("🦺\n\nSEGURIDAD", key="btn_sst"):
            navigate_to('sst')
            st.rerun()

    with col3:
        if st.button("📈\n\nDESARROLLO", key="btn_dev"):
            navigate_to('desarrollo')
            st.rerun()

# =========================================================
# VISTA 2: LOGIN Y DASHBOARDS DETALLADOS
# =========================================================
else:
    # Botón superior para regresar
    if st.button("⬅️ VOLVER AL PANEL PRINCIPAL"):
        st.session_state.view = 'home'
        st.session_state.auth = False
        st.rerun()

    area = st.session_state.view
    
    # --- SUB-VISTA A: PANTALLA DE CONTRASEÑA ---
    if not st.session_state.auth:
        st.markdown(f"<h2 style='text-align:center; color:#2e3788; margin-top:50px;'>🔐 ACCESO RESTRINGIDO</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; color:#64748b;'>Usted está intentando ingresar a: <b>{area.upper()}</b></p>", unsafe_allow_html=True)
        
        _, col_login, _ = st.columns([1.2, 1, 1.2])
        with col_login:
            st.write("---")
            pw = st.text_input("Ingrese Clave Gerencial", type="password")
            if st.button("VALIDAR CREDENCIALES"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("❌ Clave incorrecta. Intente de nuevo.")
    
    # --- SUB-VISTA B: DASHBOARD AUTORIZADO ---
    else:
        st.markdown(f"<h2 style='font-weight:800; color:#2e3788;'>Gestión Estratégica: {area.upper()}</h2>", unsafe_allow_html=True)
        st.write("---")
        
        # Función para crear las tarjetas internas de Power BI
        def render_card(icon, title, desc, link):
            st.markdown(f"""
                <div class="card">
                    <div style="font-size:55px; margin-bottom:15px;">{icon}</div>
                    <h3 style="color:#2e3788; font-weight:800; margin:0;">{title}</h3>
                    <p style="color:#64748b; font-size:0.95rem; margin-top:15px;">{desc}</p>
                    <a href="{link}" target="_blank" class="launch-btn">ABRIR REPORTE BI</a>
                </div>
            """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        
        if area == "nominas":
            with c1: render_card("🏖️", "VACACIONES", "Saldos pendientes, programación anual y flujos de descanso.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            with c2: render_card("🚑", "DESCANSOS", "Trazabilidad de licencias médicas, ausentismo y salud ocupacional.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with c3: render_card("⏰", "ASISTENCIA", "Monitor de puntualidad, horas extra y cumplimiento de turnos.", "#")
        
        elif area == "sst":
            with c1: render_card("⚠️", "INCIDENTES", "Reporte de accidentabilidad y actos inseguros en planta.", "#")
            with c2: render_card("🩹", "SST CORE", "Indicadores de cumplimiento normativo y legal vigente.", "#")
            with c3: render_card("🏢", "AUDITORÍAS", "Inspecciones de seguridad en sedes y oficinas administrativas.", "#")
            
        elif area == "desarrollo":
            with c1: render_card("🎓", "FORMACIÓN", "Avance del Plan Anual de Capacitación y competencias.", "#")
            with c2: render_card("😊", "CULTURA", "Medición de clima organizacional y niveles de compromiso.", "#")
            with c3: render_card("🎯", "KPIS", "Evaluación de desempeño por objetivos y metas anuales.", "#")

# 5. FOOTER
st.markdown("""
    <div style="margin-top: 80px; text-align: center; border-top: 1px solid #eef2f6; padding-top: 30px;">
        <p style="color: #94a3b8; font-size: 0.8rem; font-weight: 500; letter-spacing: 1px;">
            GRUPO <span style="color:#1071b8">DON POLLO</span> | UNIDAD DE INTELIGENCIA CORPORATIVA © 2026
        </p>
    </div>
""", unsafe_allow_html=True)
