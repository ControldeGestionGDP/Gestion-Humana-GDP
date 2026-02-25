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

/* TARJETA */
.card {{
    position: relative;
    border-radius: 18px;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.35s ease;
}}

.card:hover {{
    transform: translateY(-6px);
}}

.card img {{
    width: 100%;
    height: 260px;
    object-fit: cover;
    transition: transform 0.4s ease;
}}

.card:hover img {{
    transform: scale(1.05);
}}

.overlay {{
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 20px;
    color: white;
    font-weight: 700;
    font-size: 1.2rem;
    background: linear-gradient(transparent, rgba(0,0,0,0.85));
}}

.desc {{
    font-weight: 400;
    font-size: 0.95rem;
}}

.login-box {{
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.12);
    border-top: 5px solid {COLOR1};
}}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TARJETA CLICKEABLE
# =========================================================
def card(titulo, desc, img_relative_path, action=None, link=None):

    img_path = ASSETS_DIR / img_relative_path
    fallback = ASSETS_DIR / "default.jpg"
    img_to_use = img_path if img_path.exists() else fallback

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if img_to_use.exists():
        st.image(str(img_to_use), use_container_width=True)

    st.markdown(f"""
        <div class="overlay">
            {titulo}
            <div class="desc">{desc}</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if action:
        if st.button(f"abrir_{titulo}", key=titulo):
            action()

    if link:
        st.markdown(f"""
            <script>
                const cards = window.parent.document.querySelectorAll('.card');
                cards[cards.length - 1].onclick = function() {{
                    window.open("{link}", "_blank");
                }};
            </script>
        """, unsafe_allow_html=True)


# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Portal Gestión Humana</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione una línea de gestión</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "👥 Administración de Personal",
            "Vacaciones, descansos y exámenes",
            "Administracion.jpg",
            action=lambda: (
                st.session_state.update({"area": "Administración de Personal"}),
                st.rerun()
            )
        )

    with col2:
        card(
            "📚 Desarrollo Organizacional",
            "Capacitaciones y desempeño",
            "Desarrollo.jpg",
            action=lambda: (
                st.session_state.update({"area": "Desarrollo Organizacional"}),
                st.rerun()
            )
        )

    with col3:
        card(
            "🦺 Seguridad y Salud en el Trabajo",
            "Indicadores SST",
            "Seguridad.jpg",
            action=lambda: (
                st.session_state.update({"area": "Seguridad y Salud en el Trabajo"}),
                st.rerun()
            )
        )

# =========================================================
# LOGIN + DASHBOARD
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
