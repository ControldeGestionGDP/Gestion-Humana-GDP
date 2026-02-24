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
# CREDENCIALES
# =========================================================
PASSWORDS = {
    "👥 Administración de Personal": "pollo123",
    "📈 Desarrollo Organizacional": "talento2024",
    "🦺 Seguridad y Salud en el Trabajo": "seguridad2024"
}

# =========================================================
# ESTILO CORPORATIVO
# =========================================================
st.markdown("""
<style>
.stApp { background-color: #ffffff; }

h1 { color: #1071b8; font-weight: 800; }
h2, h3 { color: #2e3788; font-weight: 700; }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2e3788 0%, #1071b8 100%);
}
section[data-testid="stSidebar"] * {
    color: #ffffff;
    font-weight: 500;
}

.card {
    border: 1px solid #e5e7eb;
    border-left: 6px solid #c4579b;
    border-radius: 16px;
    padding: 1.2rem;
    background-color: #ffffff;
    box-shadow: 0 6px 16px rgba(0,0,0,0.05);
    transition: transform 0.15s ease;
}
.card:hover { transform: translateY(-4px); }

.footer {
    text-align: center;
    color: #6b7280;
    font-size: 0.85rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# AUTENTICACIÓN
# =========================================================
if 'auth_area' not in st.session_state:
    st.session_state.auth_area = None

def check_password(area):
    if st.session_state.auth_area == area:
        return True

    st.warning(f"🔒 El área de **{area}** está restringida.")

    _, col, _ = st.columns([1,1,1])
    with col:
        pwd = st.text_input("Ingrese contraseña:", type="password")

        if st.button("Validar acceso"):
            if pwd == PASSWORDS[area]:
                st.session_state.auth_area = area
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

    return False

# =========================================================
# ENCABEZADO
# =========================================================
st.title("📊 Gestión Humana | Grupo Don Pollo")

st.caption(
    "Plataforma centralizada de analítica y automatización "
    "para la toma de decisiones estratégicas."
)

# =========================================================
# MÉTRICAS GENERALES
# =========================================================
st.markdown("### 📊 Indicadores Generales")

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Colaboradores", "2,845")
c2.metric("📈 Indicadores activos", "18")
c3.metric("📊 Dashboards", "9")
c4.metric("🟢 Sistemas online", "100%")

st.success("✔️ Datos actualizados automáticamente — Hoy")

st.markdown("---")

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("## 👤 Usuario")
st.sidebar.info("Humberto Atoche\nControl de Gestión")

st.sidebar.markdown("## 📌 Líneas de Gestión")

linea = st.sidebar.selectbox(
    "",
    [
        "👥 Administración de Personal",
        "📈 Desarrollo Organizacional",
        "🦺 Seguridad y Salud en el Trabajo"
    ]
)

# =========================================================
# BUSCADOR
# =========================================================
search = st.text_input("🔎 Buscar recurso")

# =========================================================
# FUNCIÓN CARD
# =========================================================
def card(titulo, descripcion, link, detalles=None):

    if search and search.lower() not in titulo.lower():
        return

    st.markdown(f"""
    <a href="{link}" target="_blank" style="text-decoration:none;">
        <div class="card">
            <h4>{titulo}</h4>
            <p>{descripcion}</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

    if detalles:
        with st.expander("➕ Información técnica"):
            for d in detalles:
                st.markdown(f"- {d}")

# =========================================================
# CONTENIDO POR ÁREA
# =========================================================
if check_password(linea):

    # -----------------------------------------------------
    # ADMINISTRACIÓN DE PERSONAL
    # -----------------------------------------------------
    if linea == "👥 Administración de Personal":

        st.header("👥 Administración de Personal")
        st.caption("Control, seguimiento y planificación del personal.")

        col1, col2, col3 = st.columns(3)

        with col1:
            card(
                "🏖️ Vacaciones",
                "Uso, saldo y planificación anual.",
                "https://app.powerbi.com",
                ["Power BI", "Actualización mensual"]
            )

        with col2:
            card(
                "⏰ Asistencia",
                "Análisis de puntualidad y ausentismo.",
                "https://app.powerbi.com",
                ["Power BI", "Actualización diaria"]
            )

        with col3:
            card(
                "📄 Legajos Digitales",
                "Repositorio documental del personal.",
                "https://sharepoint.com",
                ["SharePoint", "Acceso restringido"]
            )

    # -----------------------------------------------------
    # DESARROLLO ORGANIZACIONAL
    # -----------------------------------------------------
    elif linea == "📈 Desarrollo Organizacional":

        st.header("📈 Desarrollo Organizacional")
        st.caption("Seguimiento del talento y cultura organizacional.")

        col1, col2 = st.columns(2)

        with col1:
            card(
                "🎓 Capacitaciones",
                "Cumplimiento del plan anual.",
                "https://app.powerbi.com",
                ["Power BI", "Mensual"]
            )

        with col2:
            card(
                "😊 Clima Laboral",
                "Resultados de encuestas internas.",
                "https://app.powerbi.com",
                ["Power BI", "Trimestral"]
            )

    # -----------------------------------------------------
    # SST
    # -----------------------------------------------------
    elif linea == "🦺 Seguridad y Salud en el Trabajo":

        st.header("🦺 Seguridad y Salud en el Trabajo")
        st.caption("Monitoreo preventivo de riesgos laborales.")

        col1, col2 = st.columns(2)

        with col1:
            card(
                "⚠️ Incidentes y Accidentes",
                "Eventos de seguridad laboral.",
                "https://app.powerbi.com",
                ["Power BI", "Mensual"]
            )

        with col2:
            card(
                "❤️ Bienestar y Ausentismo",
                "Indicadores de salud ocupacional.",
                "https://app.powerbi.com",
                ["Power BI", "Mensual"]
            )

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.markdown("""
<div class='footer'>
<b>Grupo Don Pollo</b><br>
Gerencia de Control de Gestión · Transformación Digital<br>
© 2026 — Plataforma Corporativa Interna
</div>
""", unsafe_allow_html=True)
