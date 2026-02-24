import streamlit as st

# Configuración de página
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="📈")

# =========================================================
# ESTILOS REFINADOS Y CORREGIDOS
# =========================================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');
    * {{ font-family: 'Inter', sans-serif; }}

    .stApp {{ background: #f8fafc; }}

    /* Header */
    .header-container {{
        background: white;
        padding: 40px;
        border-radius: 0 0 50px 50px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        border-bottom: 4px solid #1071b8;
        margin-bottom: 40px;
    }}

    /* Estilo de los Orbes */
    .orbe-card {{
        background: white;
        border-radius: 30px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }}

    .orbe-card:hover {{
        border-color: #c4579b;
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(196, 87, 155, 0.15);
    }}

    .icon-circle {{
        width: 80px;
        height: 80px;
        line-height: 80px;
        background: #f1f5f9;
        border-radius: 50%;
        margin: 0 auto 20px;
        font-size: 40px;
    }}

    /* Títulos y Datos */
    .title-text {{ color: #2e3788; font-weight: 800; font-size: 1.1rem; margin-bottom: 5px; }}
    .data-text {{ color: #1071b8; font-size: 1.5rem; font-weight: 300; margin-bottom: 20px; }}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LÓGICA DE NAVEGACIÓN (ESTADO)
# =========================================================
if 'url_actual' not in st.session_state:
    st.session_state.url_actual = None

# Header
st.markdown("""
    <div class="header-container">
        <h1 style='margin:0; color:#2e3788;'>Intelligence Hub <span style='color:#c4579b;'>Don Pollo</span></h1>
        <p style='color:#64748b;'>Panel de Control de Gestión Estratégica</p>
    </div>
""", unsafe_allow_html=True)

# --- BOTÓN PARA VOLVER ---
if st.session_state.url_actual:
    if st.button("⬅️ Volver al Menú Principal"):
        st.session_state.url_actual = None
        st.rerun()

# =========================================================
# VISTA PRINCIPAL O VISOR DE DASHBOARD
# =========================================================
if st.session_state.url_actual is None:
    
    # KPIs Rápidos
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Cumplimiento", "94%", "Active")
    c2.metric("Headcount", "1,420", "+12")
    c3.metric("Clima", "4.2", "Top")
    c4.metric("SST", "0.02%", "Low")

    st.markdown("### Seleccione una Dimensión para Analizar")
    
    col1, col2, col3 = st.columns(3)

    # CARD 1: VACACIONES
    with col1:
        st.markdown('<div class="orbe-card">', unsafe_allow_html=True)
        st.markdown('<div class="icon-circle">🏖️</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-text">VACACIONES</div>', unsafe_allow_html=True)
        st.markdown('<div class="data-text">Saldo: 92% Planificado</div>', unsafe_allow_html=True)
        if st.button("Ver Dashboard Vacaciones", key="btn_vac"):
            st.session_state.url_actual = "https://app.powerbi.com/view?r=eyJrIjoiMTU4NTVmYmEtNmYyYi00YjVjLTliNzMtZDliY2YyYTM1N2I3IiwidCI6IjQyZmM5NmIzLWMwMTgtNDgyZC04YWRhLWNhYjgxNzIwNDg5ZSIsImMiOjR9" # Versión Publish to Web (Ejemplo)
            # Nota: He usado un link de Power BI público porque el link 'links/...' requiere login y a veces no deja embeber.
            # Si el link es privado, usa el link que me pasaste abajo:
            st.session_state.url_actual = "https://app.powerbi.com/links/1TThJ-ia9c?ctid=42fc96b3-c018-482d-8ada-cab81720489e"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # CARD 2: DESCANSOS MÉDICOS
    with col2:
        st.markdown('<div class="orbe-card">', unsafe_allow_html=True)
        st.markdown('<div class="icon-circle">🚑</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-text">DESCANSOS MÉDICOS</div>', unsafe_allow_html=True)
        st.markdown('<div class="data-text">Monitor de Salud</div>', unsafe_allow_html=True)
        if st.button("Ver Dashboard Descansos", key="btn_dm"):
            st.session_state.url_actual = "https://app.powerbi.com/links/NQfjSntCO1?ctid=42fc96b3-c018-482d-8ada-cab81720489e"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # CARD 3: ASISTENCIA
    with col3:
        st.markdown('<div class="orbe-card">', unsafe_allow_html=True)
        st.markdown('<div class="icon-circle">⏰</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-text">ASISTENCIA</div>', unsafe_allow_html=True)
        st.markdown('<div class="data-text">Puntualidad: 98%</div>', unsafe_allow_html=True)
        if st.button("Próximamente", key="btn_asis", disabled=True):
            pass
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # VISOR DE DASHBOARD (AQUÍ SUCEDE LA MAGIA)
    st.markdown(f"""
        <iframe 
            title="Dashboard Don Pollo" 
            width="100%" 
            height="800" 
            src="{st.session_state.url_actual}" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    """, unsafe_allow_html=True)
    
    # Si el iframe falla (Power BI a veces bloquea el embebido directo por seguridad), 
    # dejamos un botón de emergencia:
    st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <p>¿No carga el reporte? El sistema de seguridad de Power BI requiere login previo.</p>
            <a href="{st.session_state.url_actual}" target="_blank" 
               style="background:#c4579b; color:white; padding:10px 20px; border-radius:10px; text-decoration:none;">
               Abrir en Ventana Nueva
            </a>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br><div style='text-align:center; color:#94a3b8;'>Don Pollo | Control de Gestión 2026</div>", unsafe_allow_html=True)
