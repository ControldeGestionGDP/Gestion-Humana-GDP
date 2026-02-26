import streamlit as st
from pathlib import Path

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Portal Gestión Humana",
    page_icon="📊",
    layout="wide"
)

COLOR1 = "#1071B8"
COLOR2 = "#2E3788"
COLOR3 = "#C4579B"

# =========================================================
# RUTA BASE
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
# ESTILOS
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

.card {{
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    margin-bottom: 10px;
}}

.card img {{
    border-radius: 18px;
}}

.card-title {{
    padding: 15px;
    font-weight: 700;
    font-size: 1.1rem;
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
# FUNCIÓN TARJETA SEGURA
# =========================================================
def report_card(titulo, desc, img_relative_path):

    img_path = ASSETS_DIR / img_relative_path
    fallback = ASSETS_DIR / "default.jpg"

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Mostrar imagen segura
    if img_path.exists():
        st.image(img_path.read_bytes(), use_container_width=True)
    elif fallback.exists():
        st.image(fallback.read_bytes(), use_container_width=True)
    else:
        st.image("https://via.placeholder.com/800x400.png?text=Imagen+no+disponible",
                 use_container_width=True)

    st.markdown(f"""
        <div class="card-title">
            {titulo}<br>
            <span style="font-weight:400;color:#6b7280;font-size:0.95rem;">
                {desc}
            </span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Portal Gestión Humana</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione una línea de gestión</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        report_card("Administración de Personal",
                    "Gestión operativa del personal",
                    "Administracion.jpg")

        if st.button("Ingresar Administración", key="admin"):
            st.session_state.area = "Administración de Personal"
            st.session_state.auth = False
            st.rerun()

    with col2:
        report_card("Desarrollo Organizacional",
                    "Talento y cultura",
                    "Desarrollo.jpg")

        if st.button("Ingresar Desarrollo", key="do"):
            st.session_state.area = "Desarrollo Organizacional"
            st.session_state.auth = False
            st.rerun()

    with col3:
        report_card("Seguridad y Salud en el Trabajo",
                    "Gestión preventiva",
                    "Seguridad.jpg")

        if st.button("Ingresar SST", key="sst"):
            st.session_state.area = "Seguridad y Salud en el Trabajo"
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
                report_card("Vacaciones", "Saldo y planificación", "Vacaciones.jpg")

            with col2:
                report_card("Descansos Médicos", "Subsidios y ausencias", "DescansosMedicos.jpg")

            with col3:
                report_card("Exámenes Médicos", "Seguimiento ocupacional", "Examenes.jpg")

        elif area == "Desarrollo Organizacional":

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                report_card("Capacitaciones", "Panel en construcción", "Capacitaciones.jpg")

        elif area == "Seguridad y Salud en el Trabajo":

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                report_card("Incidentes SST", "Panel en construcción", "Incidentes.jpg")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#9ca3af;margin-top:40px;'>Gerencia de Control de Gestión • Transformación Digital</center>",
    unsafe_allow_html=True
)
