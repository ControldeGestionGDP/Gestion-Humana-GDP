import streamlit as st
from pathlib import Path

# =========================================================
# CONFIGURACIÓN DE PÁGINA (ESTILO APP)
# =========================================================
st.set_page_config(
    page_title="Portal Gestión Humana GDP",
    page_icon="🐥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paleta de Colores Pro
COLOR1 = "#1071B8"  # Azul Principal
COLOR2 = "#0F172A"  # Slate Dark (Casi negro para textos)
COLOR3 = "#C4579B"  # Magenta de Acento
BG_LIGHT = "#FFFFFF" # Fondo Blanco Puro estilo Insta/FB

# =========================================================
# RUTA BASE
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =========================================================
# PASSWORDS (TU LÓGICA ORIGINAL)
# =========================================================
PASSWORDS = {
    "Administración de Personal": "pollo123",
    "Desarrollo Organizacional": "talento2024",
    "Seguridad y Salud en el Trabajo": "seguridad2024",
    "Gerencia": "gerencia2024"
}

if "area" not in st.session_state: st.session_state.area = None
if "auth" not in st.session_state: st.session_state.auth = False

# =========================================================
# 🎨 CSS ULTRA PRO (NIVEL PRODUCT DESIGN)
# =========================================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    /* Reset y Fondo */
    .stApp {{
        background-color: #F9FAFB;
        font-family: 'Inter', sans-serif;
    }}

    /* Títulos y Subtítulos */
    .main-title {{
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: {COLOR2};
        margin-bottom: 0.5rem;
    }}
    .subtitle {{
        color: #64748B;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }}

    /* Tarjetas Estilo Feed (Facebook/Insta) */
    .card-container {{
        background: white;
        border-radius: 24px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 25px;
    }}
    .card-container:hover {{
        transform: translateY(-8px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        border-color: {COLOR1}44;
    }}

    /* Estilo de Imagen en Card */
    .stImage > img {{
        border-radius: 20px 20px 0 0 !important;
    }}

    .card-content {{
        padding: 24px;
    }}
    .card-title-text {{
        font-weight: 700;
        font-size: 1.25rem;
        color: {COLOR2};
        margin-bottom: 8px;
    }}

    /* Botones Pro */
    div.stButton > button {{
        background: {COLOR1};
        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s;
        box-shadow: 0 4px 12px {COLOR1}33;
    }}
    div.stButton > button:hover {{
        background: {COLOR2};
        transform: scale(1.02);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }}

    /* Sidebar Executive Card */
    .executive-sidebar-card {{
        background: linear-gradient(135deg, {COLOR1}, {COLOR2});
        padding: 25px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }}

    /* Esconder Header de Streamlit para look de App */
    header {{visibility: hidden;}}
    #MainMenu {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 🔐 SIDEBAR GERENCIA
# =========================================================
with st.sidebar:
    st.markdown(f"""
    <div class="executive-sidebar-card">
        <div style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">PANEL EJECUTIVO</div>
        <div style="font-size: 0.8rem; opacity: 0.8;">Acceso Restringido a Gerencia General</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("INGRESAR A GERENCIA", use_container_width=True):
        st.session_state.area = "Gerencia"
        st.session_state.auth = False
        st.rerun()
    
    st.markdown("---")
    st.caption("© 2026 Grupo Don Pollo")

# =========================================================
# COMPONENTES DE DISEÑO
# =========================================================
def report_card_pro(titulo, desc, img_name):
    img_path = ASSETS_DIR / img_name
    
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    if img_path.exists():
        st.image(img_path.read_bytes(), use_container_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=500", use_container_width=True)
    
    st.markdown(f"""
        <div class="card-content">
            <div class="card-title-text">{titulo}</div>
            <div style="color: #64748B; font-size: 0.95rem; margin-bottom: 15px;">{desc}</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def open_dashboard_link(url):
    st.markdown(f"""
    <a href="{url}" target="_blank" style="text-decoration:none;">
        <div style="background:{COLOR1}; color:white; padding:12px; border-radius:12px; text-align:center; font-weight:700; margin-top:-15px; margin-bottom:20px; box-shadow: 0 4px 12px {COLOR1}33;">
            Abrir Dashboard
        </div>
    </a>
    """, unsafe_allow_html=True)

# =========================================================
# CUERPO DEL PORTAL
# =========================================================

# --- VISTA DE SELECCIÓN DE ÁREA ---
if st.session_state.area is None:
    st.markdown('<div class="main-title">Portal Gestión Humana</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Bienvenido al centro de inteligencia estratégica de Grupo Don Pollo</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        report_card_pro("Administración", "Gestión operativa y contratos", "Administracion.jpg")
        if st.button("Acceder", key="btn_adm"):
            st.session_state.area = "Administración de Personal"
            st.rerun()

    with col2:
        report_card_pro("Desarrollo Org.", "Cultura, Talento y Capacitación", "Desarrollo.jpg")
        if st.button("Acceder", key="btn_do"):
            st.session_state.area = "Desarrollo Organizacional"
            st.rerun()

    with col3:
        report_card_pro("Seguridad (SST)", "Salud ocupacional y prevención", "Seguridad.jpg")
        if st.button("Acceder", key="btn_sst"):
            st.session_state.area = "Seguridad y Salud en el Trabajo"
            st.rerun()

# --- VISTA DE LOGIN Y CONTENIDO ---
else:
    area = st.session_state.area

    if not st.session_state.auth:
        col_l1, col_l2, col_l3 = st.columns([1, 1.5, 1])
        with col_l2:
            st.markdown(f"""
            <div style="background:white; padding:40px; border-radius:30px; box-shadow:0 20px 40px rgba(0,0,0,0.05); border:1px solid #F1F5F9; margin-top:50px;">
                <h2 style="text-align:center; color:{COLOR1}; margin-bottom:10px;">Seguridad</h2>
                <p style="text-align:center; color:#64748B;">Módulo: <b>{area}</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            pwd = st.text_input("Ingresa la clave maestra", type="password")
            
            c_b1, c_b2 = st.columns(2)
            with c_b1:
                if st.button("Verificar"):
                    if pwd == PASSWORDS[area]:
                        st.session_state.auth = True
                        st.rerun()
                    else: st.error("Clave incorrecta")
            with c_b2:
                if st.button("Volver"):
                    st.session_state.area = None
                    st.rerun()
    else:
        # CONTENIDO AUTORIZADO
        st.markdown(f'<div class="main-title">{area}</div>', unsafe_allow_html=True)
        if st.button("← Salir del Módulo", use_container_width=False):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        # LOGICA DE GERENCIA (TU LOGICA ORIGINAL COMPLETA)
        if area == "Gerencia":
            st.subheader("📊 Consolidado Gerencial")
            row1_1, row1_2, row1_3 = st.columns(3)
            with row1_1:
                report_card_pro("Vacaciones", "Planificación", "Vacaciones.jpg")
                open_dashboard_link("https://app.powerbi.com/links/99-7IxzOn8...")
            with row1_2:
                report_card_pro("Descansos Médicos", "Ausentismo", "DescansosMedicos.jpg")
                open_dashboard_link("https://app.powerbi.com/links/NQfjSntCO1...")
            with row1_3:
                report_card_pro("Exámenes Médicos", "SST Ocupacional", "Examenes.jpg")
                open_dashboard_link("https://app.powerbi.com/links/eAcPJmr1vJ...")
            
            row2_1, row2_2, _ = st.columns(3)
            with row2_1:
                report_card_pro("Medidas Disciplinarias", "Sanciones", "Disciplinarias.jpg")
                open_dashboard_link("https://app.powerbi.com/links/Tpui1mE6E4...")
            with row2_2:
                report_card_pro("Casos Especiales", "Seguimiento", "CasosEspeciales.jpg")
                open_dashboard_link("https://app.powerbi.com")

        # LOGICA AREA: ADMINISTRACIÓN
        elif area == "Administración de Personal":
            c1, c2, c3 = st.columns(3)
            with c1:
                report_card_pro("Vacaciones", "Saldos", "Vacaciones.jpg")
                open_dashboard_link("https://app.powerbi.com/links/99-7IxzOn8...")
            with c2:
                report_card_pro("Descansos Médicos", "Subsidios", "DescansosMedicos.jpg")
                open_dashboard_link("https://app.powerbi.com/links/NQfjSntCO1...")
            with c3:
                report_card_pro("Exámenes Médicos", "Ocupacional", "Examenes.jpg")
                open_dashboard_link("https://app.powerbi.com/links/eAcPJmr1vJ...")

# FOOTER
st.markdown("<br><hr><center style='color:#94A3B8; font-size:0.85rem;'>Control de Gestión • Grupo Don Pollo • 2026</center>", unsafe_allow_html=True)
