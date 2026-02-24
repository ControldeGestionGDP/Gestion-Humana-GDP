import streamlit as st

# Configuración de página
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="⚡")

# =========================================================
# DISEÑO CYBER-EXECUTIVE 2.0 (CSS)
# =========================================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500;800&display=swap');

    .stApp {{
        background: radial-gradient(circle at 50% 50%, #ffffff 0%, #e1e8f0 100%);
    }}

    /* Título con Neón Animado */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        filter: drop-shadow(0 2px 10px rgba(16, 113, 184, 0.2));
    }}

    /* Selector de Áreas Estilizado */
    .stSelectbox div[data-baseweb="select"] {{
        background-color: white !important;
        border: 2px solid #1071b8 !important;
        border-radius: 15px !important;
        font-family: 'Orbitron', sans-serif !important;
    }}

    /* TARJETA MEJORADA */
    .card {{
        position: relative;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 25px;
        border: 1px solid rgba(46, 55, 136, 0.1);
        padding: 40px 20px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        min-height: 380px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }}

    .card:hover {{
        transform: scale(1.05);
        border-color: #c4579b;
        box-shadow: 0 25px 50px rgba(196, 87, 155, 0.2);
    }}

    .icon-box {{
        font-size: 55px;
        margin-bottom: 15px;
        transition: 0.5s;
    }}
    
    .card:hover .icon-box {{
        transform: rotateY(180deg);
    }}

    .card-title {{
        font-family: 'Orbitron', sans-serif;
        color: #2e3788;
        font-size: 1.1rem;
        letter-spacing: 1px;
        margin-bottom: 15px;
    }}

    .launch-btn {{
        background: linear-gradient(90deg, #1071b8, #2e3788);
        color: white !important;
        padding: 10px 25px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 0.8rem;
        display: inline-block;
        margin-top: 20px;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(16, 113, 184, 0.3);
    }}

    .launch-btn:hover {{
        background: #c4579b;
        box-shadow: 0 8px 20px rgba(196, 87, 155, 0.4);
    }}
</style>
""", unsafe_allow_html=True)

# =========================================================
# ESTRUCTURA DE NAVEGACIÓN
# =========================================================

st.markdown('<h1 class="main-title">GH INTELLIGENCE HUB</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#64748b; margin-bottom:40px;'>GRUPO DON POLLO | SISTEMA DE GESTIÓN CENTRALIZADO</p>", unsafe_allow_html=True)

# SELECTOR DE DIMENSIÓN (El Menú Táctico)
col_menu, _ = st.columns([2, 2])
with col_menu:
    area_seleccionada = st.selectbox(
        "SELECCIONE LÍNEA DE GESTIÓN:",
        ["💼 NÓMINAS & ADMINISTRACIÓN", "🦺 SEGURIDAD Y SALUD (SST)", "📈 DESARROLLO ORGANIZACIONAL"]
    )

st.markdown("---")

# Función para renderizar tarjetas
def render_card(icon, title, desc, link):
    st.markdown(f"""
        <div class="card">
            <div class="icon-box">{icon}</div>
            <div class="card-title">{title}</div>
            <p style="color: #64748b; font-size: 0.9rem;">{desc}</p>
            <div>
                <a href="{link}" target="_blank" class="launch-btn">SOLICITAR ACCESO / ABRIR</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# =========================================================
# LÓGICA DE ÁREAS
# =========================================================

if "NÓMINAS" in area_seleccionada:
    st.subheader("📁 Gestión de Nóminas y Personal")
    c1, c2, c3 = st.columns(3)
    with c1:
        render_card("🏖️", "VACACIONES", "Control detallado de saldos y planificación anual.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
    with c2:
        render_card("🚑", "DESCANSOS MÉDICOS", "Registro y trazabilidad de licencias médicas.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
    with c3:
        render_card("⏰", "ASISTENCIA", "Análisis de puntualidad y horas extras.", "#")

elif "SEGURIDAD" in area_seleccionada:
    st.subheader("🦺 Seguridad y Salud en el Trabajo")
    c1, c2, c3 = st.columns(3)
    with c1:
        render_card("⚠️", "INCIDENTES", "Reporte de accidentabilidad e investigaciones.", "#")
    with c2:
        render_card("🩹", "SST INDICADORES", "Cumplimiento legal y matriz de riesgos.", "#")
    with c3:
        render_card("🏢", "INSPECCIONES", "Hallazgos y planes de acción en sedes.", "#")

elif "DESARROLLO" in area_seleccionada:
    st.subheader("📈 Desarrollo Organizacional")
    c1, c2, c3 = st.columns(3)
    with c1:
        render_card("🎓", "CAPACITACIÓN", "Cumplimiento del plan de formación (PAC).", "#")
    with c2:
        render_card("😊", "CLIMA LABORAL", "Resultados de encuestas y compromiso.", "#")
    with c3:
        render_card("🎯", "DESEMPEÑO", "Evaluación de KPIs y competencias.", "#")

# FOOTER
st.markdown(f"""
    <div style="margin-top: 80px; text-align: center; opacity: 0.5;">
        <p style="font-family: 'Orbitron'; font-size: 0.7rem; letter-spacing: 2px;">
            <span style="color:#1071b8">SISTEMA CONTROL DE GESTIÓN</span> | <span style="color:#c4579b">DON POLLO</span> v2.6
        </p>
    </div>
""", unsafe_allow_html=True)
