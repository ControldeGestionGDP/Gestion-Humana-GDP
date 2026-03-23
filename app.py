import streamlit as st
from pathlib import Path

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Portal Gestión Humana GDP",
    page_icon="🐥",
    layout="wide"
)

# Paleta de Colores Corporativa
COLOR1 = "#1071B8" # Azul Primario
COLOR2 = "#2E3788" # Azul Oscuro
COLOR3 = "#C4579B" # Magenta

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
# ESTILOS "SUPER PRO" (CSS AVANZADO)
# =========================================================
st.markdown(f"""
<style>
    /* Fondo y Tipografía Global */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="st-"] {{
        font-family: 'Inter', sans-serif;
        background-color: #f8fafc;
    }}

    /* Header Ejecutivo Estilo Moderno */
    .executive-header {{
        background: linear-gradient(135deg, white 0%, #f1f5f9 100%);
        padding: 2rem;
        border-radius: 24px;
        border-left: 8px solid {COLOR1};
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }}

    .main-title {{
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, {COLOR2}, {COLOR1});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }}

    /* Tarjetas de Reporte Mejoradas */
    .card {{
        background: white;
        border-radius: 22px;
        padding: 0px;
        border: 1px solid #e2e8f0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        overflow: hidden;
        margin-bottom: 10px;
    }}

    .card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border-color: {COLOR1}44;
    }}

    .card-content {{
        padding: 20px;
    }}

    /* Botón Pro con Gradiente y Elevación */
    .btn-pro {{
        display: block;
        width: 100%;
        padding: 12px;
        text-align: center;
        background: linear-gradient(135deg, {COLOR1}, {COLOR2});
        color: white !important;
        font-weight: 700;
        text-decoration: none;
        border-radius: 12px;
        box-shadow: 0 4px 12px {COLOR1}44;
        transition: all 0.3s ease;
        border: none;
    }}

    .btn-pro:hover {{
        box-shadow: 0 6px 20px {COLOR1}66;
        transform: scale(1.02);
        filter: brightness(1.1);
    }}

    /* Estilos de la Sidebar Gerencial */
    .executive-card-sidebar {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid {COLOR1}22;
        text-align: center;
        margin-bottom: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIONES NIVELES PRO
# =========================================================
def report_card(titulo, desc, img_relative_path):
    img_path = ASSETS_DIR / img_relative_path
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    if img_path.exists():
        st.image(img_path.read_bytes(), use_container_width=True)
    else:
        st.image("https://via.placeholder.com/800x450?text=Grupo+Don+Pollo", use_container_width=True)
        
    st.markdown(f"""
        <div class="card-content">
            <div style="font-weight:800; font-size:1.15rem; color:{COLOR2};">{titulo}</div>
            <div style="font-size:0.9rem; color:#64748b; margin-top:5px; margin-bottom:15px;">{desc}</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def open_panel_button(url, key):
    st.markdown(f'<a href="{url}" target="_blank" class="btn-pro">📊 Abrir Dashboard</a>', unsafe_allow_html=True)
    st.write("") # Espaciador

# =========================================================
# 🔐 SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown(f"""
    <div class="executive-card-sidebar">
        <div style="font-size: 3rem;">💎</div>
        <div style="font-weight:800; color:{COLOR2}; text-transform:uppercase; letter-spacing:1px;">Acceso VIP</div>
        <div style="font-size:0.7rem; color:{COLOR1}; font-weight:700; margin-top:5px;">● GERENCIA GENERAL</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 INGRESAR PANEL CEO", use_container_width=True):
        st.session_state.area = "Gerencia"
        st.session_state.auth = False
        st.rerun()
    st.divider()

# =========================================================
# LOGICA DEL PORTAL
# =========================================================
if st.session_state.area is None:
    # Home Page
    st.markdown(f"""
    <div class="executive-header">
        <div class="main-title">Portal Gestión Humana</div>
        <div style="color:#64748b; font-weight:600; font-size:1.1rem;">Seleccione un área estratégica para continuar</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        report_card("Administración de Personal", "Control operativo y contractual", "Administracion.jpg")
        if st.button("Entrar a Operaciones", key="admin", use_container_width=True):
            st.session_state.area = "Administración de Personal"
            st.session_state.auth = False
            st.rerun()

    with col2:
        report_card("Desarrollo Organizacional", "Cultura, Talento y Clima", "Desarrollo.jpg")
        if st.button("Entrar a Desarrollo", key="do", use_container_width=True):
            st.session_state.area = "Desarrollo Organizacional"
            st.session_state.auth = False
            st.rerun()

    with col3:
        report_card("Seguridad y Salud", "Prevención y Bienestar SST", "Seguridad.jpg")
        if st.button("Entrar a SST", key="sst", use_container_width=True):
            st.session_state.area = "Seguridad y Salud en el Trabajo"
            st.session_state.auth = False
            st.rerun()

else:
    area = st.session_state.area

    if not st.session_state.auth:
        # Login Page Pro
        col1, col2, col3 = st.columns([1,1.5,1])
        with col2:
            st.markdown(f"""
            <div style="background:white; padding:40px; border-radius:24px; box-shadow: 0 20px 50px rgba(0,0,0,0.1); border-top: 6px solid {COLOR1};">
                <h2 style="text-align:center; color:{COLOR2}; margin-bottom:10px;">🔐 Autenticación</h2>
                <p style="text-align:center; color:#64748b;">Accediendo a: <b>{area}</b></p>
            """, unsafe_allow_html=True)
            
            pwd = st.text_input("Introduzca su clave de acceso", type="password")
            
            if st.button("Validar Credenciales", use_container_width=True):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Acceso denegado: Contraseña incorrecta")
            
            if st.button("← Volver al Inicio", use_container_width=True):
                st.session_state.area = None
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        # Dashboard Area Pro
        st.markdown(f"""
        <div class="executive-header">
            <div class="main-title">{area}</div>
            <div style="color:{COLOR3}; font-weight:700;">Indicadores de Gestión Estratégica</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("退出 Cerrar Sesión / Cambiar Área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        if area == "Gerencia":
            st.subheader("📊 Consolidado Administración de Personal")
            c1, c2, c3 = st.columns(3)
            with c1:
                report_card("Vacaciones", "Saldo y planificación", "Vacaciones.jpg")
                open_panel_button("https://app.powerbi.com/links/99-7IxzOn8?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g1")
            with c2:
                report_card("Descansos Médicos", "Subsidios y ausencias", "DescansosMedicos.jpg")
                open_panel_button("https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g2")
            with c3:
                report_card("Exámenes Médicos", "Seguimiento ocupacional", "Examenes.jpg")
                open_panel_button("https://app.powerbi.com/links/eAcPJmr1vJ?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g3")

            c_low1, c_low2, _ = st.columns(3)
            with c_low1:
                report_card("Medidas Disciplinarias", "Cumplimiento normativo", "Disciplinarias.jpg")
                open_panel_button("https://app.powerbi.com/links/Tpui1mE6E4?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_md")
            with c_low2:
                report_card("Casos Especiales", "Atención priorizada", "CasosEspeciales.jpg")
                open_panel_button("https://app.powerbi.com", "g_ce")

        elif area == "Administración de Personal":
            c1, c2, c3 = st.columns(3)
            with c1:
                report_card("Vacaciones", "Saldos actualizados", "Vacaciones.jpg")
                open_panel_button("https://app.powerbi.com/links/99-7IxzOn8?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "v")
            with c2:
                report_card("Descansos Médicos", "Gestión de subsidios", "DescansosMedicos.jpg")
                open_panel_button("https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "d")
            with c3:
                report_card("Exámenes Médicos", "Vencimientos y citas", "Examenes.jpg")
                open_panel_button("https://app.powerbi.com/links/eAcPJmr1vJ?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "e")

            c4, c5, _ = st.columns(3)
            with c4:
                report_card("Medidas Disciplinarias", "Control de sanciones", "Disciplinarias.jpg")
                open_panel_button("https://app.powerbi.com/links/Tpui1mE6E4?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "md")
            with c5:
                report_card("Casos Especiales", "Seguimiento individual", "CasosEspeciales.jpg")
                open_panel_button("https://app.powerbi.com", "ce")

        # Secciones DO y SST mantenidas con col2 centrada
        elif area == "Desarrollo Organizacional":
            _, col2, _ = st.columns([1,2,1])
            with col2:
                report_card("Capacitaciones", "Plan de formación anual", "Capacitaciones.jpg")
                open_panel_button("https://app.powerbi.com", "c")

        elif area == "Seguridad y Salud en el Trabajo":
            _, col2, _ = st.columns([1,2,1])
            with col2:
                report_card("Incidentes SST", "Reporte de accidentabilidad", "Incidentes.jpg")
                open_panel_button("https://app.powerbi.com", "i")

# Footer
st.markdown(f"""
    <div style="text-align:center; margin-top:50px; padding:20px; color:#94a3b8; font-size:0.85rem; border-top:1px solid #e2e8f0;">
        <b>Grupo Don Pollo</b> • Sistema de Inteligencia de Negocios 2026<br>
        Gerencia de Control de Gestión
    </div>
""", unsafe_allow_html=True)
