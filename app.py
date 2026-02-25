import streamlit as st
from pathlib import Path

# ================= CONFIG =================
st.set_page_config(
    page_title="Portal Gestión Humana",
    layout="wide"
)

# ===== COLORES CORPORATIVOS =====
COLOR1 = "#1071B8"
COLOR2 = "#2E3788"
COLOR3 = "#C4579B"

# ================= ESTILOS =================
st.markdown(f"""
<style>

html, body, [class*="css"] {{
    font-family: "Segoe UI", sans-serif;
    background: #f4f6fb;
}}

.main-title {{
    font-size: 2.4rem;
    font-weight: 800;
    color: {COLOR2};
}}

.subtitle {{
    color: #6b7280;
    margin-bottom: 20px;
}}

.card-container {{
    border-radius: 18px;
    overflow: hidden;
    background: white;
    box-shadow: 0 14px 40px rgba(0,0,0,0.08);
    transition: 0.35s;
}}

.card-container:hover {{
    transform: translateY(-8px);
    box-shadow: 0 25px 70px rgba(0,0,0,0.15);
}}

.overlay {{
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 18px;
    color: white;
    background: linear-gradient(transparent, rgba(0,0,0,0.75));
}}

.title-text {{
    font-weight: 700;
    font-size: 1.2rem;
}}

.desc-text {{
    font-size: 0.95rem;
}}

div.stButton > button {{
    background: linear-gradient(90deg, {COLOR1}, {COLOR2}, {COLOR3});
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
    height: 45px;
    transition: 0.3s;
}}

div.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}}

</style>
""", unsafe_allow_html=True)

# ================= FUNCIÓN TARJETA =================

def report_card(titulo, desc, link, img_path):

    path = Path(img_path)

    if path.exists():
        st.image(img_path, use_container_width=True)
    else:
        st.warning(f"No se encontró la imagen: {img_path}")

    st.markdown(f"""
    <div style="
        margin-top:-95px;
        padding:18px;
        color:white;
        font-weight:700;
        font-size:1.2rem;
        background: linear-gradient(transparent, rgba(0,0,0,0.8));
    ">
        {titulo}
        <div style="font-weight:400;font-size:0.95rem;">
            {desc}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("Abrir reporte", link, use_container_width=True)


# ================= HEADER =================

st.markdown('<div class="main-title">Portal de Gestión Humana</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Plataforma centralizada de indicadores y reportes</div>', unsafe_allow_html=True)

st.divider()

# ================= MÓDULOS =================

col1, col2, col3 = st.columns(3)

with col1:
    report_card(
        "Descansos Médicos",
        "Seguimiento, subsidios y control de ausencias",
        "https://google.com",
        "assets/DescansosMedicos.jpg"
    )

with col2:
    report_card(
        "Vacaciones",
        "Planificación y control anual",
        "https://google.com",
        "assets/Vacaciones.jpg"
    )

with col3:
    report_card(
        "Subsidios",
        "Gestión de pagos y recuperos EsSalud",
        "https://google.com",
        "assets/Subsidios.jpg"
    )

st.divider()

# ================= FOOTER =================

st.markdown(
    "<center style='color:#9ca3af'>Portal Corporativo • Gestión Humana</center>",
    unsafe_allow_html=True
)
