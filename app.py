import streamlit as st
from pathlib import Path

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Portal Gestión Humana GDP",
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
    "Seguridad y Salud en el Trabajo": "seguridad2024",
    "Gerencia": "gerencia2024"
}

# =========================================================
# SESSION STATE
# =========================================================
if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False


# =========================================================
# 🔐 SIDEBAR GERENCIA
# =========================================================
with st.sidebar:
    st.markdown("### 🔐 Acceso Ejecutivo")

    if st.button("Panel Gerencial"):
        st.session_state.area = "Gerencia"
        st.session_state.auth = False
        st.rerun()


# =========================================================
# ESTILOS (TU MISMO BLOQUE ORIGINAL)
# =========================================================
st.markdown(f"""
<style>
html, body {{
    font-family: "Segoe UI", sans-serif;
    background: #f4f6fb;
    animation: fadeInBody 0.6s ease-in-out;
}}
@keyframes fadeInBody {{
    from {{ opacity: 0; transform: translateY(8px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
.main-title {{
    font-size: 2.6rem;
    font-weight: 800;
    color: {COLOR2};
    animation: slideInTitle 0.7s ease;
}}
@keyframes slideInTitle {{
    from {{ opacity: 0; transform: translateX(-10px); }}
    to {{ opacity: 1; transform: translateX(0); }}
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
    animation: expandBar 0.8s ease forwards;
}}
@keyframes expandBar {{
    from {{ width: 0; }}
    to {{ width: 120px; }}
}}
.login-box {{
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.12);
    border-top: 5px solid {COLOR1};
    animation: fadeInCard 0.5s ease;
}}
@keyframes fadeInCard {{
    from {{ opacity: 0; transform: translateY(12px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
.card {{
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    margin-bottom: 8px;
    background: white;
    transition: all 0.35s cubic-bezier(.4,0,.2,1);
}}
.card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 25px 55px rgba(0,0,0,0.18);
}}
.card img {{
    border-radius: 18px;
    transition: transform 0.4s ease;
}}
.card:hover img {{
    transform: scale(1.04);
}}
.card-title {{
    padding: 15px;
    font-weight: 700;
    font-size: 1.1rem;
}}
div.stButton > button {{
    width: 100%;
    background: linear-gradient(90deg, {COLOR1}, {COLOR2}, {COLOR3});
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 700;
    height: 45px;
    transition: all 0.25s ease;
}}
div.stButton > button:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 22px rgba(0,0,0,0.2);
}}
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCIONES (SIN CAMBIOS)
# =========================================================
def report_card(titulo, desc, img_relative_path):
    img_path = ASSETS_DIR / img_relative_path
    fallback = ASSETS_DIR / "default.jpg"

    st.markdown('<div class="card">', unsafe_allow_html=True)

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


def open_panel_button(url, key):
    st.markdown(f"""
    <a href="{url}" target="_blank" style="text-decoration:none;">
        <div style="
            width:100%;
            text-align:center;
            padding:12px;
            border-radius:10px;
            font-weight:700;
            color:white;
            background: linear-gradient(90deg,{COLOR1},{COLOR2},{COLOR3});
            box-shadow: 0 6px 14px rgba(0,0,0,0.15);
        ">
            Abrir Dashboard
        </div>
    </a>
    """, unsafe_allow_html=True)


# =========================================================
# PORTAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Panel de Control — Gestión Humana GDP</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione el área de interés</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        report_card("Administración de Personal",
                    "Gestión operativa del personal",
                    "Administracion.jpg")
        if st.button("Ingresar", key="admin", use_container_width=True):
            st.session_state.area = "Administración de Personal"
            st.session_state.auth = False
            st.rerun()

    with col2:
        report_card("Desarrollo Organizacional",
                    "Talento y cultura",
                    "Desarrollo.jpg")
        if st.button("Ingresar", key="do", use_container_width=True):
            st.session_state.area = "Desarrollo Organizacional"
            st.session_state.auth = False
            st.rerun()

    with col3:
        report_card("Seguridad y Salud en el Trabajo",
                    "Gestión preventiva",
                    "Seguridad.jpg")
        if st.button("Ingresar", key="sst", use_container_width=True):
            st.session_state.area = "Seguridad y Salud en el Trabajo"
            st.session_state.auth = False
            st.rerun()

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

        # ================= GERENCIA VE TODO =================
        if area == "Gerencia":

            st.subheader("Administración de Personal")
            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Vacaciones", "Saldo y planificación", "Vacaciones.jpg")
                open_panel_button("https://app.powerbi.com/links/1TThJ-ia9c", "g1")
            with col2:
                report_card("Descansos Médicos", "Subsidios y ausencias", "DescansosMedicos.jpg")
                open_panel_button("https://app.powerbi.com/links/NQfjSntCO1", "g2")
            with col3:
                report_card("Exámenes Médicos", "Seguimiento ocupacional", "Examenes.jpg")
                open_panel_button("https://app.powerbi.com/links/eAcPJmr1vJ", "g3")
            
            # Segunda fila alineada a la izquierda
            col_g4, col_g5, _ = st.columns(3)
            with col_g4:
                report_card("Medidas Disciplinarias", "Registro de sanciones", "Disciplinarias.jpg")
                open_panel_button("https://app.powerbi.com", "g_md")
            with col_g5:
                report_card("Casos Especiales", "Seguimiento de casos", "CasosEspeciales.jpg")
                open_panel_button("https://app.powerbi.com", "g_ce")

            st.divider()
            st.subheader("Desarrollo Organizacional")
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                report_card("Capacitaciones", "Panel en construcción", "Capacitaciones.jpg")
                open_panel_button("https://app.powerbi.com", "g4")

            st.divider()
            st.subheader("Seguridad y Salud en el Trabajo")
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                report_card("Incidentes SST", "Panel en construcción", "Incidentes.jpg")
                open_panel_button("https://app.powerbi.com", "g5")

       # ================= AREAS NORMALES =================
        elif area == "Administración de Personal":

            # Primera fila (3 columnas)
            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Vacaciones", "Saldo y planificación", "Vacaciones.jpg")
                open_panel_button("https://app.powerbi.com/links/99-7IxzOn8?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "v")
            with col2:
                report_card("Descansos Médicos", "Subsidios y ausencias", "DescansosMedicos.jpg")
                open_panel_button("https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "d")
            with col3:
                report_card("Exámenes Médicos", "Seguimiento ocupacional", "Examenes.jpg")
                open_panel_button("https://app.powerbi.com/links/eAcPJmr1vJ?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "e")
            
            # Segunda fila alineada a la izquierda (3 columnas, la última vacía)
            col_a4, col_a5, _ = st.columns(3)
            with col_a4:
                report_card("Medidas Disciplinarias", "Registro de sanciones", "Disciplinarias.jpg")
                open_panel_button("https://app.powerbi.com", "md")
            with col_a5:
                report_card("Casos Especiales", "Seguimiento de casos", "CasosEspeciales.jpg")
                open_panel_button("https://app.powerbi.com", "ce")

        elif area == "Desarrollo Organizacional":
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                report_card("Capacitaciones", "Panel en construcción", "Capacitaciones.jpg")
                open_panel_button("https://app.powerbi.com", "c")

        elif area == "Seguridad y Salud en el Trabajo":
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                report_card("Incidentes SST", "Panel en construcción", "Incidentes.jpg")
                open_panel_button("https://app.powerbi.com", "i")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#9ca3af;margin-top:40px;'>Gerencia de Control de Gestión • Grupo Don Pollo</center>",
    unsafe_allow_html=True
)
