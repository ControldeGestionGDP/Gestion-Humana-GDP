import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Gestión Corporativa | Don Pollo", layout="wide", page_icon="🐔")

# 2. CREDENCIALES
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. CSS INDUSTRIAL (Sólido, Limpio y Corporativo)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;600;800&family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
    }

    /* Fondo gris muy tenue, estilo oficina/planta */
    .stApp {
        background-color: #f4f7f9;
    }

    /* HEADER TIPO LOGO CORPORATIVO */
    .header-box {
        background-color: #ffffff;
        padding: 1.5rem 2rem;
        border-bottom: 4px solid #1071b8; /* El azul de Don Pollo */
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .brand-title {
        font-family: 'Barlow', sans-serif;
        font-weight: 800;
        font-size: 2rem;
        color: #1a365d;
        margin: 0;
        display: flex;
        align-items: center;
    }

    /* TARJETAS DE ÁREA (Sólidas y Profesionales) */
    .area-card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #d1d5db;
        transition: 0.3s;
        height: 100%;
    }
    
    .area-card:hover {
        border-color: #1071b8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* BOTONES ACCIÓN DIRECTA */
    div.stButton > button {
        border-radius: 4px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 700 !important;
        background-color: #1071b8 !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    div.stButton > button:hover {
        background-color: #0d5a94 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    }

    /* LISTA DE REPORTES */
    .report-container {
        background: #ffffff;
        padding: 1rem;
        border-radius: 6px;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# HEADER CORPORATIVO (Aterrizado)
st.markdown("""
    <div class="header-box">
        <div>
            <h1 class="brand-title">🐔 DON POLLO <span style="color:#1071b8; margin-left:10px; font-weight:400;">| BI</span></h1>
            <p style="margin:0; color:#64748b; font-size:0.85rem; font-weight:600;">PORTAL DE GESTIÓN OPERATIVA</p>
        </div>
        <div style="text-align: right;">
            <p style="margin:0; font-size:0.8rem; color:#1e293b; font-weight:700;">AVÍCOLA DON POLLO S.A.</p>
            <p style="margin:0; font-size:0.75rem; color:#64748b;">Actualizado: 2026</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# =========================================================
# VISTA 1: HOME (ÁREAS CLARAS)
# =========================================================
if st.session_state.view == 'home':
    st.markdown("<h3 style='color:#1a365d; margin-bottom:1.5rem;'>Módulos de Control</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="area-card">
                <h4 style="color:#1071b8; margin-top:0;">NÓMINAS Y PERSONAL</h4>
                <p style="color:#4b5563; font-size:0.9rem;">Control de asistencia, vacaciones y planillas del personal de planta y campo.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ENTRAR A NÓMINAS", key="btn_nom"):
            st.session_state.view = 'nominas'; st.rerun()

    with col2:
        st.markdown("""
            <div class="area-card">
                <h4 style="color:#1071b8; margin-top:0;">SEGURIDAD (SST)</h4>
                <p style="color:#4b5563; font-size:0.9rem;">Monitoreo de accidentes, seguridad industrial y cumplimiento normativo.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ENTRAR A SEGURIDAD", key="btn_sst"):
            st.session_state.view = 'sst'; st.rerun()

    with col3:
        st.markdown("""
            <div class="area-card">
                <h4 style="color:#1071b8; margin-top:0;">DESARROLLO HUMANO</h4>
                <p style="color:#4b5563; font-size:0.9rem;">Indicadores de desempeño, clima laboral y planes de capacitación.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ENTRAR A DESARROLLO", key="btn_dev"):
            st.session_state.view = 'desarrollo'; st.rerun()

# =========================================================
# VISTA 2: ACCESO Y REPORTES
# =========================================================
else:
    area = st.session_state.view
    
    c1, c2 = st.columns([1, 4])
    with c1:
        if st.button("⬅ VOLVER"):
            st.session_state.view = 'home'; st.session_state.auth = False; st.rerun()
    with c2:
        st.subheader(f"Panel: {area.upper()}")

    if not st.session_state.auth:
        st.markdown("---")
        _, col_log, _ = st.columns([1, 1, 1])
        with col_log:
            st.info("🔐 Ingrese clave de seguridad")
            pw = st.text_input("Contraseña", type="password")
            if st.button("VALIDAR ACCESO"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True; st.rerun()
                else: st.error("Clave incorrecta")
    
    else:
        st.markdown("---")
        st.markdown("#### Reportes Disponibles")
        
        def display_report(name, detail, url):
            st.markdown(f"""
                <div class="report-container">
                    <p style="margin:0; font-weight:700; color:#1a365d;">{name}</p>
                    <p style="margin:0; font-size:0.85rem; color:#6b7280;">{detail}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"VER REPORTE DE {name.upper()}", url, use_container_width=True)
            st.write("")

        if area == "nominas":
            display_report("Vacaciones", "Reporte consolidado de días pendientes y programados.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            display_report("Descansos Médicos", "Seguimiento de ausentismo y licencias médicas.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
        elif area == "sst":
            display_report("Accidentabilidad", "Kpis mensuales de incidentes en planta.", "#")
        elif area == "desarrollo":
            display_report("Capacitación", "Avance de horas hombre entrenadas.", "#")

# FOOTER
st.markdown("""
    <div style="margin-top: 5rem; text-align: center; border-top: 1px solid #d1d5db; padding: 20px;">
        <p style="color: #6b7280; font-size: 0.8rem; font-weight: 600;">© 2026 AVÍCOLA DON POLLO S.A. - SISTEMAS DE INFORMACIÓN</p>
    </div>
""", unsafe_allow_html=True)
