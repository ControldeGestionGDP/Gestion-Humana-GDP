import streamlit as st
from pathlib import Path
import base64

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Portal Gestión Humana",
    page_icon="📊",
    layout="wide"
)

# ===== COLORES =====
COLOR1 = "#1071B8"
COLOR2 = "#2E3788"
COLOR3 = "#C4579B"

# =========================================================
# RUTAS
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =========================================================
# PASSWORDS
# =========================================================
PASSWORDS = {
    "Administración de Personal": "pollo123",
    "Desarrollo Organizacional": "talento2024",
    "Seguridad y Salud en el Trabajo": "seguridad2024"
}

# =========================================================
# SESSION STATE
# =========================================================
if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False

# =========================================================
# FUNCION: CONVERTIR IMAGEN A BASE64
# =========================================================
def img_to_base64(path):
    if not path.exists():
        path = ASSETS_DIR / "default.jpg"
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# =========================================================
# CSS PREMIUM
# =========================================================
st.markdown(f"""
<style>

html, body {{
    font-family: "Segoe UI", sans-serif;
    background: #f4f6fb;
}}

.main-title {{
    font-size: 2.6rem;
    font-weight: 800;
    color: {COLOR2};
}}

.subtitle {{
    color: #6b7280;
    margin-bottom: 12px;
}}

.title-accent {{
    height: 4px;
    width: 120px;
    background: linear-gradient(90deg,{COLOR1},{COLOR2},{COLOR3});
    border-radius: 4px;
    margin-bottom: 28px;
}}

.login-box {{
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.12);
    border-top: 5px solid {COLOR1};
}}

.card-img {{
    width: 100%;
    height: 260px;        /* 🔥 MISMO TAMAÑO REAL */
    object-fit: cover;    /* 🔥 RECORTE PRO */
    border-radius: 18px;
}}

.overlay {{
    position: relative;
    margin-top: -110px;
    padding: 20px;
    color: white;
    font-weight: 700;
    font-size: 1.2rem;
    background: linear-gradient(transparent, rgba(0,0,0,0.85));
    border-bottom-left-radius: 18px;
    border-bottom-right-radius: 18px;
}}

div.stButton > button {{
    background: linear-gradient(90deg, {COLOR1}, {COLOR2}, {COLOR3});
    color: white;
    border-radius: 999px;
    border: none;
    font-weight: 700;
    height: 45px;
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TARJETA CON TAMAÑO PERFECTO
# =========================================================
def report_card(titulo, desc, link, img_file):

    img_path = ASSETS_DIR / img_file
    img_base64 = img_to_base64(img_path)

    st.markdown(f"""
    <img src="data:image/jpg;base64,{img_base64}" class="card-img">
    <div class="overlay">
        {titulo}
        <div style="font-weight:400;font-size:0.95rem;">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("Abrir reporte", link, use_container_width=True)

# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Portal Gestión Humana</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione una línea de gestión</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    areas = [
        ("Administración de Personal", "Administracion.jpg"),
        ("Desarrollo Organizacional", "Desarrollo.jpg"),
        ("Seguridad y Salud en el Trabajo", "Seguridad.jpg")
    ]

    for col, (name, img_file) in zip([col1, col2, col3], areas):

        with col:

            img_base64 = img_to_base64(ASSETS_DIR / img_file)

            st.markdown(f"""
            <img src="data:image/jpg;base64,{img_base64}" class="card-img">
            <div class="overlay">{name}</div>
            """, unsafe_allow_html=True)

            if st.button("Ingresar", key=name):
                st.session_state.area = name
                st.session_state.auth = False
                st.rerun()

# =========================================================
# LOGIN
# =========================================================
else:

    area = st.session_state.area

    if not st.session_state.auth:

        col1, col2, col3 = st.columns([1,2,1])

        with col2:

            st.markdown(f"""
            <div class="login-box">
                <div style="font-size:1.4rem;font-weight:700;color:{COLOR2};text-align:center;">
                    {area}
                </div>
                <div style="text-align:center;color:#6b7280;margin-bottom:20px;">
                    Ingrese su contraseña
                </div>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("Contraseña", type="password")

            if st.button("Ingresar", use_container_width=True):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Contraseña incorrecta")

            if st.button("Volver", use_container_width=True):
                st.session_state.area = None
                st.rerun()

# =========================================================
# DASHBOARDS
# =========================================================
    else:

        st.markdown(f'<div class="main-title">{area}</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

        if st.button("Cambiar área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                report_card("Vacaciones", "Saldo y planificación",
                            "https://app.powerbi.com",
                            "Vacaciones.jpg")

            with col2:
                report_card("Descansos Médicos", "Subsidios y ausencias",
                            "https://app.powerbi.com",
                            "DescansosMedicos.jpg")

            with col3:
                report_card("Exámenes Médicos", "Seguimiento ocupacional",
                            "https://app.powerbi.com",
                            "Examenes.jpg")

        elif area == "Desarrollo Organizacional":

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                report_card("Capacitaciones",
                            "Panel en construcción",
                            "https://app.powerbi.com",
                            "Capacitaciones.jpg")

        elif area == "Seguridad y Salud en el Trabajo":

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                report_card("Incidentes SST",
                            "Panel en construcción",
                            "https://app.powerbi.com",
                            "Incidentes.jpg")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#9ca3af;margin-top:40px;'>Gerencia de Control de Gestión • Transformación Digital</center>",
    unsafe_allow_html=True
)
