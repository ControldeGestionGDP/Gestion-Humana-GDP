import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="⚡")

# 2. CREDENCIALES
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. CSS TECNOLÓGICO Y LIMPIO (Upgrade 2026)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
    }

    .stApp {
        background: radial-gradient(circle at bottom left, #ffffff, #f0f4f8);
    }

    /* TÍTULO CON TOQUE TECNOLÓGICO */
    .tech-title {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(90deg, #1071b8, #c4579b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
        font-weight: 600;
        letter-spacing: 2px;
    }

    /* TARJETAS CON EFECTO DE VIDRIO (GLASSMORPHISM) */
    .tech-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(16, 113, 184, 0.1);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
        transition: all 0.4s ease;
        margin-bottom: 15px;
    }
    
    .tech-card:hover {
        border: 1px solid #1071b8;
        transform: translateY(-5px);
        box-shadow: 0 10px 40px rgba(16, 113, 184, 0.15);
    }

    /* BOTONES ESTILO FUTURISTA */
    div.stButton > button {
        border-radius: 12px !important;
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        color: #1e293b !important;
        font-weight: 600 !important;
        padding: 10px 20px !important;
        transition: all 0.3s !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02) !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #1071b8, #2e3788) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 8px 15px rgba(16, 113, 184, 0.3) !important;
    }

    /* LISTA DE REPORTES CON NEÓN IZQUIERDO */
    .report-item-tech {
        background: white;
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 5px solid #1071b8;
        margin-bottom: 1rem;
        transition: 0.3s;
    }
    .report-item-tech:hover {
        border-left: 5px solid #c4579b;
        background: #fcfcfd;
    }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# HEADER TECNOLÓGICO
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 20px 0; margin-bottom: 20px;">
        <div>
            <span class="tech-title">DON POLLO</span>
            <p style='margin:0; color:#64748b; font-size:0.85rem; letter-spacing:4px;'>COMMAND CENTER 2026</p>
        </div>
        <div style='text-align:right; border-left: 1px solid #ddd; padding-left: 20px;'>
            <p style='margin:0; font-size: 0.7rem; color: #94a3b8;'>SYSTEM STATUS</p>
            <p style='margin:0; font-size: 0.8rem; color: #10b981; font-weight:700;'>● ONLINE / ENCRIPTADO</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# =========================================================
# VISTA 1: HOME (PANELES TECH)
# =========================================================
if st.session_state.view == 'home':
    st.markdown("<h4 style='color:#1e293b; font-weight:400; margin-bottom:30px;'>Seleccione el terminal de datos:</h4>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="tech-card">
            <h2 style='margin-bottom:10px;'>💼</h2>
            <h4 style='margin:0; color:#1071b8;'>NÓMINAS</h4>
            <p style='color:#64748b; font-size:0.85rem; margin-top:10px;'>Análisis de compensaciones, asistencia y ciclos de descanso.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("ABRIR TERMINAL", key="btn_nom", use_container_width=True):
            st.session_state.view = 'nominas'; st.rerun()

    with col2:
        st.markdown("""<div class="tech-card">
            <h2 style='margin-bottom:10px;'>🦺</h2>
            <h4 style='margin:0; color:#1071b8;'>SEGURIDAD</h4>
            <p style='color:#64748b; font-size:0.85rem; margin-top:10px;'>Gestión de riesgos ocupacionales y cumplimiento SST.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("ABRIR TERMINAL", key="btn_sst", use_container_width=True):
            st.session_state.view = 'sst'; st.rerun()

    with col3:
        st.markdown("""<div class="tech-card">
            <h2 style='margin-bottom:10px;'>📈</h2>
            <h4 style='margin:0; color:#1071b8;'>DESARROLLO</h4>
            <p style='color:#64748b; font-size:0.85rem; margin-top:10px;'>Métricas de talento, clima y KPIs de desempeño.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("ABRIR TERMINAL", key="btn_dev", use_container_width=True):
            st.session_state.view = 'desarrollo'; st.rerun()

# =========================================================
# VISTA 2: ACCESO Y DASHBOARDS
# =========================================================
else:
    area = st.session_state.view
    
    c_nav1, c_nav2 = st.columns([1, 6])
    with c_nav1:
        if st.button("⬅ VOLVER"):
            st.session_state.view = 'home'; st.session_state.auth = False; st.rerun()
    with c_nav2:
        st.write(f"### ACCESO AL NODO: {area.upper()}")

    if not st.session_state.auth:
        st.markdown("<br>", unsafe_allow_html=True)
        _, col_login, _ = st.columns([1.2, 1, 1.2])
        with col_login:
            st.markdown(f"""<div style='text-align:center; padding:20px; background:white; border-radius:20px; border:1px solid #eee;'>
                <p style='color:#64748b; font-size:0.9rem;'>Área protegida: <b>{area.upper()}</b></p>
            </div>""", unsafe_allow_html=True)
            pw = st.text_input("PASSWORD GERENCIAL", type="password")
            if st.button("AUTENTICAR", use_container_width=True):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True; st.rerun()
                else: st.error("TOKEN INCORRECTO")
    
    else:
        st.markdown("<br><p style='color:#64748b;'>Seleccione el reporte en tiempo real:</p>", unsafe_allow_html=True)
        
        def tech_report_link(name, description, link):
            with st.container():
                c_info, c_link = st.columns([4, 1.2])
                with c_info:
                    st.markdown(f"""<div class="report-item-tech">
                        <p style='margin:0; font-weight:700; color:#2e3788;'>{name}</p>
                        <p style='margin:0; font-size:0.8rem; color:#64748b;'>{description}</p>
                    </div>""", unsafe_allow_html=True)
                with c_link:
                    st.write("") # Alineación
                    st.link_button("VISUALIZAR", link, use_container_width=True)

        if area == "nominas":
            tech_report_link("📊 Dashboard Vacaciones", "Saldos proyectados y programación de planta.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            tech_report_link("📈 Gestión de Descansos", "Análisis de licencias y días no laborados.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
        elif area == "sst":
            tech_report_link("⚠️ Control Accidentabilidad", "Kpis críticos de seguridad laboral.", "#")
            tech_report_link("📋 Auditorías SST", "Seguimiento de hallazgos por sede.", "#")
        elif area == "desarrollo":
            tech_report_link("🎓 Avance Formación", "Cumplimiento del Plan Anual de Capacitación.", "#")
            tech_report_link("💎 Clima y Cultura", "Resultados consolidados de encuestas.", "#")

# FOOTER FINAL
st.markdown("""
    <div style="margin-top: 50px; text-align: center; opacity: 0.5; font-size: 0.7rem;">
        <hr style="border:0.5px solid #eee;">
        GRUPO DON POLLO | DATA INTELLIGENCE DEPT. | ENCRYPTED CONNECTION
    </div>
""", unsafe_allow_html=True)
