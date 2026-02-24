import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="📈")

# 2. CREDENCIALES
PASSWORDS = {"nominas": "pollo123", "sst": "seguridad2024", "desarrollo": "talento2024"}

# 3. CSS "AVÍCOLA FUTURISTA" (Elegante y Fluido)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&family=Outfit:wght@300;600&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif !important;
    }

    .stApp {
        background: radial-gradient(circle at top right, #f8fafc, #e2e8f0);
    }

    /* HEADER ESTILO GLASS-TECH */
    .header-tech {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 1.5rem 2.5rem;
        border: 1px solid rgba(255, 255, 255, 0.6);
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 3rem;
    }

    .brand-text {
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 1.8rem;
        background: linear-gradient(135deg, #0f172a 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }

    /* TARJETAS FLUIDAS (GLASSMORPHISM) */
    .tech-card {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(12px);
        border-radius: 30px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.7);
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
        text-align: center;
    }
    
    .tech-card:hover {
        transform: translateY(-10px) scale(1.02);
        background: rgba(255, 255, 255, 0.9);
        border-color: #3b82f6;
        box-shadow: 0 30px 60px rgba(59, 130, 246, 0.15);
    }

    /* BOTONES MODERNOS REDONDEADOS */
    div.stButton > button {
        border-radius: 50px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
        color: white !important;
        border: none !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
        text-transform: uppercase;
        font-size: 0.8rem !important;
        letter-spacing: 1px !important;
    }

    div.stButton > button:hover {
        transform: scale(1.05) !important;
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4) !important;
    }

    /* INDICADOR DE REPORTE */
    .report-pill {
        background: white;
        padding: 1rem 1.5rem;
        border-radius: 20px;
        border-left: 6px solid #3b82f6;
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
</style>
""", unsafe_allow_html=True)

# 4. NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# HEADER CORPORATIVO TECH-ELEGANT
st.markdown("""
    <div class="header-tech">
        <div>
            <div class="brand-text">DON POLLO <span style="font-weight:300; opacity:0.6;">CORE</span></div>
            <div style="font-size:0.7rem; color:#64748b; letter-spacing:3px; margin-top:5px;">INTELIGENCIA OPERATIVA</div>
        </div>
        <div style="text-align:right;">
            <div style="background:#e0f2fe; color:#0369a1; padding:4px 12px; border-radius:20px; font-size:0.7rem; font-weight:700;">
                SISTEMA ACTIVO v2.4
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# =========================================================
# VISTA 1: HOME
# =========================================================
if st.session_state.view == 'home':
    st.markdown("<h4 style='text-align:center; color:#1e293b; font-weight:300; margin-bottom:2rem;'>Seleccione una división estratégica</h4>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="tech-card"><h2>💼</h2><h3 style="color:#0f172a;">Nóminas</h3><p style="color:#64748b; font-size:0.85rem;">Gestión de capital humano y flujos de asistencia.</p></div>', unsafe_allow_html=True)
        if st.button("ACCEDER NODO", key="btn_nom"):
            st.session_state.view = 'nominas'; st.rerun()

    with col2:
        st.markdown('<div class="tech-card"><h2>🦺</h2><h3 style="color:#0f172a;">Seguridad</h3><p style="color:#64748b; font-size:0.85rem;">Monitoreo de riesgos y cumplimiento industrial.</p></div>', unsafe_allow_html=True)
        if st.button("ACCEDER NODO", key="btn_sst"):
            st.session_state.view = 'sst'; st.rerun()

    with col3:
        st.markdown('<div class="tech-card"><h2>📈</h2><h3 style="color:#0f172a;">Desarrollo</h3><p style="color:#64748b; font-size:0.85rem;">Indicadores de crecimiento y KPIs de talento.</p></div>', unsafe_allow_html=True)
        if st.button("ACCEDER NODO", key="btn_dev"):
            st.session_state.view = 'desarrollo'; st.rerun()

# =========================================================
# VISTA 2: REPORTES
# =========================================================
else:
    area = st.session_state.view
    c_back, c_title = st.columns([1, 4])
    with c_back:
        if st.button("⬅ VOLVER"):
            st.session_state.view = 'home'; st.session_state.auth = False; st.rerun()
    with c_title:
        st.markdown(f"<h3 style='margin:0;'>División {area.capitalize()}</h3>", unsafe_allow_html=True)

    if not st.session_state.auth:
        st.markdown("<br><br>", unsafe_allow_html=True)
        _, col_login, _ = st.columns([1, 0.8, 1])
        with col_login:
            pw = st.text_input("PASSWORD GERENCIAL", type="password")
            if st.button("DESBLOQUEAR ACCESO", use_container_width=True):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True; st.rerun()
                else: st.error("Clave Incorrecta")
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        def render_report(title, link):
            st.markdown(f"""<div class="report-pill">
                <span style="font-weight:600; color:#1e293b;">{title}</span>
                <span style="color:#3b82f6; font-size:0.7rem;">READY TO VIEW</span>
            </div>""", unsafe_allow_html=True)
            st.link_button(f"ABRIR {title.upper()}", link, use_container_width=True)
            st.write("")

        if area == "nominas":
            render_report("Control Vacaciones", "https://app.powerbi.com/...")
            render_report("Descansos Médicos", "https://app.powerbi.com/...")
        elif area == "sst":
            render_report("Reporte Accidentabilidad", "#")

# FOOTER
st.markdown("<div style='margin-top:100px; text-align:center; color:#cbd5e1; font-size:0.7rem; letter-spacing:2px;'>DON POLLO GROUP | BUSINESS INTELLIGENCE UNIT</div>", unsafe_allow_html=True)
