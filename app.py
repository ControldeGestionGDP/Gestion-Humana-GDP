import streamlit as st

# =============================
# CONFIGURACIÓN GENERAL
# =============================
st.set_page_config(
    page_title="Portal Gestión Humana",
    page_icon="👥",
    layout="wide"
)

# =============================
# ESTILO CORPORATIVO GH
# =============================
st.markdown("""
<style>

/* Fondo general */
.stApp {
    background-color: #ffffff;
}

/* Títulos */
h1, h2, h3 {
    color: #1071b8;
    font-weight: 700;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #2e3788;
}

section[data-testid="stSidebar"] * {
    color: white;
}

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #e6e6e6;
    border-left: 6px solid #c4579b;
    border-radius: 14px;
    padding: 1rem;
    background-color: #ffffff;
}

/* Links */
a {
    color: #1071b8;
    font-weight: 600;
    text-decoration: none;
}

a:hover {
    color: #c4579b;
    text-decoration: underline;
}

/* Separadores */
hr {
    border: none;
    height: 4px;
    background: linear-gradient(
        90deg,
        #1071b8,
        #2e3788,
        #c4579b
    );
    margin: 2rem 0;
}

</style>
""", unsafe_allow_html=True)

# =============================
# ENCABEZADO
# =============================
st.title("📊 Portal de Transformación Digital – Gestión Humana")
st.markdown(
    """
    Este portal centraliza los **desarrollos digitales, reportes y aplicaciones**
    de la **Gerencia de Gestión Humana**, organizados por líneas estratégicas.
    """
)

st.markdown("---")

# =============================
# MENÚ LATERAL
# =============================
linea = st.sidebar.radio(
    "📌 Líneas de Gestión Humana",
    [
        "👥 Administración de Personal",
        "📈 Desarrollo Organizacional",
        "🦺 Seguridad y Salud en el Trabajo"
    ]
)

# =============================
# FUNCIÓN CARD
# =============================
def card(titulo, descripcion, link, icon="🔗"):
    with st.container(border=True):
        st.subheader(titulo)
        st.write(descripcion)
        st.markdown(f"{icon} [Acceder al recurso]({link})")

# =============================
# ADMINISTRACIÓN DE PERSONAL
# =============================
if linea == "👥 Administración de Personal":
    st.header("👥 Administración de Personal")
    st.caption("Gestión operativa y analítica del personal")

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "🏖️ Vacaciones",
            "Seguimiento de saldos, uso y planificación de descansos.",
            "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare",
            icon="📊"
        )

    with col2:
        card(
            "⏰ Asistencia",
            "Control de asistencia, tardanzas y ausencias.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

    with col3:
        card(
            "📄 Legajos Digitales",
            "Repositorio centralizado de información del personal.",
            "https://github.com/tuusuario/tu-repo",
            icon="📁"
        )

# =============================
# DESARROLLO ORGANIZACIONAL
# =============================
elif linea == "📈 Desarrollo Organizacional":
    st.header("📈 Desarrollo Organizacional")
    st.caption("Crecimiento, desempeño y desarrollo del talento")

    col1, col2 = st.columns(2)

    with col1:
        card(
            "🎓 Capacitaciones",
            "Monitoreo de participación, horas y cumplimiento del plan de capacitación.",
            "https://github.com/tuusuario/tu-repo",
            icon="📊"
        )

    with col2:
        card(
            "😊 Clima Laboral",
            "Resultados de encuestas y análisis del clima organizacional.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

# =============================
# SEGURIDAD Y SALUD EN EL TRABAJO
# =============================
elif linea == "🦺 Seguridad y Salud en el Trabajo":
    st.header("🦺 Seguridad y Salud en el Trabajo")
    st.caption("Prevención, bienestar y control de riesgos")

    col1, col2 = st.columns(2)

    with col1:
        card(
            "⚠️ Incidentes y Accidentes",
            "Registro y análisis de incidentes laborales.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

    with col2:
        card(
            "❤️ Bienestar y Ausentismo",
            "Seguimiento de ausentismo y salud ocupacional.",
            "https://tu-link-powerbi.com",
            icon="📊"
        )

# =============================
# FOOTER
# =============================
st.markdown("---")
st.caption("Gerencia de Gestión Humana | Transformación Digital")
