import streamlit as st
from datetime import datetime

# =========================================================
# CONFIGURACIÓN
# =========================================================
st.set_page_config(
    page_title="GH Command Center",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# ESTADO
# =========================================================
if "area_autorizada" not in st.session_state:
    st.session_state.area_autorizada = None

PASSWORDS = {
    "👥 Administración de Personal": "pollo123",
    "📈 Desarrollo Organizacional": "talento2024",
    "🦺 Seguridad y Salud en el Trabajo": "seguridad2024"
}

# =========================================================
# ESTILO FUTURISTA
# =========================================================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0b1220, #020617 70%);
    color: #e5e7eb;
}

/* TÍTULOS */
h1 {
    font-weight: 900;
    letter-spacing: 1px;
    color: #e2e8f0;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#020617,#0f172a);
}
section[data-testid="stSidebar"] * {
    color: #cbd5f5;
}

/* TARJETAS GLASS */
.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 25px rgba(99,102,241,0.15);
    transition: all 0.2s ease;
}
.card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 0 35px rgba(139,92,246,0.35);
}

/* PANEL KPI */
.kpi {
    background: linear-gradient(145deg,#020617,#0f172a);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(99,102,241,0.25);
    box-shadow: 0 0 20px rgba(99,102,241,0.2);
}

/* FOOTER */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 50px;
    font-size: 0.85rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIONES
# =========================================================
def validar(area):

    if st.session_state.area_autorizada == area:
        return True

    st.warning(f"🔒 Acceso restringido: {area}")

    c1, c2, c3 = st.columns([1,1,1])

    with c2:
        pwd = st.text_input("Contraseña", type="password")

        if st.button("Validar acceso"):
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
            <h3>{titulo}</h3>
            <p>{desc}</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.title("🧠 GH COMMAND CENTER")

st.caption("Sistema estratégico de inteligencia organizacional")

# =========================================================
# PANEL DE KPIs
# =========================================================
st.markdown("### ⚡ Estado Organizacional en Tiempo Real")

k1, k2, k3, k4 = st.columns(4)

k1.markdown('<div class="kpi"><b>👥 Colaboradores</b><br><h2>2,845</h2></div>', unsafe_allow_html=True)
k2.markdown('<div class="kpi"><b>📉 Ausentismo</b><br><h2>3.1%</h2></div>', unsafe_allow_html=True)
k3.markdown('<div class="kpi"><b>📚 Capacitaciones</b><br><h2>87%</h2></div>', unsafe_allow_html=True)
k4.markdown('<div class="kpi"><b>😊 Clima</b><br><h2>8.6 / 10</h2></div>', unsafe_allow_html=True)

st.info(f"Última sincronización: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

st.markdown("---")

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("## 🧭 Módulos GH")
st.sidebar.info("Usuario: Humberto Atoche\nNivel: Control de Gestión")

area = st.sidebar.radio("Seleccionar área", list(PASSWORDS.keys()))

# =========================================================
# BUSCADOR
# =========================================================
busqueda = st.text_input("🔎 Buscar módulo")

# =========================================================
# CONTENIDO
# =========================================================
if validar(area):

    if area == "👥 Administración de Personal":

        st.header("👥 Administración de Personal")

        c1, c2, c3 = st.columns(3)

        with c1:
            tarjeta("🏖️ Vacaciones", "Control integral de descansos.", "https://app.powerbi.com")

        with c2:
            tarjeta("⏰ Asistencia", "Monitoreo de puntualidad.", "https://app.powerbi.com")

        with c3:
            tarjeta("📁 Legajos", "Gestión documental.", "https://sharepoint.com")

    elif area == "📈 Desarrollo Organizacional":

        st.header("📈 Desarrollo Organizacional")

        c1, c2 = st.columns(2)

        with c1:
            tarjeta("🎓 Capacitaciones", "Seguimiento del plan anual.", "https://app.powerbi.com")

        with c2:
            tarjeta("😊 Clima", "Análisis de percepción organizacional.", "https://app.powerbi.com")

    elif area == "🦺 Seguridad y Salud en el Trabajo":

        st.header("🦺 Seguridad y Salud")

        c1, c2 = st.columns(2)

        with c1:
            tarjeta("⚠️ Incidentes", "Registro y análisis.", "https://app.powerbi.com")

        with c2:
            tarjeta("❤️ Bienestar", "Indicadores de salud.", "https://app.powerbi.com")

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
GH Command Center · Plataforma Estratégica 2026
</div>
""", unsafe_allow_html=True)
