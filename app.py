import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="⚡")

# 2. CREDENCIALES (Como pediste)
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. EL "OUTFIT" DE LA WEB (CSS PREMIUM)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@300;400;600;800&display=swap');
    
    /* Fuente Empresarial */
    html, body, [class*="st-"] {{
        font-family: 'Inter', sans-serif !important;
    }}

    /* Fondo Gradiente Suave */
    .stApp {{
        background: radial-gradient(circle at top right, #ffffff, #f0f4f8);
    }}

    /* Título Futurista */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: -50px;
        margin-bottom: 10px;
    }}

    /* EL CÍRCULO INTERACTIVO (Sin botones visibles) */
    .circle-wrapper {{
        position: relative;
        width: 280px;
        height: 280px;
        margin: auto;
    }}

    .area-circle {{
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: white;
        border: 1px solid rgba(16, 113, 184, 0.2);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        cursor: pointer;
    }}

    .circle-wrapper:hover .area-circle {{
        transform: translateY(-15px) scale(1.05);
        border-color: #c4579b;
        box-shadow: 0 20px 50px rgba(196, 87, 155, 0.2);
    }}

    /* Ocultar el botón real de Streamlit encima del círculo */
    .stButton > button {{
        position: absolute;
        top: 0; left: 0;
        width: 280px !important;
        height: 280px !important;
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        z-index: 10;
        cursor: pointer;
    }}
    .stButton > button:hover {{ color: transparent !important; background: transparent !important; }}

    /* Tarjetas de Datos */
    .card {{
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,0.4);
        padding: 40px 25px;
        text-align: center;
        transition: 0.4s;
        height: 360px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }}
    .card:hover {{
        transform: translateY(-10px);
        background: white;
        border-color: #c4579b;
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    }}

    /* Botones de Lanzamiento */
    .launch-btn {{
        background: linear-gradient(135deg, #1071b8, #2e3788);
        color: white !important;
        padding: 12px 28px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-top: 20px;
        transition: 0.3s;
    }}
    .launch-btn:hover {{
        background: #c4579b;
        box-shadow: 0 10px 20px rgba(196, 87, 155, 0.3);
    }}
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

def navigate_to(area):
    st.session_state.view = area
    st.session_state.auth = False

# =========================================================
# VISTA 1: PORTAL DE ENTRADA (MÍNIMO Y ELEGANTE)
# =========================================================
if st.session_state.view == 'home':
    st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; letter-spacing:2px; font-weight:300; margin-bottom:60px;'>INTELIGENCIA DE DATOS | DON POLLO</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="circle-wrapper"><div class="area-circle"><h1 style="font-size:70px; margin:0;">💼</h1><p style="font-weight:700; color:#2e3788; margin-top:10px; letter-spacing:1px;">NÓMINAS</p></div></div>', unsafe_allow_html=True)
        if st.button("nom", key="btn_nom"): navigate_to('nominas')

    with c2:
        st.markdown('<div class="circle-wrapper"><div class="area-circle"><h1 style="font-size:70px; margin:0;">🦺</h1><p style="font-weight:700; color:#2e3788; margin-top:10px; letter-spacing:1px;">SEGURIDAD</p></div></div>', unsafe_allow_html=True)
        if st.button("sst", key="btn_sst"): navigate_to('sst')

    with c3:
        st.markdown('<div class="circle-wrapper"><div class="area-circle"><h1 style="font-size:70px; margin:0;">📈</h1><p style="font-weight:700; color:#2e3788; margin-top:10px; letter-spacing:1px;">DESARROLLO</p></div></div>', unsafe_allow_html=True)
        if st.button("dev", key="btn_dev"): navigate_to('desarrollo')

# =========================================================
# VISTA 2: ACCESO Y DASHBOARDS
# =========================================================
else:
    col_back, _ = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ INICIO"):
            st.session_state.view = 'home'
            st.rerun()

    area = st.session_state.view
    
    if not st.session_state.auth:
        st.markdown(f"<h2 style='text-align:center; font-weight:800; color:#2e3788; margin-top:40px;'>🔐 ACCESO RESTRINGIDO</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; color:#64748b;'>Área: {area.upper()}</p>", unsafe_allow_html=True)
        
        col_x, col_login, col_z = st.columns([1.2, 1, 1.2])
        with col_login:
            st.markdown("<br>", unsafe_allow_html=True)
            pw = st.text_input("Clave de Seguridad", type="password", help="Solo personal autorizado")
            if st.button("AUTENTICAR"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Clave incorrecta")
    
    else:
        st.markdown(f"<h2 style='font-weight:800; color:#2e3788;'>Gestión de {area.upper()}</h2>", unsafe_allow_html=True)
        st.write("---")
        
        def render_card(icon, title, desc, link):
            st.markdown(f"""
                <div class="card">
                    <div style="font-size:55px; margin-bottom:15px;">{icon}</div>
                    <h3 style="color:#2e3788; font-weight:800; margin:0;">{title}</h3>
                    <p style="color:#64748b; font-size:0.95rem; margin-top:15px;">{desc}</p>
                    <a href="{link}" target="_blank" class="launch-btn">VER REPORTE BI</a>
                </div>
            """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        if area == "nominas":
            with c1: render_card("🏖️", "VACACIONES", "Análisis de saldos, programación y flujos de descanso.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            with c2: render_card("🚑", "DESCANSOS", "Trazabilidad de licencias médicas y ausentismo.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with c3: render_card("⏰", "ASISTENCIA", "Monitor de puntualidad y cumplimiento de turnos.", "#")
        elif area == "sst":
            with c1: render_card("⚠️", "ACCIDENTABILIDAD", "Reporte de incidentes y actos inseguros.", "#")
            with c2: render_card("🩹", "SST CORE", "Indicadores de cumplimiento normativo legal.", "#")
            with c3: render_card("🏢", "AUDITORÍAS", "Inspecciones de seguridad en plantas y oficinas.", "#")
        elif area == "desarrollo":
            with c1: render_card("🎓", "FORMACIÓN", "Avance del Plan Anual de Capacitación.", "#")
            with col2: render_card("😊", "CULTURA", "Medición de clima y compromiso organizacional.", "#")
            with col3: render_card("🎯", "KPIS", "Evaluación de desempeño y objetivos.", "#")

# FOOTER
st.markdown(f"""
    <div style="margin-top: 80px; text-align: center; border-top: 1px solid #eef2f6; padding-top: 30px;">
        <p style="color: #94a3b8; font-size: 0.8rem; font-weight: 500; letter-spacing: 1px;">
            GRUPO <span style="color:#1071b8">DON POLLO</span> | UNIDAD DE INTELIGENCIA ESTRATÉGICA © 2026
        </p>
    </div>
""", unsafe_allow_html=True)
