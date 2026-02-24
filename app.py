import streamlit as st

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Portal Corporativo | Control de Gestión",
    page_icon="📊",
    layout="wide"
)

# CREDENCIALES
PASSWORDS = {
    "👥 Administración de Personal": "pollo123",
    "📈 Desarrollo Organizacional": "talento2024",
    "🦺 Seguridad y Salud en el Trabajo": "seguridad2024"
}

# =========================================================
# ESTILO CORPORATIVO (IDENTIDAD GH / DON POLLO)
# =========================================================
st.markdown("""
<style>
/* APP GENERAL */
.stApp { background-color: #ffffff; }

/* TÍTULOS */
h1 { color: #1071b8; font-weight: 800; }
h2, h3 { color: #2e3788; font-weight: 700; }

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2e3788 0%, #1071b8 100%);
}
section[data-testid="stSidebar"] * {
    color: #ffffff;
    font-weight: 500;
}

/* CARDS */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #e5e7eb;
    border-left: 6px solid #c4579b;
    border-radius: 16px;
    padding: 1.2rem;
    background-color: #ffffff;
    box-shadow: 0 6px 16px rgba(0,0,0,0.04);
}

/* LINKS */
a { color: #1071b8; font-weight: 600; text-decoration: none; }
a:hover { color: #c4579b; text-decoration: underline; }

/* SEPARADORES */
hr {
    border: none;
    height: 4px;
    background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
    margin: 2.5rem 0;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #6b7280;
    font-size: 0.85rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# LÓGICA DE AUTENTICACIÓN
# =========================================================
if 'auth_area' not in st.session_state:
    st.session_state.auth_area = None

def check_password(area_seleccionada):
    if st.session_state.auth_area == area_seleccionada:
        return True
    
    st.warning(f"🔒 El área de **{area_seleccionada}** está restringida.")
    _, col_p, _ = st.columns([1,1,1])
    with col_p:
        pwd = st.text_input("Ingrese contraseña de acceso:", type="password")
        if st.button("Validar Acceso"):
            if pwd == PASSWORDS[area_seleccionada]:
                st.session_state.auth_area = area_seleccionada
                st.rerun()
            else:
                st.error("Contraseña incorrecta")
    return False

# =========================================================
# ENCABEZADO PRINCIPAL
# =========================================================
st.title("📊 Gestión Humana | Grupo Don Pollo")
st.markdown(
    """
    Plataforma centralizada de **analítica, automatización y visualización de información**,  
    desarrollada para apoyar la **toma de decisiones estratégicas** de la organización.
    """
)

st.markdown("---")

# =========================================================
# MENÚ LATERAL
# =========================================================
st.sidebar.markdown("## 📌 Líneas de Gestión")
linea = st.sidebar.radio(
    "",
    [
        "👥 Administración de Personal",
        "📈 Desarrollo Organizacional",
        "🦺 Seguridad y Salud en el Trabajo"
    ]
)

# =========================================================
# FUNCIÓN CARD PRO
# =========================================================
def card(titulo, descripcion, link, icon="🔗", detalles=None):
    with st.container(border=True):
        st.subheader(titulo)
        st.write(descripcion)
        st.markdown(f"{icon} **[Acceder al recurso]({link})**")
        if detalles:
            with st.expander("➕ Información técnica"):
                for d in detalles:
                    st.markdown(f"- {d}")

# =========================================================
# VALIDACIÓN Y CONTENIDO
# =========================================================
if check_password(linea):
    
    if linea == "👥 Administración de Personal":
        st.header("👥 Administración de Personal")
        st.caption("Indicadores clave para el control, seguimiento y planificación del recurso humano.")
        col1, col2, col3 = st.columns(3)
        with col1:
            card("🏖️ Vacaciones", "Visualización del uso, saldo y planificación.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", icon="📊", detalles=["🛠️ Power BI", "🔄 Automática", "📅 Mensual"])
        with col2:
            card("⏰ Asistencia", "Análisis de puntualidad y ausentismo.", "https://tu-link-powerbi.com", icon="📊", detalles=["🛠️ Power BI", "🔄 Automática", "📅 Diaria"])
        with col3:
            card("📄 Legajos Digitales", "Repositorio documental del personal.", "https://github.com", icon="📁", detalles=["🛠️ SharePoint", "🔐 Restringido", "🔄 Manual"])

    elif linea == "📈 Desarrollo Organizacional":
        st.header("📈 Desarrollo Organizacional")
        st.caption("Seguimiento del crecimiento y fortalecimiento del talento humano.")
        col1, col2 = st.columns(2)
        with col1:
            card("🎓 Capacitaciones", "Control del cumplimiento del plan anual.", "https://github.com", icon="📊", detalles=["🛠️ Power BI", "📊 Registros", "📅 Mensual"])
        with col2:
            card("😊 Clima Laboral", "Resultados consolidados de encuestas.", "https://tu-link-powerbi.com", icon="📊", detalles=["🛠️ Power BI", "📝 Encuestas", "📅 Trimestral"])

    elif linea == "🦺 Seguridad y Salud en el Trabajo":
        st.header("🦺 Seguridad y Salud en el Trabajo")
        st.caption("Monitoreo preventivo de riesgos e incidentes.")
        col1, col2 = st.columns(2)
        with col1:
            card("⚠️ Incidentes y Accidentes", "Análisis de eventos de seguridad laboral.", "https://tu-link-powerbi.com", icon="📊", detalles=["🛠️ Power BI", "📊 Registros SST", "📅 Mensual"])
        with col2:
            card("❤️ Bienestar y Ausentismo", "Indicadores de salud ocupacional.", "https://tu-link-powerbi.com", icon="📊", detalles=["🛠️ Power BI", "📊 RRHH / SST", "📅 Mensual"])

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.markdown(
    "<div class='footer'>Gerencia de Control de Gestión | Transformación Digital</div>",
    unsafe_allow_html=True
)
