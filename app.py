import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="🔐")

# 2. DEFINICIÓN DE CONTRASEÑAS
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. ESTILOS REFINADOS (FUENTES EMPRESARIALES Y CÍRCULOS CLICKEABLES)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@300;400;600;800&display=swap');
    
    /* Fuente empresarial Inter para todo el cuerpo */
    html, body, [class*="st-"] {{
        font-family: 'Inter', sans-serif !important;
    }}

    .stApp {{ background: radial-gradient(circle at 50% 50%, #ffffff 0%, #e1e8f0 100%); }}

    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem; font-weight: 800; text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 50px;
    }}

    /* Estilo del Orbe Clickeable */
    .area-circle {{
        width: 300px; height: 300px; border-radius: 50%;
        background: white; border: 4px solid #1071b8;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        transition: 0.5s all cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 15px 35px rgba(16, 113, 184, 0.1);
        margin: auto;
        position: relative;
    }}
    .area-circle:hover {{
        transform: scale(1.08); border-color: #c4579b;
        box-shadow: 0 0 50px rgba(196, 87, 155, 0.3);
    }}

    /* Ocultar botones de Streamlit para que parezcan parte del círculo */
    .stButton > button {{
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        height: 300px !important;
        width: 300px !important;
        position: absolute !important;
        top: -300px;
        z-index: 10;
        cursor: pointer;
    }}

    /* Tarjetas de Dashboard */
    .card {{
        background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px);
        border-radius: 20px; border: 1px solid rgba(16, 113, 184, 0.2);
        padding: 30px; text-align: center; transition: 0.4s; height: 350px;
        display: flex; flex-direction: column; justify-content: center;
    }}
    .card:hover {{ transform: translateY(-10px); border-color: #c4579b; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }}

    .launch-btn {{
        background: linear-gradient(90deg, #1071b8, #2e3788);
        color: white !important; padding: 12px 25px; border-radius: 50px;
        text-decoration: none !important; font-weight: 600; font-size: 0.85rem;
        display: inline-block; margin-top: 15px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

def access_area(target):
    st.session_state.view = target
    st.session_state.auth = False

# =========================================================
# VISTA 1: HOME (CÍRCULOS LIMPIOS)
# =========================================================
if st.session_state.view == 'home':
    st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="area-circle"><h1 style="font-size:80px;">💼</h1><p style="font-weight:700; color:#2e3788; letter-spacing:1px;">NÓMINAS</p></div>', unsafe_allow_html=True)
        if st.button("n", key="btn_nom"): access_area('nominas')

    with col2:
        st.markdown('<div class="area-circle"><h1 style="font-size:80px;">🦺</h1><p style="font-weight:700; color:#2e3788; letter-spacing:1px;">SEGURIDAD</p></div>', unsafe_allow_html=True)
        if st.button("s", key="btn_sst"): access_area('sst')

    with col3:
        st.markdown('<div class="area-circle"><h1 style="font-size:80px;">📈</h1><p style="font-weight:700; color:#2e3788; letter-spacing:1px;">DESARROLLO</p></div>', unsafe_allow_html=True)
        if st.button("d", key="btn_des"): access_area('desarrollo')

# =========================================================
# VISTA 2: LOGIN Y DASHBOARDS
# =========================================================
else:
    if st.button("⬅️ VOLVER AL MENÚ"):
        st.session_state.view = 'home'
        st.rerun()

    area = st.session_state.view
    
    if not st.session_state.auth:
        st.markdown(f"<h2 style='text-align:center; font-weight:800; color:#2e3788;'>ACCESO PRIVADO: {area.upper()}</h2>", unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns([1,1,1])
        with col_b:
            pw = st.text_input("Contraseña de Gerencia", type="password")
            if st.button("ENTRAR AL SISTEMA"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Credenciales Inválidas")
    
    else:
        # CONTENIDO DE DASHBOARDS
        def render_card(icon, title, desc, link):
            st.markdown(f"""
                <div class="card">
                    <div style="font-size:50px; margin-bottom:10px;">{icon}</div>
                    <h3 style="color:#2e3788; font-weight:700;">{title}</h3>
                    <p style="color:#64748b; font-size:0.95rem;">{desc}</p>
                    <a href="{link}" target="_blank" class="launch-btn">Lanzar Dashboard</a>
                </div>
            """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        if area == "nominas":
            with col1: render_card("🏖️", "VACACIONES", "Gestión de saldos y planificación.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            with col2: render_card("🚑", "DESCANSOS", "Monitor de salud y ausentismo.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col3: render_card("⏰", "ASISTENCIA", "Control de tiempos y puntualidad.", "#")
        elif area == "sst":
            with col1: render_card("⚠️", "INCIDENTES", "Tasa de accidentabilidad.", "#")
            with col2: render_card("🩹", "INDICADORES", "Cumplimiento legal SST.", "#")
            with col3: render_card("🏢", "INSPECCIONES", "Hallazgos en sedes.", "#")
        elif area == "desarrollo":
            with col1: render_card("🎓", "CAPACITACIÓN", "Cumplimiento del PAC.", "#")
            with col2: render_card("😊", "CLIMA", "Nivel de satisfacción.", "#")
            with col3: render_card("🎯", "DESEMPEÑO", "Métricas de objetivos.", "#")

# FOOTER
st.markdown("<br><br><p style='text-align:center; color:#94a3b8; font-size:0.8rem; font-weight:600;'>GRUPODON POLLO | CONTROL DE GESTIÓN 2026</p>", unsafe_allow_html=True)
