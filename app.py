import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Security Hub | Don Pollo", layout="wide", page_icon="🔐")

# 2. DEFINICIÓN DE CONTRASEÑAS (Cámbialas aquí)
PASSWORDS = {
    "nominas": "pollo123",
    "sst": "seguridad2024",
    "desarrollo": "talento2024"
}

# 3. ESTILOS ULTRA-FUTURISTAS (CSS)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500;800&display=swap');
    
    .stApp {{ background: radial-gradient(circle at 50% 50%, #ffffff 0%, #e1e8f0 100%); }}

    /* Título Command Center */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem; font-weight: 800; text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 50px;
    }}

    /* Orbes de Gerencia */
    .area-circle {{
        width: 300px; height: 300px; border-radius: 50%;
        background: white; border: 4px solid #1071b8;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        transition: 0.5s all cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 15px 35px rgba(16, 113, 184, 0.1);
        margin: auto;
    }}
    .area-circle:hover {{
        transform: scale(1.1); border-color: #c4579b;
        box-shadow: 0 0 50px rgba(196, 87, 155, 0.3);
    }}

    /* Tarjetas de Dashboard */
    .card {{
        background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px);
        border-radius: 20px; border: 1px solid rgba(16, 113, 184, 0.2);
        padding: 30px; text-align: center; transition: 0.4s; height: 350px;
        display: flex; flex-direction: column; justify-content: center;
    }}
    .card:hover {{ transform: translateY(-10px); border-color: #c4579b; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }}

    /* Botón Lanzar */
    .launch-btn {{
        background: linear-gradient(90deg, #1071b8, #2e3788);
        color: white !important; padding: 10px 20px; border-radius: 50px;
        text-decoration: none !important; font-weight: 700; font-size: 0.8rem;
        text-transform: uppercase; display: inline-block; margin-top: 15px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN Y ESTADOS
if 'view' not in st.session_state:
    st.session_state.view = 'home'
if 'auth' not in st.session_state:
    st.session_state.auth = False

def change_view(target):
    st.session_state.view = target
    st.session_state.auth = False

# =========================================================
# VISTA 1: HOME (SÓLO CÍRCULOS)
# =========================================================
if st.session_state.view == 'home':
    st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="area-circle"><h1 style="font-size:80px;">💼</h1><p style="font-family:Orbitron; color:#2e3788; font-weight:700;">NÓMINAS</p></div>', unsafe_allow_html=True)
        if st.button("ACCEDER A NÓMINAS", use_container_width=True): change_view('nominas')

    with col2:
        st.markdown('<div class="area-circle"><h1 style="font-size:80px;">🦺</h1><p style="font-family:Orbitron; color:#2e3788; font-weight:700;">SEGURIDAD</p></div>', unsafe_allow_html=True)
        if st.button("ACCEDER A SEGURIDAD", use_container_width=True): change_view('sst')

    with col3:
        st.markdown('<div class="area-circle"><h1 style="font-size:80px;">📈</h1><p style="font-family:Orbitron; color:#2e3788; font-weight:700;">DESARROLLO</p></div>', unsafe_allow_html=True)
        if st.button("ACCEDER A DESARROLLO", use_container_width=True): change_view('desarrollo')

# =========================================================
# VISTA 2: AUTENTICACIÓN Y DASHBOARDS
# =========================================================
else:
    # Botón para volver siempre visible en vistas internas
    if st.button("⬅️ VOLVER AL MENÚ PRINCIPAL"):
        st.session_state.view = 'home'
        st.rerun()

    current_area = st.session_state.view
    
    # Verificamos si ya está autenticado
    if not st.session_state.auth:
        st.markdown(f"<h2 style='text-align:center; font-family:Orbitron;'>ACCESO RESTRINGIDO: {current_area.upper()}</h2>", unsafe_allow_html=True)
        
        col_space, col_login, col_space2 = st.columns([1,1,1])
        with col_login:
            password_input = st.text_input("Ingrese Código de Acceso Gerencial", type="password")
            if st.button("VALIDAR CREDENCIALES"):
                if password_input == PASSWORDS[current_area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Código incorrecto. Acceso denegado.")
    
    # Si la contraseña es correcta, mostramos las tarjetas
    else:
        st.success(f"Bienvenido a la Dimensión de {current_area.upper()}")
        
        def render_card(icon, title, desc, link):
            st.markdown(f"""
                <div class="card">
                    <div style="font-size:50px;">{icon}</div>
                    <h3 style="font-family:Orbitron; color:#2e3788;">{title}</h3>
                    <p style="color:#64748b;">{desc}</p>
                    <a href="{link}" target="_blank" class="launch-btn">Abrir Panel</a>
                </div>
            """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        if current_area == "nominas":
            with col1: render_card("🏖️", "VACACIONES", "Saldos y planificación.", "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10")
            with col2: render_card("🚑", "DESCANSOS", "Monitoreo médico.", "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col3: render_card("⏰", "ASISTENCIA", "Horas extra y control.", "#")
            
        elif current_area == "sst":
            with col1: render_card("⚠️", "INCIDENTES", "Tasa de riesgos.", "#")
            with col2: render_card("🩹", "INDICADORES", "Cumplimiento legal.", "#")
            with col3: render_card("🏢", "INSPECCIONES", "Hallazgos sedes.", "#")

        elif current_area == "desarrollo":
            with col1: render_card("🎓", "CAPACITACIÓN", "Avance PAC.", "#")
            with col2: render_card("😊", "CLIMA", "Engagement.", "#")
            with col3: render_card("🎯", "DESEMPEÑO", "Evaluación KPIs.", "#")

# FOOTER
st.markdown("<br><br><p style='text-align:center; color:#94a3b8; font-family:Orbitron; font-size:0.7rem;'>SISTEMA DE SEGURIDAD DE DATOS | DON POLLO 2026</p>", unsafe_allow_html=True)
