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

# ===== COLORES CORPORATIVOS =====
COLOR1 = "#1071B8"
COLOR2 = "#2E3788"
COLOR3 = "#C4579B"

# =========================================================
# RUTA BASE (FUNCIONA EN LOCAL Y CLOUD)
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
# ESTILOS SaaS PREMIUM
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

.area-card {{
    background: white;
    border-radius: 18px;
    height: 240px;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    box-shadow: 0 18px 40px rgba(0,0,0,0.08);
    border-top: 6px solid {COLOR1};
    transition: all 0.25s ease;
}}

.area-card:hover {{
    transform: translateY(-8px);
    border-top: 6px solid {COLOR3};
    box-shadow: 0 28px 60px rgba(0,0,0,0.12);
}}

.login-box {{
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.12);
    border-top: 5px solid {COLOR1};
}}

.report-card img {{
    border-radius: 18px;
    transition: transform 0.4s ease;
}}

.report-card:hover img {{
    transform: scale(1.05);
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

.desc {{
    font-weight: 400;
    font-size: 0.95rem;
}}

div.stButton > button {{
    background: linear-gradient(90deg, {COLOR1}, {COLOR2}, {COLOR3});
    color: white;
    border-radius: 999px;
    border: none;
    font-weight: 700;
    height: 45px;
    transition: 0.3s;
}}

div.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIÓN TARJETA PRO (CLOUD SAFE)
# =========================================================
def report_card(titulo, desc, link, img_relative_path):

    img_path = ASSETS_DIR / img_relative_path
    fallback = ASSETS_DIR / "default.jpg"
    img_to_use = img_path if img_path.exists() else fallback

    st.markdown('<div class="report-card">', unsafe_allow_html=True)

    if img_to_use.exists():
        st.image(str(img_to_use), use_container_width=True)
    else:
        st.warning("Imagen no encontrada y no existe default.jpg")

    st.markdown(f"""
    <div class="overlay">
        {titulo}
        <div class="desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("Abrir reporte", link, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Portal Gestión Humana</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione una línea de gestión</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    areas = [
        ("👥 Administración de Personal"),
        ("📚 Desarrollo Organizacional"),
        ("🦺 Seguridad y Salud en el Trabajo")
    ]

    for col, name in zip([col1, col2, col3], areas):
        with col:

            st.markdown(f"""
            <div class="area-card">
                <div style="font-size:1.3rem;font-weight:700;color:{COLOR2};">
                    {name}
                </div>
            </div>
            """, unsafe_allow_html=True)

            clean_name = name.split(" ", 1)[1]

            if st.button("Ingresar", key=clean_name):
                st.session_state.area = clean_name
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

        # ADMINISTRACIÓN DE PERSONAL (3 REALES)
        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                report_card("Vacaciones", "Saldo y planificación",
                            "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare",
                            "Vacaciones.jpg")

            with col2:
                report_card("Descansos Médicos", "Subsidios y ausencias",
                            "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare",
                            "DescansosMedicos.jpg")

            with col3:
                report_card("Exámenes Médicos", "Seguimiento ocupacional",
                            "https://app.powerbi.com/links/eAcPJmr1vJ?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare",
                            "Examenes.jpg")

        # DESARROLLO ORGANIZACIONAL (1 FICTICIO)
        elif area == "Desarrollo Organizacional":

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                report_card("Capacitaciones",
                            "Panel en construcción",
                            "https://app.powerbi.com",
                            "Capacitaciones.jpg")

        # SEGURIDAD Y SALUD (1 FICTICIO)
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
