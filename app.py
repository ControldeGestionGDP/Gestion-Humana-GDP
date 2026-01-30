import streamlit as st

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Portal Corporativo | Control de Gestión",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# ESTILO CORPORATIVO (IDENTIDAD GH / DON POLLO)
# =========================================================
st.markdown("""
<style>

/* -------------------------
   APP GENERAL
------------------------- */
.stApp {
    background-color: #ffffff;
}

/* -------------------------
   TÍTULOS
------------------------- */
h1 {
    color: #1071b8;
    font-weight: 800;
}

h2, h3 {
    color: #2e3788;
    font-weight: 700;
}

/* -------------------------
   SIDEBAR
------------------------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #2e3788 0%,
        #1071b8 100%
    );
}

section[data-testid="stSidebar"] * {
    color: #ffffff;
    font-weight: 500;
}

/* -------------------------
   CARDS
------------------------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #e5e7eb;
    border-left: 6px solid #c4579b;
    border-radius: 16px;
    padding: 1.2rem;
    background-color: #ffffff;
    box-shadow: 0 6px 16px rgba(0,0,0,0.04);
}

/* -------------------------
   LINKS
------------------------- */
a {
    color: #1071b8;
    font-weight: 600;
    text-decoration: none;
}

a:hover {
    color: #c4579b;
    text-decoration: underline;
}

/* -------------------------
   SEPARADORES
------------------------- */
hr {
    border: none;
    height: 4px;
    background: linear-gradient(
        90deg,
        #1071b8,
        #2e3788,
        #c4579b
    );
    margin: 2.5rem 0;
}

/* -------------------------
   FOOTER
------------------------- */
.footer {
    text-align: center;
    color: #6b7280;
    font-size: 0.85rem;
    margin-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

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
# FUNCIÓN CARD (REUTILIZABLE)
# =========================================================
def card(titulo, descripcion, link, icon="🔗"):
    with st.container(border=True):
        st.subheader(titulo)
        st.write(descripcion)
        st.markdown(f"{icon} **[Acceder al recurso]({link})**")

# =========================================================
# ADMINISTRACIÓN DE PERSONAL
# =========================================================
if linea == "👥 Administración de Personal":
    st.header("👥 Administración de Personal")
    st.caption(
        "Indicadores clave para el control, seguimiento y planificación del recurso humano."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "🏖️ Vacaciones",
            "Visualización del uso, saldo y planificación de vacaciones para asegurar continuidad operativa.",
            "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare",
            icon="📊"
        )

    with col2:
        card(
            "⏰ Asistencia",
            "Análisis de asistencia, puntualidad y ausentismo por área y periodo.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

    with col3:
        card(
            "📄 Legajos Digitales",
            "Repositorio estructurado de información laboral y documental del personal.",
            "https://github.com/tuusuario/tu-repo",
            icon="📁"
        )

# =========================================================
# DESARROLLO ORGANIZACIONAL
# =========================================================
elif linea == "📈 Desarrollo Organizacional":
    st.header("📈 Desarrollo Organizacional")
    st.caption(
        "Seguimiento del crecimiento, desempeño y fortalecimiento del talento humano."
    )

    col1, col2 = st.columns(2)

    with col1:
        card(
            "🎓 Capacitaciones",
            "Control del avance, cobertura y cumplimiento del plan anual de capacitación.",
            "https://github.com/tuusuario/tu-repo",
            icon="📊"
        )

    with col2:
        card(
            "😊 Clima Laboral",
            "Resultados consolidados de encuestas y análisis de clima organizacional.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

# =========================================================
# SEGURIDAD Y SALUD EN EL TRABAJO
# =========================================================
elif linea == "🦺 Seguridad y Salud en el Trabajo":
    st.header("🦺 Seguridad y Salud en el Trabajo")
    st.caption(
        "Monitoreo preventivo de riesgos, incidentes y bienestar del personal."
    )

    col1, col2 = st.columns(2)

    with col1:
        card(
            "⚠️ Incidentes y Accidentes",
            "Registro, análisis y seguimiento de eventos de seguridad laboral.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

    with col2:
        card(
            "❤️ Bienestar y Ausentismo",
            "Indicadores de salud ocupacional y ausentismo para acciones preventivas.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.markdown(
    "<div class='footer'>Gerencia de Control de Gestión | Transformación Digital</div>",
    unsafe_allow_html=True
)
