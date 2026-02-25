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

.area-card {{
    background: white;
    border-radius: 18px;
    padding: 0.5rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
    box-shadow: 0 18px 40px rgba(0,0,0,0.08);
    border-top: 6px solid {COLOR1};
    transition: all 0.25s ease;
    overflow: hidden;
    height: 260px;
}}

.area-card:hover {{
    transform: translateY(-8px);
    border-top: 6px solid {COLOR3};
    box-shadow: 0 28px 60px rgba(0,0,0,0.12);
}}

.area-card img {{
    border-radius: 18px 18px 0 0;
    height: 160px;
    width: 100%;
    object-fit: cover;
}}

.area-card .area-title {{
    font-size:1.3rem;
    font-weight:700;
    color:{COLOR2};
    margin-top: 0.5rem;
    text-align: center;
}}

.login-box {{
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.12);
    border-top: 5px solid {COLOR1};
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
# FUNCIÓN TARJETA CON IMAGEN
# =========================================================
def area_card(name, img_file):
    img_path = ASSETS_DIR / img_file
    if not img_path.exists():
        st.warning(f"Imagen {img_file} no encontrada")
        return

    st.markdown('<div class="area-card">', unsafe_allow_html=True)
    st.image(str(img_path), use_column_width=True)
    st.markdown(f'<div class="area-title">{name}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
            area_card(name, img_file)
            clean_name = name.split(" ", 1)[1]
            if st.button("Ingresar", key=clean_name):
                st.session_state.area = clean_name
                st.session_state.auth = False
                st.rerun()

# =========================================================
# LOGIN Y DASHBOARDS
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

        # ADMINISTRACIÓN DE PERSONAL
        if area == "Administración de Personal":
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(str(ASSETS_DIR / "Vacaciones.jpg"), use_column_width=True)
                st.markdown("<div style='font-weight:700;'>Vacaciones</div>", unsafe_allow_html=True)
            with col2:
                st.image(str(ASSETS_DIR / "DescansosMedicos.jpg"), use_column_width=True)
                st.markdown("<div style='font-weight:700;'>Descansos Médicos</div>", unsafe_allow_html=True)
            with col3:
                st.image(str(ASSETS_DIR / "Examenes.jpg"), use_column_width=True)
                st.markdown("<div style='font-weight:700;'>Exámenes Médicos</div>", unsafe_allow_html=True)

        # DESARROLLO ORGANIZACIONAL
        elif area == "Desarrollo Organizacional":
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.image(str(ASSETS_DIR / "Capacitaciones.jpg"), use_column_width=True)
                st.markdown("<div style='font-weight:700;'>Capacitaciones</div>", unsafe_allow_html=True)

        # SEGURIDAD Y SALUD
        elif area == "Seguridad y Salud en el Trabajo":
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.image(str(ASSETS_DIR / "Incidentes.jpg"), use_column_width=True)
                st.markdown("<div style='font-weight:700;'>Incidentes SST</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#9ca3af;margin-top:40px;'>Gerencia de Control de Gestión • Transformación Digital</center>",
    unsafe_allow_html=True
)
