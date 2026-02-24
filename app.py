import streamlit as st
from datetime import datetime

# =========================================================
# CONFIGURACIÓN
# =========================================================
st.set_page_config(
    page_title="Portal GH | Grupo Don Pollo",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# ESTADO DE SESIÓN
# =========================================================
if "area_autorizada" not in st.session_state:
    st.session_state.area_autorizada = None

# =========================================================
# CONTRASEÑAS
# =========================================================
PASSWORDS = {
    "👥 Administración de Personal": "pollo123",
    "📈 Desarrollo Organizacional": "talento2024",
    "🦺 Seguridad y Salud en el Trabajo": "seguridad2024"
}

# =========================================================
# ESTILO MODERNO 2026
# =========================================================
st.markdown("""
<style>

.stApp { background-color: #f6f8fb; }

h1 { font-weight: 800; color: #0f172a; }
h2, h3 { color: #1e293b; }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0f172a 0%,#1e3a8a 100%);
}
section[data-testid="stSidebar"] * {
    color: white;
}

.metric-card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}

.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    transition: all 0.18s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 0.85rem;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIONES
# =========================================================
def validar_acceso(area):

    if st.session_state.area_autorizada == area:
        return True

    st.warning(f"🔒 Área restringida: {area}")

    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        pwd = st.text_input("Ingrese contraseña", type="password")

        if st.button("Acceder"):
            if pwd == PASSWORDS[area]:
                st.session_state.area_autorizada = area
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

    return False


def tarjeta(titulo, desc, link):

    if busqueda and busqueda.lower() not in titulo.lower():
        return

    st.markdown(f"""
    <a href="{link}" target="_blank" style="text-decoration:none;">
        <div class="card">
            <h4>{titulo}</h4>
            <p>{desc}</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.title("🧠 Portal de Gestión Humana")
st.caption("Plataforma interna de analítica, control y soporte a decisiones")

# =========================================================
# PANEL EJECUTIVO
# =========================================================
st.markdown("### 📊 Estado General")

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Colaboradores", "2,845", "+12")
c2.metric("📉 Ausentismo", "3.1%", "-0.4%")
c3.metric("📚 Capacitaciones", "87%", "+5%")
c4.metric("🟢 Clima Laboral", "8.6/10", "+0.3")

st.info(f"Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

st.markdown("---")

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("## 🧭 Navegación GH")
st.sidebar.info("Usuario: Humberto Atoche\nÁrea: Control de Gestión")

area = st.sidebar.radio(
    "Seleccionar línea",
    list(PASSWORDS.keys())
)

# =========================================================
# BUSCADOR
# =========================================================
busqueda = st.text_input("🔎 Buscar herramienta o dashboard")

# =========================================================
# CONTENIDO POR ÁREA
# =========================================================
if validar_acceso(area):

    # -----------------------------------------------------
    # ADMINISTRACIÓN
    # -----------------------------------------------------
    if area == "👥 Administración de Personal":

        st.header("👥 Administración de Personal")

        col1, col2, col3 = st.columns(3)

        with col1:
            tarjeta(
                "🏖️ Gestión de Vacaciones",
                "Control de saldos, programación y alertas.",
                "https://app.powerbi.com"
            )

        with col2:
            tarjeta(
                "⏰ Control de Asistencia",
                "Puntualidad, tardanzas y ausencias.",
                "https://app.powerbi.com"
            )

        with col3:
            tarjeta(
                "📁 Legajos Digitales",
                "Repositorio documental del personal.",
                "https://sharepoint.com"
            )

    # -----------------------------------------------------
    # DESARROLLO
    # -----------------------------------------------------
    elif area == "📈 Desarrollo Organizacional":

        st.header("📈 Desarrollo Organizacional")

        col1, col2 = st.columns(2)

        with col1:
            tarjeta(
                "🎓 Plan de Capacitaciones",
                "Seguimiento del plan anual.",
                "https://app.powerbi.com"
            )

        with col2:
            tarjeta(
                "😊 Clima Organizacional",
                "Resultados de encuestas internas.",
                "https://app.powerbi.com"
            )

    # -----------------------------------------------------
    # SST
    # -----------------------------------------------------
    elif area == "🦺 Seguridad y Salud en el Trabajo":

        st.header("🦺 Seguridad y Salud en el Trabajo")

        col1, col2 = st.columns(2)

        with col1:
            tarjeta(
                "⚠️ Incidentes y Accidentes",
                "Registro y análisis de eventos.",
                "https://app.powerbi.com"
            )

        with col2:
            tarjeta(
                "❤️ Bienestar y Ausentismo",
                "Indicadores de salud ocupacional.",
                "https://app.powerbi.com"
            )

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
Grupo Don Pollo · Gestión Humana · Plataforma Interna 2026
</div>
""", unsafe_allow_html=True)
