import streamlit as st
from datetime import datetime

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="GH Strategic Command",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# SESIÓN
# =========================================================
if "area_autorizada" not in st.session_state:
    st.session_state.area_autorizada = None

PASSWORDS = {
    "👥 Administración de Personal": "pollo123",
    "📈 Desarrollo Organizacional": "talento2024",
    "🦺 Seguridad y Salud en el Trabajo": "seguridad2024"
}

# =========================================================
# ESTILO PREMIUM CORPORATIVO
# =========================================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg,#f1f5f9,#e0e7ff);
}

/* HEADER PRINCIPAL */
.main-header {
    background: linear-gradient(90deg,#1e3a8a,#2563eb);
    padding: 24px 28px;
    border-radius: 18px;
    color: white;
    box-shadow: 0 12px 30px rgba(37,99,235,0.35);
}

/* TITULOS */
h1 { font-weight: 900; }
h2 { color: #0f172a; }

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#1e3a8a,#1d4ed8);
}
section[data-testid="stSidebar"] * { color: white; }

/* KPI CAPSULAS */
.kpi {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    text-align: center;
    transition: all 0.2s ease;
}
.kpi:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(37,99,235,0.18);
}

/* TARJETAS */
.card {
    background: white;
    border-radius: 20px;
    padding: 26px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 14px 32px rgba(0,0,0,0.08);
    transition: all 0.2s ease;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 26px 60px rgba(37,99,235,0.22);
}

/* FOOTER */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 45px;
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

    st.warning(f"🔒 Área restringida: {area}")

    c1, c2, c3 = st.columns([1,1,1])

    with c2:
        pwd = st.text_input("Contraseña", type="password")

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
            <h3>{titulo}</h3>
            <p>{desc}</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# =========================================================
# HEADER PREMIUM
# =========================================================
st.markdown(f"""
<div class="main-header">
<h1>📊 GH Strategic Command</h1>
<p>Centro de inteligencia y control de Gestión Humana</p>
<p>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("")

# =========================================================
# KPIs EJECUTIVOS
# =========================================================
st.markdown("### 📈 Estado Organizacional")

k1, k2, k3, k4 = st.columns(4)

k1.markdown('<div class="kpi"><b>👥 Colaboradores</b><br><h2>2,845</h2></div>', unsafe_allow_html=True)
k2.markdown('<div class="kpi"><b>📉 Ausentismo</b><br><h2>3.1%</h2></div>', unsafe_allow_html=True)
k3.markdown('<div class="kpi"><b>📚 Capacitaciones</b><br><h2>87%</h2></div>', unsafe_allow_html=True)
k4.markdown('<div class="kpi"><b>😊 Clima</b><br><h2>8.6 / 10</h2></div>', unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("## 🧭 Navegación")
st.sidebar.info("Usuario: Humberto Atoche\nRol: Control de Gestión")

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
            tarjeta("😊 Clima", "Análisis organizacional.", "https://app.powerbi.com")

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
GH Strategic Command · Plataforma Ejecutiva 2026
</div>
""", unsafe_allow_html=True)
