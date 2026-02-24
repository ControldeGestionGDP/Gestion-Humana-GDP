import streamlit as st

# Configuración de página
st.set_page_config(page_title="GH Hub | Don Pollo", layout="wide", page_icon="⚡")

# =========================================================
# DISEÑO ULTRA-FUTURISTA (CSS CUSTOM)
# =========================================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500;800&display=swap');

    /* Fondo base con profundidad */
    .stApp {{
        background: radial-gradient(circle at 20% 20%, #ffffff 0%, #e1e8f0 100%);
    }}

    /* Estilo del contenedor de tarjetas */
    .dashboard-container {{
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 30px;
        padding: 40px 0;
    }}

    /* LA TARJETA FUTURISTA */
    .card {{
        position: relative;
        width: 320px;
        height: 400px;
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(16, 113, 184, 0.2);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: 0.5s all ease;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    }}

    .card:hover {{
        transform: translateY(-20px);
        border: 2px solid #c4579b;
        box-shadow: 0 30px 60px rgba(196, 87, 155, 0.2);
    }}

    /* El efecto de brillo superior */
    .card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(16, 113, 184, 0.1), transparent);
        pointer-events: none;
    }}

    /* Iconos animados */
    .icon-box {{
        font-size: 60px;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 10px rgba(16, 113, 184, 0.3));
        transition: 0.5s;
    }}
    .card:hover .icon-box {{
        transform: scale(1.2);
        filter: drop-shadow(0 0 20px #c4579b);
    }}

    /* Títulos con fuente tecnológica */
    .card-title {{
        font-family: 'Orbitron', sans-serif;
        color: #2e3788;
        font-weight: 700;
        font-size: 1.2rem;
        letter-spacing: 2px;
        margin-bottom: 10px;
        text-align: center;
    }}

    .card-desc {{
        color: #64748b;
        font-size: 0.9rem;
        text-align: center;
        padding: 0 20px;
        margin-bottom: 30px;
    }}

    /* BOTÓN LINK (El área interactiva real) */
    .launch-btn {{
        background: linear-gradient(90deg, #1071b8, #2e3788);
        color: white !important;
        padding: 12px 35px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 800;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s;
        border: none;
        box-shadow: 0 10px 20px rgba(46, 55, 136, 0.2);
    }}

    .launch-btn:hover {{
        background: #c4579b;
        box-shadow: 0 0 20px rgba(196, 87, 155, 0.5);
    }}

    /* Título Principal */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }}
</style>
""", unsafe_allow_html=True)

# =========================================================
# CONTENIDO
# =========================================================

st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#64748b; font-weight:500; margin-bottom:50px;'>DATA INTELLIGENCE | GRUPO DON POLLO</p>", unsafe_allow_html=True)

# Creamos las columnas para las tarjetas
col1, col2, col3 = st.columns(3)

# FUNCIÓN PARA CREAR TARJETAS
def crear_portal(columna, icono, titulo, descripcion, link):
    with columna:
        st.markdown(f"""
            <div class="card">
                <div class="icon-box">{icono}</div>
                <div class="card-title">{titulo}</div>
                <div class="card-desc">{descripcion}</div>
                <a href="{link}" target="_blank" class="launch-btn">Lanzar Dashboard</a>
            </div>
        """, unsafe_allow_html=True)

# TARJETA 1: VACACIONES
crear_portal(
    col1, "🏖️", "VACACIONES", 
    "Control de flujos, saldos y planificación de descansos del personal.", 
    "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare10"
)

# TARJETA 2: DESCANSOS MÉDICOS
crear_portal(
    col2, "🚑", "DESCANSOS MÉDICOS", 
    "Monitoreo de ausentismo por salud y alertas de seguimiento médico.", 
    "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare"
)

# TARJETA 3: ASISTENCIA (EJEMPLO)
crear_portal(
    col3, "⏰", "ASISTENCIA", 
    "Métricas de puntualidad, horas extra y cumplimiento de turnos.", 
    "#"
)

# SEGUNDA FILA (SI ES NECESARIO)
st.markdown("<br><br>", unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)

crear_portal(
    col4, "🎓", "CAPACITACIÓN", 
    "Estado del plan anual de formación y desarrollo de competencias.", 
    "#"
)

crear_portal(
    col5, "😊", "CLIMA LABORAL", 
    "Resultados de encuestas de satisfacción y cultura organizacional.", 
    "#"
)

crear_portal(
    col6, "🛡️", "SEGURIDAD", 
    "Indicadores de SST, incidentes y cumplimiento normativo.", 
    "#"
)

# FOOTER
st.markdown(f"""
    <div style="margin-top: 100px; text-align: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px;">
        <p style="color: #94a3b8; font-family: 'Orbitron'; font-size: 0.7rem; letter-spacing: 3px;">
            PLATAFORMA DE GESTIÓN HUMANA | <span style="color:#c4579b">DON POLLO</span> 2026
        </p>
    </div>
""", unsafe_allow_html=True)
