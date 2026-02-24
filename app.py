import streamlit as st

# 1. CONFIGURACIÓN GENERAL
st.set_page_config(
    page_title="Executive BI | Grupo Don Pollo",
    page_icon="📊",
    layout="wide"
)

# 2. SISTEMA DE SEGURIDAD (Las llaves del reino)
PASSWORDS = {
    "👥 Administración de Personal": "pollo123",
    "📈 Desarrollo Organizacional": "talento2024",
    "🦺 Seguridad y Salud en el Trabajo": "seguridad2024"
}

# 3. ESTILO FUTURISTA REFINADO (Glassmorphism & Soft Tech)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Fondo con gradiente sutil */
    .stApp {
        background: radial-gradient(at 0% 0%, rgba(16, 113, 184, 0.05) 0, transparent 50%),
                    radial-gradient(at 100% 100%, rgba(196, 87, 155, 0.05) 0, transparent 50%);
        background-color: #f8fafc;
    }

    /* SIDEBAR TECH */
    section[data-testid="stSidebar"] {
        background: #0f172a !important;
    }
    section[data-testid="stSidebar"] * {
        color: #f1f5f9 !important;
    }

    /* TARJETAS INTERACTIVAS (GLASS) */
    .tech-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.8);
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        margin-bottom: 1.5rem;
        transition: all 0.4s ease;
    }
    .tech-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(16, 113, 184, 0.1);
        border-color: #1071b8;
    }

    /* TÍTULO CORPORATIVO */
    .main-title {
        font-weight: 800;
        background: linear-gradient(90deg, #1071b8, #2e3788);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        margin-bottom: 0;
    }

    /* BOTONES ACCIÓN */
    div.stButton > button {
        border-radius: 12px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        background: #0f172a !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background: #1071b8 !important;
        box-shadow: 0 8px 15px rgba(16, 113, 184, 0.3) !important;
    }

    /* INFO TÉCNICA EXPANDER */
    .stExpander {
        border: none !important;
        background: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# 4. ENCABEZADO
col_h1, col_h2 = st.columns([2,1])
with col_h1:
    st.markdown('<h1 class="main-title">DON POLLO | BI UNIT</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:1rem;'>Plataforma de Inteligencia y Control de Gestión Humana</p>", unsafe_allow_html=True)

# 5. MENÚ LATERAL (Limpiamos el Radio para que sea el disparador)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1789/1789313.png", width=80) # Icono decorativo
st.sidebar.markdown("### PANEL DE CONTROL")
linea = st.sidebar.radio(
    "Seleccione Área de Gestión:",
    ["👥 Administración de Personal", "📈 Desarrollo Organizacional", "🦺 Seguridad y Salud en el Trabajo"]
)

# Reset de autenticación si cambia de línea
if 'current_line' not in st.session_state:
    st.session_state.current_line = linea
    st.session_state.authenticated = False

if st.session_state.current_line != linea:
    st.session_state.current_line = linea
    st.session_state.authenticated = False

# 6. LÓGICA DE ACCESO SEGURO
if not st.session_state.authenticated:
    st.markdown("---")
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        st.markdown(f"### Acceso Protegido\nÁrea: **{linea}**")
        pw = st.text_input("Ingrese Clave Gerencial", type="password")
        if st.button("DESBLOQUEAR INDICADORES"):
            if pw == PASSWORDS[linea]:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Credencial incorrecta")
else:
    # SI ESTÁ AUTENTICADO, MOSTRAR CONTENIDO
    st.markdown(f"### 🚀 {linea}")
    
    # --- FUNCIÓN PARA RENDERIZAR CARDS FUTURISTAS ---
    def render_tech_card(titulo, desc, link, tech_info):
        st.markdown(f"""
            <div class="tech-card">
                <h3 style="margin-top:0; color:#0f172a; font-size:1.3rem;">{titulo}</h3>
                <p style="color:#64748b; font-size:0.9rem;">{desc}</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"ABRIR DASHBOARD", link, use_container_width=True)
        with st.expander("⚙️ Especificaciones Técnicas"):
            for item in tech_info:
                st.markdown(f"• {item}")
        st.write(" ")

    # CONTENIDO SEGÚN LÍNEA
    if linea == "👥 Administración de Personal":
        c1, c2, c3 = st.columns(3)
        with c1:
            render_tech_card("🏖️ Vacaciones", "Control de saldos y planificación operativa.", 
                             "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare",
                             ["Fuente: SAP/Planillas", "Carga: Automática", "Frecuencia: Diaria"])
        with c2:
            render_tech_card("⏰ Asistencia", "Análisis de puntualidad y ausentismo.", "#",
                             ["Fuente: Reloj Biométrico", "Carga: Cloud", "Frecuencia: Tiempo Real"])
        with c3:
            render_tech_card("📁 Legajos Digitales", "Gestión documental centralizada.", "#",
                             ["Plataforma: SharePoint", "Seguridad: AES-256"])

    elif linea == "📈 Desarrollo Organizacional":
        c1, c2 = st.columns(2)
        with c1:
            render_tech_card("🎓 Capacitaciones", "Cumplimiento del Plan Anual.", "#",
                             ["KPI: Horas/Hombre", "Avance: Trimestral"])
        with c2:
            render_tech_card("😊 Clima Laboral", "Resultados de encuestas internas.", "#",
                             ["Metodología: eNPS", "Frecuencia: Semestral"])

    elif linea == "🦺 Seguridad y Salud en el Trabajo":
        c1, c2 = st.columns(2)
        with c1:
            render_tech_card("⚠️ Accidentabilidad", "Registro de incidentes y actos inseguros.", "#",
                             ["Índice: IF / IG", "Carga: Manual Validada"])
        with c2:
            render_tech_card("❤️ Bienestar", "Salud ocupacional y monitoreo preventivo.", "#",
                             ["Fuente: Tópico / SST", "Frecuencia: Mensual"])

# 7. FOOTER
st.markdown("---")
st.markdown("<div style='text-align:center; color:#94a3b8; font-size:0.8rem;'>GERENCIA DE CONTROL DE GESTIÓN | TRANSFORMACIÓN DIGITAL DON POLLO 2026</div>", unsafe_allow_html=True)
