import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Modo Ancho para visión gerencial)
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="📈")

# 2. CREDENCIALES
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. CSS DE ALTA GAMA (ESTILO MINIMALISTA EMPRESARIAL)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
    }

    /* Fondo Neutro */
    .stApp {
        background-color: #fcfcfd;
    }

    /* BARRA SUPERIOR ELEGANTE */
    .top-nav {
        background-color: #ffffff;
        padding: 1rem 2rem;
        border-bottom: 1px solid #e2e8f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
    }

    /* TARJETAS DE ÁREA (Compactas) */
    .area-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        text-align: left;
        transition: 0.3s;
    }
    
    /* BOTONES ESTILO APPLE */
    div.stButton > button {
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        transition: 0.3s !important;
    }

    /* DISEÑO DE LISTA DE REPORTES */
    .report-item {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        margin-bottom: 0.8rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# HEADER CORPORATIVO
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; padding-bottom: 20px; border-bottom: 2px solid #3b82f6;">
        <div>
            <h1 style='margin:0; font-weight:700; color:#0f172a; font-size:1.8rem;'>DON POLLO <span style='color:#3b82f6;'>COMMAND CENTER</span></h1>
            <p style='margin:0; color:#64748b; font-size:0.9rem;'>SISTEMA DE INTELIGENCIA ESTRATÉGICA</p>
        </div>
        <div style='text-align:right;'>
            <p style='margin:0; font-weight:600;'>BI SOLUTIONS 2026</p>
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)

# =========================================================
# VISTA 1: HOME (MENU SELECCIÓN)
# =========================================================
if st.session_state.view == 'home':
    st.subheader("Seleccione el Área de Control")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0;">
                <h3 style="margin-top:0;">💼 Nóminas</h3>
                <p style="color:#64748b; font-size:0.9rem;">Control de vacaciones, asistencia y pagos de personal.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Gestionar Nóminas", use_container_width=True, key="btn_nom"):
            st.session_state.view = 'nominas'; st.rerun()

    with col2:
        st.markdown("""
            <div style="background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0;">
                <h3 style="margin-top:0;">🦺 Seguridad</h3>
                <p style="color:#64748b; font-size:0.9rem;">Monitoreo de SST, incidentes y cumplimiento legal.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Gestionar Seguridad", use_container_width=True, key="btn_sst"):
            st.session_state.view = 'sst'; st.rerun()

    with col3:
        st.markdown("""
            <div style="background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0;">
                <h3 style="margin-top:0;">📈 Desarrollo</h3>
                <p style="color:#64748b; font-size:0.9rem;">KPIs de capacitación, clima laboral y desempeño.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Gestionar Desarrollo", use_container_width=True, key="btn_dev"):
            st.session_state.view = 'desarrollo'; st.rerun()

# =========================================================
# VISTA 2: ACCESO Y REPORTE
# =========================================================
else:
    area = st.session_state.view
    
    # Navegación Superior Interna
    nav1, nav2 = st.columns([1, 6])
    with nav1:
        if st.button("⬅ Volver"):
            st.session_state.view = 'home'; st.session_state.auth = False; st.rerun()
    with nav2:
        st.write(f"### Módulo de {area.upper()}")

    if not st.session_state.auth:
        st.warning(f"Se requiere validación para acceder a los reportes de {area.upper()}")
        _, col_login, _ = st.columns([1, 1, 1])
        with col_login:
            pw = st.text_input("Ingrese su Clave Gerencial", type="password")
            if st.button("Acceder al Dashboard", use_container_width=True):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True; st.rerun()
                else: st.error("Acceso Denegado")
    
    else:
        st.markdown("---")
        st.info("Visualización de Reportes Power BI autorizada")
        
        def report_link(name, description, link):
            with st.container():
                c_desc, c_btn = st.columns([4, 1])
                with c_desc:
                    st.markdown(f"""
                        <div class="report-item">
                            <p style='margin:0; font-weight:700;'>{name}</p>
                            <p style='margin:0; font-size:0.85rem; color:#64748b;'>{description}</p>
                        </div>
                    """, unsafe_allow_html=True)
                with c_btn:
                    st.write("") # Alineación
                    st.link_button("Abrir Reporte", link, use_container_width=True)

        if area == "nominas":
            report_link("🏖️ Control de Vacaciones", "Saldos pendientes y programación anual.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            report_link("🚑 Gestión de Descansos", "Trazabilidad de licencias médicas y ausentismo.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
        elif area == "sst":
            report_link("⚠️ Accidentabilidad", "Kpis de incidentes y actos inseguros.", "#")
            report_link("🩹 SST Core", "Cumplimiento normativo y auditorías.", "#")
        elif area == "desarrollo":
            report_link("🎓 Capacitaciones", "Avance de horas hombre y evaluaciones.", "#")
            report_link("🎯 Desempeño", "Resultados de KPIs por jefatura.", "#")

# PIE DE PÁGINA
st.markdown("<br><br><p style='text-align:center; color:#94a3b8; font-size:0.8rem;'>DON POLLO S.A. | Todos los derechos reservados 2026</p>", unsafe_allow_html=True)
