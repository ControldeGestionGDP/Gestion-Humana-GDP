import streamlit as st

# Configuración de página
st.set_page_config(page_title="GH Hub | Don Pollo", layout="wide", page_icon="🌐")

# =========================================================
# EL "WOW FACTOR": CSS PERSONALIZADO (BLANCO FUTURISTA)
# =========================================================
st.markdown("""
<style>
    /* Fondo con gradiente sutil y animado */
    .stApp {
        background: radial-gradient(circle at top right, #f0f4f8, #e5eef5, #ffffff);
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Estilo de los "Círculos de Datos" (Cards Circulares) */
    .dashboard-circle {
        width: 220px;
        height: 220px;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 20px;
        border: 2px solid rgba(16, 113, 184, 0.1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05), inset 0 0 15px rgba(16, 113, 184, 0.05);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        text-decoration: none !important;
        margin: 0 auto;
    }

    .dashboard-circle:hover {
        transform: scale(1.1) rotate(5deg);
        background: white;
        border: 2px solid #c4579b;
        box-shadow: 0 20px 40px rgba(196, 87, 155, 0.2);
    }

    .circle-icon { font-size: 45px; margin-bottom: 10px; }
    .circle-title { color: #2e3788; font-weight: 800; font-size: 16px; margin: 0; }
    .circle-value { color: #1071b8; font-size: 24px; font-weight: 300; }

    /* Header Flotante */
    .main-header {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.5);
        margin-bottom: 40px;
        text-align: center;
    }

    /* Quitar decoraciones de Streamlit */
    div[data-testid="stMetricValue"] > div { font-size: 28px !important; color: #1071b8 !important; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER ESTRATÉGICO
# =========================================================
st.markdown("""
    <div class="main-header">
        <h1 style='margin:0; color:#2e3788; letter-spacing:-1px;'>Intelligence Hub <span style='color:#c4579b;'>Don Pollo</span></h1>
        <p style='color:#6b7280; font-weight:400;'>Arquitectura de Datos para Decisiones de Alta Gerencia</p>
    </div>
""", unsafe_allow_html=True)

# =========================================================
# MÉTRICAS EN TIEMPO REAL (Línea de Vida)
# =========================================================
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Talento Activo", "1,420", "+2.4%")
with m2: st.metric("Eficacia Formación", "92%", "Core")
with m3: st.metric("Índice Clima", "84/100", "Top")
with m4: st.metric("Siniestralidad", "0.02%", "-0.1%")

st.write("---")

# =========================================================
# NAVEGACIÓN POR DIMENSIONES (Círculos Interactivos)
# =========================================================
tabs = st.tabs(["🚀 Operaciones Humana", "💎 Desarrollo & Talento", "🛡️ Salud & Futuro"])

def render_circle(icon, title, value, link):
    return f"""
        <a href="{link}" target="_blank" style="text-decoration: none;">
            <div class="dashboard-circle">
                <div class="circle-icon">{icon}</div>
                <p class="circle-title">{title}</p>
                <div class="circle-value">{value}</div>
                <p style="font-size:10px; color:#aaa; margin-top:5px;">CLICK PARA ABRIR</p>
            </div>
        </a>
    """

with tabs[0]:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(render_circle("🏖️", "VACACIONES", "94% Planificado", "#"), unsafe_allow_html=True)
    with c2: st.markdown(render_circle("⏰", "ASISTENCIA", "98.2% Logrado", "#"), unsafe_allow_html=True)
    with c3: st.markdown(render_circle("📄", "LEGAJOS", "Digitalizado", "#"), unsafe_allow_html=True)

with tabs[1]:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.markdown(render_circle("🎓", "CAPACITACIÓN", "8.2 hrs/mes", "#"), unsafe_allow_html=True)
    with c2: st.markdown(render_circle("😊", "CLIMA", "Nivel A+", "#"), unsafe_allow_html=True)

with tabs[2]:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.markdown(render_circle("⚠️", "RIESGOS", "Nivel Bajo", "#"), unsafe_allow_html=True)
    with c2: st.markdown(render_circle("❤️", "BIENESTAR", "15 Actividades", "#"), unsafe_allow_html=True)

# =========================================================
# SECCIÓN DE ANÁLISIS PREDICTIVO (El toque extra)
# =========================================================
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("🔍 Ver Proyecciones Inteligentes (IA)"):
    col_a, col_b = st.columns(2)
    col_a.info("**Predicción de Rotación:** Se estima una reducción del 5% para el próximo trimestre basada en las últimas encuestas de clima.")
    col_b.warning("**Alerta de Vacaciones:** 3 áreas críticas superan el 20% de saldo acumulado. Se sugiere programar antes de Junio.")

# Footer
st.markdown("""
    <div style="text-align:center; padding:50px; color:#bdc3c7; font-size:12px;">
        GESTIÓN HUMANA | GRUPO DON POLLO | 2026 DIGITAL ECOSYSTEM
    </div>
""", unsafe_allow_html=True)
