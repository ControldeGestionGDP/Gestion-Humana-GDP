import streamlit as st

# Configuración de página con estilo Wide
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="📈")

# =========================================================
# DISEÑO DE ALTO IMPACTO (CSS AVANZADO)
# =========================================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');

    * {{ font-family: 'Inter', sans-serif; }}

    /* Fondo de alto contraste sofisticado */
    .stApp {{
        background: radial-gradient(circle at 50% 50%, #ffffff 0%, #f0f2f6 100%);
    }}

    /* Header Estilo Glassmorphism Pro */
    .header-container {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 30px;
        border: 1px solid rgba(46, 55, 136, 0.1);
        box-shadow: 0 20px 50px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 40px;
    }}

    /* EL ORBE (Círculo Futurista) */
    .orbe-nav {{
        width: 240px;
        height: 240px;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        margin: 20px auto;
        position: relative;
        background: white;
        border: 2px solid #1071b8;
        box-shadow: 0 10px 30px rgba(16, 113, 184, 0.1);
        transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
        cursor: pointer;
        overflow: hidden;
    }}

    .orbe-nav:hover {{
        transform: translateY(-15px) scale(1.05);
        border-color: #c4579b;
        box-shadow: 0 30px 60px rgba(196, 87, 155, 0.3);
    }}

    /* Efecto de anillo de luz */
    .orbe-nav::after {{
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 2px solid transparent;
        border-top-color: #c4579b;
        border-bottom-color: #2e3788;
        animation: rotate 4s linear infinite;
        opacity: 0;
        transition: 0.5s;
    }}

    .orbe-nav:hover::after {{ opacity: 1; }}

    @keyframes rotate {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}

    .icon-style {{ font-size: 50px; margin-bottom: 10px; }}
    .title-style {{ color: #2e3788; font-weight: 800; font-size: 18px; letter-spacing: 1px; }}
    .value-style {{ color: #1071b8; font-size: 26px; font-weight: 300; }}

    /* Botones de acción */
    .btn-portal {{
        background: linear-gradient(135deg, #1071b8 0%, #2e3788 100%);
        color: white !important;
        padding: 12px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin-top: 15px;
        transition: 0.3s;
        box-shadow: 0 10px 20px rgba(46, 55, 136, 0.3);
    }}
    .btn-portal:hover {{
        background: #c4579b;
        box-shadow: 0 10px 20px rgba(196, 87, 155, 0.4);
        transform: scale(1.05);
    }}
</style>
""", unsafe_allow_html=True)

# =========================================================
# CONTENIDO PRINCIPAL
# =========================================================

# Header
st.markdown("""
    <div class="header-container">
        <h1 style='margin:0; color:#2e3788; font-size: 3rem;'>Control de Gestión <span style='color:#c4579b;'>360°</span></h1>
        <p style='color:#1071b8; font-size: 1.2rem; font-weight: 300;'>Ecosistema de Analítica Avanzada - Grupo Don Pollo</p>
    </div>
""", unsafe_allow_html=True)

# Tabs con estilo limpio
tab_admin, tab_desarrollo, tab_sst = st.tabs(["📊 ADMINISTRACIÓN", "🚀 DESARROLLO", "🛡️ SEGURIDAD"])

def crear_orbe(id_key, icono, titulo, dato, url):
    """Genera el orbe interactivo con link directo"""
    st.markdown(f"""
        <div class="orbe-nav">
            <div class="icon-style">{icono}</div>
            <div class="title-style">{titulo}</div>
            <div class="value-style">{dato}</div>
            <a href="{url}" target="_blank" class="btn-portal">Abrir Dashboard</a>
        </div>
    """, unsafe_allow_html=True)

# --- TAB ADMINISTRACIÓN ---
with tab_admin:
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        crear_orbe(
            "vac", "🏖️", "VACACIONES", "Disponibilidad 92%", 
            "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10"
        )
    
    with col2:
        crear_orbe(
            "dm", "🚑", "DESCANSOS MÉDICOS", "Monitor de Salud", 
            "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare"
        )
        
    with col3:
        crear_orbe(
            "asis", "⏰", "ASISTENCIA", "98% Puntualidad", 
            "#"
        )

# --- TAB DESARROLLO ---
with tab_desarrollo:
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        crear_orbe("cap", "🎓", "CAPACITACIÓN", "Meta: 100%", "#")
    with col2:
        crear_orbe("clima", "😊", "CLIMA LABORAL", "Score: 4.5/5", "#")

# --- TAB SEGURIDAD ---
with tab_sst:
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        crear_orbe("inc", "⚠️", "INCIDENTES", "Tasa: 0.0%", "#")
    with col2:
        crear_orbe("bien", "❤️", "BIENESTAR", "Activo", "#")

# =========================================================
# PANEL DE INSIGHTS (INTELIGENCIA ARTIFICIAL)
# =========================================================
st.markdown("<br><br>", unsafe_allow_html=True)
with st.container():
    st.markdown(f"""
        <div style="background: linear-gradient(90deg, #2e3788 0%, #1071b8 100%); padding: 30px; border-radius: 20px; color: white;">
            <h3 style="margin:0;">🔍 Insights Estratégicos (IA Predictiva)</h3>
            <p style="opacity:0.8;">Análisis generado automáticamente para la toma de decisiones.</p>
            <div style="display: flex; gap: 20px; margin-top: 15px;">
                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; flex: 1;">
                    <strong>Tendencia Vacaciones:</strong> El 15% del personal de planta tiene saldos > 30 días. Riesgo de acumulación legal alto.
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; flex: 1;">
                    <strong>Salud Laboral:</strong> Los descansos médicos por temas respiratorios subieron 2% este mes. Sugerido: Reforzar EPP.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer con logo o texto corporativo
st.markdown("""
    <div style="text-align: center; margin-top: 60px; color: #bdc3c7; font-weight: 300;">
        GRUPO DON POLLO | GERENCIA DE CONTROL DE GESTIÓN | v2.0 - 2026
    </div>
""", unsafe_allow_html=True)
