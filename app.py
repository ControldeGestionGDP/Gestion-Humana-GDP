import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="📊")

# 2. CREDENCIALES
PASSWORDS = {"nominas": "pollo123", "sst": "seguridad2024", "desarrollo": "talento2024"}

# 3. CSS MINIMALISTA (ESTILO CLEAN TECH)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
        background-color: #ffffff;
    }

    /* Título Sutil */
    .brand-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #0f172a;
        letter-spacing: 1px;
        border-bottom: 2px solid #3b82f6;
        display: inline-block;
        margin-bottom: 2rem;
    }

    /* Botones de Navegación (Menos es más) */
    div.stButton > button {
        background-color: #f8fafc !important;
        color: #475569 !important;
        border: 1px solid #e2e8f0 !important;
        padding: 0.8rem 1.5rem !important;
        border-radius: 8px !important;
        font-weight: 400 !important;
        transition: 0.2s !important;
    }

    div.stButton > button:hover {
        background-color: #3b82f6 !important;
        color: white !important;
        border-color: #3b82f6 !important;
    }

    /* Tarjetas de Reporte (Pequeñas y Limpias) */
    .report-box {
        padding: 1.2rem;
        border-radius: 10px;
        background: #ffffff;
        border: 1px solid #f1f5f9;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        margin-bottom: 10px;
    }
    
    .report-title {
        font-weight: 700;
        color: #1e293b;
        font-size: 1rem;
        margin-bottom: 4px;
    }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE ESTADO
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# =========================================================
# HEADER COMÚN
# =========================================================
st.markdown('<div class="brand-title">DON POLLO | COMMAND CENTER</div>', unsafe_allow_html=True)

# =========================================================
# VISTA 1: MENÚ DE ACCESO RÁPIDO
# =========================================================
if st.session_state.view == 'home':
    st.write("### Panel de Control")
    st.write("Seleccione el área que desea supervisar:")
    
    col1, col2, col3, _ = st.columns([1, 1, 1, 2])
    
    with col1:
        if st.button("💼 NÓMINAS", use_container_width=True):
            st.session_state.view = 'nominas'; st.rerun()
    with col2:
        if st.button("🦺 SEGURIDAD", use_container_width=True):
            st.session_state.view = 'sst'; st.rerun()
    with col3:
        if st.button("📈 DESARROLLO", use_container_width=True):
            st.session_state.view = 'desarrollo'; st.rerun()

# =========================================================
# VISTA 2: LOGIN Y CONTENIDO
# =========================================================
else:
    area = st.session_state.view
    
    # Barra de navegación interna sutil
    nav_col1, nav_col2 = st.columns([1, 5])
    with nav_col1:
        if st.button("← Inicio"):
            st.session_state.view = 'home'; st.session_state.auth = False; st.rerun()
    with nav_col2:
        st.write(f"**Módulo:** {area.upper()}")

    if not st.session_state.auth:
        st.write("---")
        _, col_pw, _ = st.columns([1, 1, 1])
        with col_pw:
            pw = st.text_input("Contraseña de acceso", type="password")
            if st.button("Acceder", use_container_width=True):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True; st.rerun()
                else: st.error("Incorrecto")
    
    else:
        st.write("---")
        # Listado de reportes (Limpio, sin cuadrados gigantes)
        def list_report(name, desc, url):
            col_txt, col_btn = st.columns([4, 1])
            with col_txt:
                st.markdown(f"""
                    <div class="report-box">
                        <div class="report-title">{name}</div>
                        <div style="color:#64748b; font-size:0.85rem;">{desc}</div>
                    </div>
                """, unsafe_allow_html=True)
            with col_btn:
                st.write("") # Alineación sutil
                st.link_button("Abrir", url, use_container_width=True)

        if area == "nominas":
            list_report("🏖️ Vacaciones", "Control de saldos y goce físico.", "https://app.powerbi.com/...")
            list_report("🚑 Descansos Médicos", "Reporte de ausentismo y licencias.", "https://app.powerbi.com/...")
        elif area == "sst":
            list_report("⚠️ Accidentabilidad", "Kpis de seguridad e incidentes.", "#")
        elif area == "desarrollo":
            list_report("🎓 Capacitaciones", "Seguimiento de horas hombre.", "#")

# FOOTER
st.markdown("<br><br><p style='color:#cbd5e1; font-size:0.75rem;'>Intelligence System 2026</p>", unsafe_allow_html=True)
