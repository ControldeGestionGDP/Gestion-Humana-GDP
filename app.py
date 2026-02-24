import streamlit as st

# Configuración de página
st.set_page_config(page_title="Command Center | Don Pollo", layout="wide", page_icon="⚡")

# =========================================================
# ESTILOS REFINADOS (CIRCULOS INTERACTIVOS + CARDS)
# =========================================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500;800&display=swap');

    .stApp {{
        background: radial-gradient(circle at 50% 50%, #ffffff 0%, #e1e8f0 100%);
    }}

    /* CONTENEDOR DE CÍRCULOS (GIGANTES) */
    .circle-container {{
        display: flex;
        justify-content: center;
        gap: 50px;
        padding: 50px 0;
    }}

    /* CÍRCULOS DE GERENCIA */
    .area-circle {{
        width: 280px;
        height: 280px;
        border-radius: 50%;
        background: white;
        border: 4px solid #1071b8;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 30px rgba(16, 113, 184, 0.15);
        text-align: center;
        padding: 20px;
    }}

    .area-circle:hover {{
        transform: scale(1.1);
        border-color: #c4579b;
        box-shadow: 0 0 40px rgba(196, 87, 155, 0.4);
    }}

    .circle-icon {{ font-size: 70px; margin-bottom: 10px; }}
    .circle-text {{ 
        font-family: 'Orbitron', sans-serif; 
        color: #2e3788; 
        font-weight: 700; 
        font-size: 0.9rem;
    }}

    /* REUTILIZANDO TU DISEÑO DE TARJETAS */
    .card {{
        position: relative;
        width: 100%;
        height: 380px;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(16, 113, 184, 0.2);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: 0.5s all ease;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}

    .card:hover {{
        transform: translateY(-15px);
        border: 2px solid #c4579b;
        box-shadow: 0 30px 60px rgba(196, 87, 155, 0.2);
    }}

    .icon-box {{ font-size: 50px; margin-bottom: 15px; transition: 0.5s; }}
    .card-title {{ font-family: 'Orbitron', sans-serif; color: #2e3788; font-weight: 700; font-size: 1.1rem; margin-bottom: 10px; text-align: center; }}
    .card-desc {{ color: #64748b; font-size: 0.85rem; text-align: center; padding: 0 15px; margin-bottom: 25px; }}

    .launch-btn {{
        background: linear-gradient(90deg, #1071b8, #2e3788);
        color: white !important;
        padding: 10px 25px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 800;
        font-size: 0.75rem;
        text-transform: uppercase;
        transition: 0.3s;
        box-shadow: 0 10px 20px rgba(46, 55, 136, 0.2);
    }}
    .launch-btn:hover {{ background: #c4579b; box-shadow: 0 0 20px rgba(196, 87, 155, 0.5); }}

    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
</style>
""", unsafe_allow_html=True)

# =========================================================
# LÓGICA DE NAVEGACIÓN
# =========================================================
if 'area' not in st.session_state:
    st.session_state.area = None

def set_area(name):
    st.session_state.area = name

# HEADER
st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#64748b; font-weight:500; margin-bottom:20px;'>DATA INTELLIGENCE | GRUPO DON POLLO</p>", unsafe_allow_html=True)

# =========================================================
# NIVEL 1: LOS 3 CÍRCULOS (GERENCIAS)
# =========================================================
st.write("---")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("💼 NÓMINAS & PERSONAL", use_container_width=True): set_area("nominas")
    st.markdown("""<div class="area-circle"><div class="circle-icon">💼</div><div class="circle-text">NÓMINAS &<br>PERSONAL</div></div>""", unsafe_allow_html=True)

with c2:
    if st.button("🦺 SEGURIDAD & SALUD", use_container_width=True): set_area("sst")
    st.markdown("""<div class="area-circle"><div class="circle-icon">🦺</div><div class="circle-text">SEGURIDAD Y<br>SALUD</div></div>""", unsafe_allow_html=True)

with c3:
    if st.button("📈 DESARROLLO ORG.", use_container_width=True): set_area("desarrollo")
    st.markdown("""<div class="area-circle"><div class="circle-icon">📈</div><div class="circle-text">DESARROLLO<br>ORGANIZACIONAL</div></div>""", unsafe_allow_html=True)

st.write("---")

# =========================================================
# NIVEL 2: LAS TARJETAS (SEGÚN SELECCIÓN)
# =========================================================
def crear_card(icono, titulo, desc, link):
    st.markdown(f"""
        <div class="card">
            <div class="icon-box">{icono}</div>
            <div class="card-title">{titulo}</div>
            <div class="card-desc">{desc}</div>
            <a href="{link}" target="_blank" class="launch-btn">Lanzar Dashboard</a>
        </div>
    """, unsafe_allow_html=True)

if st.session_state.area == "nominas":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#2e3788;'>PANEL NÓMINAS</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: crear_card("🏖️", "VACACIONES", "Control de flujos y saldos.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
    with col2: crear_card("🚑", "DESCANSOS MÉDICOS", "Monitoreo de ausentismo por salud.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
    with col3: crear_card("⏰", "ASISTENCIA", "Métricas de puntualidad y horas extra.", "#")

elif st.session_state.area == "sst":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#2e3788;'>PANEL SEGURIDAD</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: crear_card("⚠️", "INCIDENTES", "Tasa de accidentabilidad.", "#")
    with col2: crear_card("🩹", "INDICADORES SST", "Cumplimiento normativo.", "#")
    with col3: crear_card("🏢", "INSPECCIONES", "Hallazgos en sedes.", "#")

elif st.session_state.area == "desarrollo":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#2e3788;'>PANEL DESARROLLO</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: crear_card("🎓", "CAPACITACIÓN", "Avance de plan anual.", "#")
    with col2: crear_card("😊", "CLIMA", "Nivel de compromiso.", "#")
    with col3: crear_card("🎯", "DESEMPEÑO", "Métricas de KPIs.", "#")

# FOOTER
st.markdown(f"""
    <div style="margin-top: 50px; text-align: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px;">
        <p style="color: #94a3b8; font-family: 'Orbitron'; font-size: 0.7rem; letter-spacing: 3px;">
            PLATAFORMA DE GESTIÓN HUMANA | <span style="color:#c4579b">DON POLLO</span> 2026
        </p>
    </div>
""", unsafe_allow_html=True)
