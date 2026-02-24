import streamlit as st
import random

# =============================
# CONFIG
# =============================
st.set_page_config(
    page_title="GH Control Center 2026",
    page_icon="🧠",
    layout="wide"
)

# =============================
# ESTILO EJECUTIVO CLARO
# =============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg,#f8fafc,#eef2ff);
    font-family: 'Segoe UI', sans-serif;
}
.title {
    font-size: 40px;
    font-weight: 800;
    color: #1e3a8a;
}
.module-card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    transition: 0.3s;
}
.module-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(37,99,235,0.18);
}
.panel-box {
    background: white;
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}
.alert-green {color: #16a34a; font-weight: 600;}
.alert-yellow {color: #ca8a04; font-weight: 600;}
.alert-red {color: #dc2626; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

# =============================
# ÁREAS
# =============================
AREAS = {
    "Administración de Personal": "admin2026",
    "Desarrollo Organizacional": "do2026",
    "Seguridad y Salud": "sst2026"
}

# =============================
# ESTADO
# =============================
if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False

def volver():
    st.session_state.area = None
    st.session_state.auth = False

# =============================
# KPIs DINÁMICOS (Simulación)
# =============================
colaboradores = random.randint(2700, 2900)
ausentismo = round(random.uniform(2.0, 4.5), 2)
rotacion = round(random.uniform(4.0, 7.0), 2)

def estado(valor, limite_bueno, limite_medio):
    if valor <= limite_bueno:
        return "alert-green", "Estable"
    elif valor <= limite_medio:
        return "alert-yellow", "Atención"
    else:
        return "alert-red", "Crítico"

# =============================
# PORTAL PRINCIPAL
# =============================
if st.session_state.area is None:

    st.markdown('<p class="title">GH Control Center 2026</p>', unsafe_allow_html=True)
    st.caption("Centro estratégico de Gestión Humana")

    st.markdown("### 📊 Estado Organizacional en Tiempo Real")

    c1, c2, c3 = st.columns(3)

    c1.metric("Colaboradores", colaboradores)
    c2.metric("Ausentismo %", ausentismo)
    c3.metric("Rotación %", rotacion)

    clase, texto = estado(ausentismo, 2.5, 3.5)
    st.markdown(f"<p class='{clase}'>Nivel de ausentismo: {texto}</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧭 Módulos GH")

    col1, col2, col3 = st.columns(3)

    for i, area in enumerate(AREAS.keys()):
        with [col1, col2, col3][i]:
            st.markdown(f"""
            <div class="module-card">
                <h4>{area}</h4>
                <p>Acceso al módulo estratégico</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Ingresar a {area}", use_container_width=True):
                st.session_state.area = area
                st.rerun()

# =============================
# CONTRASEÑA
# =============================
elif not st.session_state.auth:

    area = st.session_state.area
    st.markdown(f"## 🔐 Acceso a {area}")

    clave = st.text_input("Ingrese contraseña", type="password")

    if st.button("Acceder"):
        if clave == AREAS[area]:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")

    if st.button("⬅ Volver"):
        volver()
        st.rerun()

# =============================
# PANEL INTERNO
# =============================
else:

    area = st.session_state.area

    st.markdown(f"## 🧠 Módulo: {area}")

    if st.button("⬅ Volver al portal"):
        volver()
        st.rerun()

    st.markdown('<div class="panel-box">', unsafe_allow_html=True)

    if area == "Administración de Personal":
        st.metric("Vacaciones pendientes", random.randint(20, 40))
        st.metric("Asistencias irregulares", random.randint(3, 10))

    elif area == "Desarrollo Organizacional":
        st.metric("Clima laboral", f"{random.randint(75,90)}%")
        st.metric("Capacitaciones activas", random.randint(5, 15))

    elif area == "Seguridad y Salud":
        st.metric("Incidentes mes actual", random.randint(0, 3))
        st.metric("Días sin accidentes", random.randint(50, 120))

    st.markdown('</div>', unsafe_allow_html=True)
