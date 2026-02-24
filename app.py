import streamlit as st

# ===============================
# CONFIGURACIÓN
# ===============================
st.set_page_config(
    page_title="Portal GH 2026",
    page_icon="🧠",
    layout="wide"
)

# ===============================
# ESTILOS PREMIUM CLAROS
# ===============================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg,#f8fafc,#eef2ff);
    font-family: 'Segoe UI', sans-serif;
}

/* Título principal */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #1e3a8a;
}

/* Tarjetas módulos */
.module-card {
    background: white;
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    transition: 0.25s;
}

.module-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 45px rgba(37,99,235,0.18);
}

.area-title {
    font-size: 22px;
    font-weight: 700;
    color: #1e3a8a;
}

.panel-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ===============================
# ÁREAS Y CLAVES
# ===============================
AREAS = {
    "Reclutamiento": "recluta2026",
    "Bienestar": "bienestar2026",
    "Capacitación": "capacitacion2026",
    "Administración": "admin2026",
    "Indicadores": "kpi2026",
    "Seguridad y Salud": "sst2026"
}

# ===============================
# ESTADO
# ===============================
if "area_activa" not in st.session_state:
    st.session_state.area_activa = None

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False


def volver():
    st.session_state.area_activa = None
    st.session_state.autenticado = False


# ===============================
# PORTAL PRINCIPAL
# ===============================
if st.session_state.area_activa is None:

    st.markdown('<p class="main-title">Portal Gestión Humana 2026</p>', unsafe_allow_html=True)
    st.markdown("### Plataforma modular interna")

    col1, col2, col3 = st.columns(3)
    modulos = list(AREAS.keys())

    for i, area in enumerate(modulos):

        with [col1, col2, col3][i % 3]:

            st.markdown(f"""
            <div class="module-card">
                <div class="area-title">{area}</div>
                <p>Acceso al módulo estratégico</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Ingresar a {area}", use_container_width=True):
                st.session_state.area_activa = area
                st.rerun()


# ===============================
# PANTALLA CONTRASEÑA
# ===============================
elif not st.session_state.autenticado:

    area = st.session_state.area_activa

    st.markdown(f"## 🔐 Acceso al módulo: {area}")

    clave = st.text_input("Ingrese la contraseña", type="password")

    col1, col2 = st.columns([1,1])

    with col1:
        if st.button("Acceder"):
            if clave == AREAS[area]:
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

    with col2:
        if st.button("⬅ Volver"):
            volver()
            st.rerun()


# ===============================
# PANEL DEL MÓDULO
# ===============================
else:

    area = st.session_state.area_activa

    st.markdown(f"## 🧠 Módulo: {area}")

    if st.button("⬅ Volver al portal"):
        volver()
        st.rerun()

    st.markdown('<div class="panel-box">', unsafe_allow_html=True)

    if area == "Reclutamiento":
        st.metric("Convocatorias abiertas", 12, "+2")
        st.metric("Postulantes este mes", 348, "+15%")

    elif area == "Bienestar":
        st.metric("Satisfacción general", "88%", "+3%")
        st.metric("Participación en actividades", "72%", "+5%")

    elif area == "Capacitación":
        st.metric("Cursos activos", 9)
        st.metric("Horas promedio por colaborador", 18)

    elif area == "Administración":
        st.metric("Documentos emitidos", 124)
        st.metric("Trámites pendientes", 7)

    elif area == "Indicadores":
        st.metric("Rotación anual", "6.2%", "-0.8%")
        st.metric("Ausentismo", "2.1%", "-0.3%")

    elif area == "Seguridad y Salud":
        st.metric("Accidentes reportados", 1)
        st.metric("Días sin accidentes", 84)

    st.markdown('</div>', unsafe_allow_html=True)
