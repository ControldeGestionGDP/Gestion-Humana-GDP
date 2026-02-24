import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="📊")

# 2. CREDENCIALES
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. CSS DE ÚLTIMA GENERACIÓN (Estilo Dark/Light Moderno)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
        color: #1e293b;
    }

    .stApp {
        background-color: #f8fafc;
    }

    /* Encabezado Principal */
    .header-container {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }

    /* Tarjetas de Selección (Home) */
    .area-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        text-align: center;
    }

    /* Botones de Streamlit convertidos en Tarjetas Elegantes */
    div.stButton > button {
        width: 100% !important;
        background-color: white !important;
        color: #1e293b !important;
        border: 1px solid #e2e8f0 !important;
        padding: 3rem 1rem !important;
        border-radius: 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
    }

    div.stButton > button:hover {
        border-color: #3b82f6 !important;
        color: #3b82f6 !important;
        transform: translateY(-5px) !important;
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1) !important;
    }

    /* Tarjetas de Reporte (Internas) */
    .report-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

def logout():
    st.session_state.view = 'home'
    st.session_state.auth = False
    st.rerun()

# =========================================================
# VISTA 1: MENÚ PRINCIPAL
# =========================================================
if st.session_state.view == 'home':
    st.markdown("""
        <div class="header-container">
            <div class="main-title">COMMAND CENTER</div>
            <div style="opacity: 0.8; font-weight: 300; font-size: 1.1rem;">
                UNIDAD DE INTELIGENCIA DE DATOS | GRUPO DON POLLO
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Seleccione un área de gestión")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 💼 Nóminas")
        if st.button("ACCEDER A RR.HH.\n(Vacaciones, Asistencia, Pagos)", key="go_nom"):
            st.session_state.view = 'nominas'
            st.rerun()

    with col2:
        st.markdown("### 🦺 Seguridad")
        if st.button("ACCEDER A SST\n(Incidentes, Auditorías, EPPs)", key="go_sst"):
            st.session_state.view = 'sst'
            st.rerun()

    with col3:
        st.markdown("### 📈 Desarrollo")
        if st.button("ACCEDER A TALENTO\n(Capacitación, Clima, KPIs)", key="go_dev"):
            st.session_state.view = 'desarrollo'
            st.rerun()

# =========================================================
# VISTA 2: ACCESO Y REPORTES
# =========================================================
else:
    area = st.session_state.view
    
    # Header de la sección
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("⬅ Volver"):
            logout()
    with col_title:
        st.title(f"Módulo de {area.upper()}")

    if not st.session_state.auth:
        st.info(f"Por seguridad, ingrese la clave de acceso para el área de {area.upper()}")
        _, col_login, _ = st.columns([1, 1, 1])
        with col_login:
            pw = st.text_input("Password", type="password")
            if st.button("Desbloquear Dashboard"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Clave incorrecta")
    
    else:
        # CONTENIDO DE LOS REPORTES
        st.markdown("---")
        st.write("### Reportes Disponibles en Power BI")
        
        def display_report(title, desc, url):
            with st.container():
                col_info, col_link = st.columns([3, 1])
                with col_info:
                    st.markdown(f"""
                        <div class="report-card">
                            <h4 style="margin:0; color:#1e293b;">{title}</h4>
                            <p style="margin:5px 0 0 0; color:#64748b; font-size:0.9rem;">{desc}</p>
                        </div>
                    """, unsafe_allow_html=True)
                with col_link:
                    st.write("") # Espaciador
                    st.link_button("Abrir Reporte", url, use_container_width=True)

        if area == "nominas":
            display_report("🏖️ Control de Vacaciones", "Análisis de días pendientes, gozados y programación por sedes.", "https://app.powerbi.com/...")
            display_report("🚑 Gestión de Descansos Médicos", "Reporte de ausentismo, licencias y subsidios.", "https://app.powerbi.com/...")
            display_report("⏰ Monitor de Asistencia", "Control de ingresos, salidas y horas extraordinarias.", "#")
        
        elif area == "sst":
            display_report("⚠️ Tasa de Accidentabilidad", "Registro de incidentes y seguimiento de actos inseguros.", "#")
            display_report("🏢 Cumplimiento de Auditorías", "Resultados de inspecciones internas y externas.", "#")
        
        elif area == "desarrollo":
            display_report("🎓 Plan de Capacitación", "Avance de horas hombre de formación y evaluaciones.", "#")
            display_report("😊 Clima Organizacional", "Resultados de la última encuesta de satisfacción.", "#")

# FOOTER
st.markdown(f"""
    <div style="margin-top: 5rem; text-align: center; color: #94a3b8; font-size: 0.8rem; border-top: 1px solid #e2e8f0; padding-top: 1rem;">
        GRUPO DON POLLO - SISTEMA DE INTELIGENCIA CORPORATIVA 2026
    </div>
""", unsafe_allow_html=True)
