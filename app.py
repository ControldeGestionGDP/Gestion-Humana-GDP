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

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

PASSWORDS = {
    "Administración de Personal": "pollo123",
    "Desarrollo Organizacional": "talento2024",
    "Seguridad y Salud en el Trabajo": "seguridad2024"
}

if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False


# =========================================================
# ESTILOS (ROSADO + AZUL)
# =========================================================
st.markdown(f"""
<style>

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

.card {{
    background: white;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 20px 45px rgba(0,0,0,0.12);
    transition: transform 0.35s ease;
}}

.card:hover {{
    transform: translateY(-6px);
}}

.card img {{
    width: 100%;
    height: 240px;   /* 👈 MISMO TAMAÑO PARA TODAS */
    object-fit: cover;
}}

.card-body {{
    padding: 20px;
    text-align: center;
}}

.card-title {{
    font-weight: 700;
    font-size: 1.2rem;
    color: {COLOR2};
}}

.card-desc {{
    font-size: 0.95rem;
    color: #6b7280;
    margin-bottom: 14px;
}}

.stButton > button {{
    background: linear-gradient(90deg,{COLOR1},{COLOR2},{COLOR3});
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TARJETA CON BOTÓN
# =========================================================
def card(titulo, desc, img_file, action=None, link=None):

    img_path = ASSETS_DIR / img_file

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if img_path.exists():
        st.image(str(img_path), use_container_width=True)

    st.markdown(f"""
        <div class="card-body">
            <div class="card-title">{titulo}</div>
            <div class="card-desc">{desc}</div>
        </div>
    """, unsafe_allow_html=True)

    if action:
        if st.button("Ingresar", key=titulo):
            action()

    if link:
        st.markdown(f"""
            <a href="{link}" target="_blank">
                <button style="width:100%;padding:10px;
                background:linear-gradient(90deg,{COLOR1},{COLOR2},{COLOR3});
                border:none;border-radius:10px;color:white;font-weight:600;">
                Ingresar
                </button>
            </a>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# PORTAL PRINCIPAL (ÁREAS)
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Portal Gestión Humana</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione una línea de gestión</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "Administración de Personal",
            "Vacaciones, descansos y exámenes",
            "Administracion.jpg",
            action=lambda: (
                st.session_state.update({"area": "Administración de Personal"}),
                st.rerun()
            )
        )

    with col2:
        card(
            "Desarrollo Organizacional",
            "Capacitaciones y desempeño",
            "Desarrollo.jpg",
            action=lambda: (
                st.session_state.update({"area": "Desarrollo Organizacional"}),
                st.rerun()
            )
        )

    with col3:
        card(
            "Seguridad y Salud en el Trabajo",
            "Indicadores SST",
            "Seguridad.jpg",
            action=lambda: (
                st.session_state.update({"area": "Seguridad y Salud en el Trabajo"}),
                st.rerun()
            )
        )


# =========================================================
# LOGIN
# =========================================================
else:

    area = st.session_state.area

    if not st.session_state.auth:

        st.subheader(area)
        pwd = st.text_input("Contraseña", type="password")

        if st.button("Ingresar"):
            if pwd == PASSWORDS[area]:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

        if st.button("Volver"):
            st.session_state.area = None
            st.rerun()


# =========================================================
# DASHBOARD INTERNO
# =========================================================
    else:

        st.header(area)

        if st.button("Cambiar área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                card(
                    "Vacaciones",
                    "Saldo y planificación",
                    "Vacaciones.jpg",
                    link="https://app.powerbi.com"
                )

            with col2:
                card(
                    "Descansos Médicos",
                    "Subsidios y ausencias",
                    "DescansosMedicos.jpg",
                    link="https://app.powerbi.com"
                )

            with col3:
                card(
                    "Exámenes Médicos",
                    "Seguimiento ocupacional",
                    "Examenes.jpg",
                    link="https://app.powerbi.com"
                )


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#9ca3af;margin-top:40px;'>Gerencia de Control de Gestión • Transformación Digital</center>",
    unsafe_allow_html=True
)
