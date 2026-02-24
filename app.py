import streamlit as st

# Configuración inicial
st.set_page_config(
    page_title="Gestión Humana | Smart Portal",
    page_icon="🚀",
    layout="wide"
)

# =========================================================
# ESTILO FUTURISTA (GLASSMORPHISM & ANIMACIONES)
# =========================================================
st.markdown("""
<style>
/* Fondo general con degradado animado */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #2e3788, #1071b8);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Títulos con neón */
h1 {
    color: #ffffff !important;
    text-shadow: 0 0 10px rgba(16, 113, 184, 0.8);
    font-family: 'Inter', sans-serif;
}

/* Sidebar transparente */
section[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(10px);
}

/* CARDS GLASSMORPHISM */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 20px !important;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(196, 87, 155, 0.5) !important;
    box-shadow: 0 12px 40px 0 rgba(196, 87, 155, 0.2);
}

/* Estilo de Botones tipo 'Cápsula' */
.stButton>button {
    border-radius: 20px;
    background: linear-gradient(90deg, #1071b8, #c4579b);
    color: white;
    border: none;
    transition: 0.3s;
}

/* Texto en blanco para legibilidad */
p, li, label, .stMarkdown {
    color: #e2e8f0 !important;
}

/* Ocultar decoraciones de Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER & KPI RESUMEN
# =========================================================
st.title("🚀 Smart Management Portal")
st.write("Grupo Don Pollo | Intelligence Hub")

# Fila de métricas rápidas (Los "Bolos" que mencionabas)
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric(label="Dotación Total", value="1,250", delta="12%")
kpi2.metric(label="Cumplimiento SST", value="98%", delta="2%")
kpi3.metric(label="Clima Laboral", value="4.2/5", delta="0.5")
kpi4.metric(label="Capacitación", value="85%", delta="-3%")

st.markdown("---")

# =========================================================
# MENÚ LATERAL
# =========================================================
st.sidebar.image("https://via.placeholder.com/150x50/ffffff/1071b8?text=DON+POLLO", width=150)
st.sidebar.markdown("### 🧠 Central de Navegación")
linea = st.sidebar.selectbox(
    "Selecciona una dimensión:",
    ["👥 Administración de Personal", "📈 Desarrollo Organizacional", "🦺 Seguridad y Salud"]
)

# =========================================================
# COMPONENTE DE CARD MEJORADO
# =========================================================
def card_futurista(titulo, icono, desc, link, tech_stack):
    with st.container(border=True):
        col_icon, col_txt = st.columns([1, 4])
        with col_icon:
            st.markdown(f"## {icono}")
        with col_txt:
            st.subheader(titulo)
        
        st.write(desc)
        
        # Tags de tecnología
        tags = ""
        for tech in tech_stack:
            tags += f" `<small>{tech}</small>` "
        st.markdown(tags, unsafe_allow_html=True)
        
        # Link como botón estilizado
        st.markdown(f"""
        <a href="{link}" target="_blank">
            <div style="
                text-align: center;
                padding: 10px;
                background: linear-gradient(90deg, #1071b8, #2e3788);
                border-radius: 10px;
                color: white;
                font-weight: bold;
                margin-top: 15px;
                cursor: pointer;">
                Explorar Dashboard
            </div>
        </a>
        """, unsafe_allow_html=True)

# =========================================================
# LÓGICA DE CONTENIDO
# =========================================================
if "Administración" in linea:
    st.header("👥 Administración de Personal")
    c1, c2, c3 = st.columns(3)
    with c1:
        card_futurista("Vacaciones", "🏖️", "Gestión de saldos y provisión.", "#", ["Power BI", "Real-time"])
    with c2:
        card_futurista("Asistencia", "⏰", "Control de tiempos y ausentismo.", "#", ["Power BI", "Daily"])
    with c3:
        card_futurista("Legajos", "📄", "Expediente digital del colaborador.", "#", ["SharePoint", "Secure"])

elif "Desarrollo" in linea:
    st.header("📈 Desarrollo Organizacional")
    c1, c2 = st.columns(2)
    with c1:
        card_futurista("Capacitación", "🎓", "Avance del Plan Anual.", "#", ["Metrics", "LMS"])
    with c2:
        card_futurista("Clima", "😊", "Engagement y satisfacción.", "#", ["Survey", "Quarterly"])

else:
    st.header("🦺 Seguridad y Salud")
    c1, c2 = st.columns(2)
    with c1:
        card_futurista("Incidentes", "⚠️", "Reporte de seguridad y riesgos.", "#", ["SST", "Critical"])
    with c2:
        card_futurista("Bienestar", "❤️", "Salud física y mental.", "#", ["Salud", "Monthly"])

# Footer futurista
st.markdown("""
<div style="text-align: center; margin-top: 50px; opacity: 0.5;">
    <hr>
    <p>Powered by Control de Gestión | Don Pollo AI Team 2026</p>
</div>
""", unsafe_allow_html=True)
