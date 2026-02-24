import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Máxima limpieza visual)
st.set_page_config(page_title="Don Pollo | Business Intelligence", layout="wide", page_icon="📊")

# 2. SISTEMA DE SEGURIDAD
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. CSS "EXECUTIVE PREMIUM" (Diseño de alto impacto)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #fcfcfd;
    }

    /* Contenedor Principal */
    .stApp {
        background: radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.03) 0, transparent 50%), 
                    radial-gradient(at 50% 0%, rgba(16, 185, 129, 0.01) 0, transparent 50%);
    }

    /* HEADER CORPORATIVO */
    .main-header {
        background: white;
        padding: 1.5rem 3rem;
        border-radius: 25px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 3rem;
    }

    .logo-text {
        font-size: 1.6rem;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.5px;
    }

    /* TARJETAS EJECUTIVAS */
    .card-executive {
        background: white;
        padding: 2.5rem 2rem;
        border-radius: 30px;
        border: 1px solid #f1f5f9;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: center;
    }
    
    .card-executive:hover {
        transform: translateY(-10px);
        box-shadow: 0 30px 50px -10px rgba(0,0,0,0.08);
        border-color: #3b82f6;
    }

    /* BOTONES DE LUJO */
    div.stButton > button {
        border-radius: 14px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        background: #0f172a !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background: #3b82f6 !important;
        box-shadow: 0 10px 20px -5px rgba(59, 130, 246, 0.4) !important;
        transform: scale(1.02);
    }

    /* LISTADO DE REPORTES */
    .report-box {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        border-left: 6px solid #0f172a;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
    }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# HEADER CORPORATIVO
st.markdown("""
    <div class="main-header">
        <div>
            <span class="logo-text">DON POLLO <span style="color:#3b82f6;">BI</span></span>
            <p style="margin:0; color:#64748b; font-size:0.8rem; font-weight:500;">SISTEMA INTEGRAL DE GESTIÓN</p>
        </div>
        <div style="text-align:right;">
            <span style="color:#10b981; font-size:0.75rem; font-weight:700;">● CONEXIÓN SEGURA</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# =========================================================
# VISTA 1: MENÚ DE CONTROL (HOME)
# =========================================================
if st.session_state.view == 'home':
    st.markdown("<h2 style='text-align:center; color:#0f172a; font-weight:800; margin-bottom:3rem;'>Dirección Estratégica</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown('<div class="card-executive"><p style="font-size:2.5rem; margin-bottom:1rem;">💼</p><h3 style="color:#0f172a; margin-bottom:1rem;">Nóminas</h3><p style="color:#64748b; font-size:0.9rem; margin-bottom:1.5rem;">Análisis de capital humano, vacaciones y asistencia.</p></div>', unsafe_allow_html=True)
        if st.button("Abrir División", key="btn_nom"):
            st.session_state.view = 'nominas'; st.rerun()

    with col2:
        st.markdown('<div class="card-executive"><p style="font-size:2.5rem; margin-bottom:1rem;">🦺</p><h3 style="color:#0f172a; margin-bottom:1rem;">Seguridad</h3><p style="color:#64748b; font-size:0.9rem; margin-bottom:1.5rem;">Indicadores de SST, accidentabilidad y normativas.</p></div>', unsafe_allow_html=True)
        if st.button("Abrir División", key="btn_sst"):
            st.session_state.view = 'sst'; st.rerun()

    with col3:
        st.markdown('<div class="card-executive"><p style="font-size:2.5rem; margin-bottom:1rem;">📈</p><h3 style="color:#0f172a; margin-bottom:1rem;">Desarrollo</h3><p style="color:#64748b; font-size:0.9rem; margin-bottom:1.5rem;">Capacitaciones, clima laboral y evaluación de talento.</p></div>', unsafe_allow_html=True)
        if st.button("Abrir División", key="btn_dev"):
            st.session_state.view = 'desarrollo'; st.rerun()

# =========================================================
# VISTA 2: ACCESO Y RECURSOS
# =========================================================
else:
    area = st.session_state.view
    
    # Barra de navegación interna
    c_back, c_title = st.columns([1, 5])
    with c_back:
        if st.button("← Volver"):
            st.session_state.view = 'home'; st.session_state.auth = False; st.rerun()
    with c_title:
        st.markdown(f"<h2 style='margin:0; color:#0f172a;'>División de {area.capitalize()}</h2>", unsafe_allow_html=True)

    if not st.session_state.auth:
        st.markdown("<br><br>", unsafe_allow_html=True)
        _, col_login, _ = st.columns([1.2, 1, 1.2])
        with col_login:
            st.markdown("<div style='text-align:center; margin-bottom:1rem;'>Protección de Datos Gerenciales</div>", unsafe_allow_html=True)
            pw = st.text_input("Ingrese su contraseña", type="password", label_visibility="collapsed")
            if st.button("Validar Credenciales"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True; st.rerun()
                else: st.error("Acceso denegado: Clave incorrecta")
    
    else:
        st.markdown("<br><p style='color:#64748b;'>Panel de reportes autorizados:</p>", unsafe_allow_html=True)
        
        def render_report_row(name, detail, url):
            st.markdown(f"""
                <div class="report-box">
                    <p style="margin:0; font-weight:800; color:#0f172a; font-size:1.1rem;">{name}</p>
                    <p style="margin:0; font-size:0.85rem; color:#64748b;">{detail}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Abrir Dashboard {name}", url, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)

        if area == "nominas":
            render_report_row("Gestión de Vacaciones", "Saldos pendientes y programación anual por sede.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            render_report_row("Descansos Médicos", "Reporte de ausentismo y licencias registradas.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
        elif area == "sst":
            render_report_row("Incidentes y SST", "Monitoreo de accidentes y actos inseguros.", "#")
        elif area == "desarrollo":
            render_report_row("Plan de Capacitación", "Avance de formación y cumplimiento de metas.", "#")

# FOOTER PROFESIONAL
st.markdown("""
    <div style="margin-top: 5rem; padding: 2rem; border-top: 1px solid #f1f5f9; text-align: center;">
        <p style="color: #94a3b8; font-size: 0.75rem; font-weight: 600; letter-spacing: 1px;">AVÍCOLA DON POLLO S.A. • 2026</p>
    </div>
""", unsafe_allow_html=True)
