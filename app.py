import streamlit as st

# ===============================
# CONFIGURACIÓN GENERAL
# ===============================
st.set_page_config(
    page_title="Portal GH 2026",
    page_icon="🧬",
    layout="wide"
)

# ===============================
# ESTILO FUTURISTA
# ===============================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #050505, #0d1117);
    color: #E6EDF3;
    font-family: 'Segoe UI', sans-serif;
}

/* Título principal */
.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #58A6FF;
    text-shadow: 0 0 25px #58A6FF;
}

/* Tarjetas módulos */
.module-card {
    background: linear-gradient(145deg, #0d1117, #161b22);
    padding: 35px;
    border-radius: 18px;
    border: 1px solid #30363d;
    text-align: center;
    box-shadow: 0 0 20px rgba(88,166,255,0.25);
    transition: 0.3s;
}

.module-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 35px rgba(88,166,255,0.55);
}

.area-title {
    font-size: 26px;
    font-weight: bold;
    color: #58A6FF;
}

.area-desc {
    font-size: 15px;
    color: #c9d1d9;
}

.panel-box {
    background: #0d1117;
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #30363d;
    box-shadow: 0 0 30px rgba(88,166,255,0.25);
}

</style>
""", unsafe_allow_html=True)

# ===============================
# CLAVES POR ÁREA
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


# ===============================
# FUNCIÓN VOLVER
# ===============================
def volver():
    st.session_state.area_activa = None
    st.session_state.autenticado = False


# ===============================
# PANTALLA PRINCIPAL — MÓDULOS
# ===============================
if st.session_state.area_activa is None:

    st.markdown('<p class="main-title">Portal Gestión Humana 2026</p>', unsafe_allow_html=True)
    st.markdown("### Plataforma interna — Acceso por módulos")

    col1, col2, col3 = st.columns(3)

    modulos = list(AREAS.keys())

    for i, area in enumerate(modulos):

        with [col1, col2, col3][i % 3]:

            st.markdown(f"""
            <div class="module-card">
                <div class="area-title">{area}</div>
                <div class="area-desc">Acceso seguro al módulo</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"INGRESAR — {area}", use_container_width=True):
                st.session_state.area_activa = area
                st.rerun()


# ===============================
# PANTALLA DE CONTRASEÑA
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
# PANEL DEL ÁREA
# ===============================
else:

    area = st.session_state.area_activa

    st.markdown(f"## 🧠 Módulo: {area}")

    if st.button("⬅ Volver al portal"):
        volver()
        st.rerun()

    st.markdown('<div class="panel-box">', unsafe_allow_html=True)

    # ========= CONTENIDO DEMO =========

    if area == "Reclutamiento":
        st.subheader("Procesos activos")
        st.metric("Convocatorias abiertas", 12, "+2")
        st.metric("Postulantes este mes", 348, "+15%")

    elif area == "Bienestar":
        st.subheader("Clima laboral")
        st.metric("Satisfacción general", "88%", "+3%")
        st.metric("Participación en actividades", "72%", "+5%")

    elif area == "Capacitación":
        st.subheader("Formación")
        st.metric("Cursos activos", 9)
        st.metric("Horas promedio", 18)

    elif area == "Administración":
        st.subheader("Gestión interna")
        st.metric("Documentos emitidos", 124)
        st.metric("Trámites pendientes", 7)

    elif area == "Indicadores":
        st.subheader("KPIs GH")
        st.metric("Rotación anual", "6.2%", "-0.8%")
        st.metric("Ausentismo", "2.1%", "-0.3%")

    elif area == "Seguridad y Salud":
        st.subheader("SST")
        st.metric("Accidentes reportados", 1)
        st.metric("Días sin accidentes", 84)

    st.markdown('</div>', unsafe_allow_html=True)
