import streamlit as st

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Portal Gestión Humana",
    page_icon="📊",
    layout="wide"
)

PASSWORDS = {
    "Administración de Personal": "pollo123",
    "Desarrollo Organizacional": "talento2024",
    "Seguridad y Salud en el Trabajo": "seguridad2024"
}

# =========================================================
# SESSION STATE
# =========================================================
if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False

# =========================================================
# ESTILO SaaS CORPORATIVO
# =========================================================
st.markdown("""
<style>

/* ===== FONDO GENERAL ===== */
.stApp {
    background: linear-gradient(180deg, #f4f7fb 0%, #ffffff 100%);
    font-family: 'Segoe UI', sans-serif;
}

/* ===== TITULOS ===== */
h1, h2, h3 {
    color: #2E3788;
    font-weight: 800;
}

/* ===== TARJETAS PORTAL ===== */
.area-card {
    background: white;
    border-radius: 20px;
    height: 270px;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 20px 45px rgba(0,0,0,0.08);
    border-top: 6px solid #1071B8;
    transition: all 0.25s ease;
}

.area-card:hover {
    transform: translateY(-10px);
    border-top: 6px solid #C4579B;
    box-shadow: 0 30px 65px rgba(0,0,0,0.12);
}

/* ===== ICONOS SVG ===== */
.area-icon {
    width: 64px;
    height: 64px;
}

/* ===== BOTONES GRADIENTE ===== */
.stButton > button {
    background: linear-gradient(90deg, #1071B8, #2E3788);
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: 600;
    padding: 0.6rem 1rem;
    transition: 0.25s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #C4579B, #2E3788);
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

/* ===== LOGIN CARD ===== */
.login-card {
    width: 420px;
    background: white;
    padding: 40px;
    border-radius: 22px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    border-top: 6px solid #1071B8;
    animation: fadeIn 0.6s ease;
}

/* ===== REPORT CARDS ===== */
.report-card {
    background: white;
    border-radius: 18px;
    padding: 25px;
    height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    border-left: 6px solid #1071B8;
    transition: 0.25s;
}

.report-card:hover {
    transform: translateY(-6px);
    border-left: 6px solid #C4579B;
    box-shadow: 0 22px 45px rgba(0,0,0,0.12);
}

/* ===== ANIMACION SUAVE ===== */
@keyframes fadeIn {
    from {opacity:0; transform: translateY(20px);}
    to {opacity:1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# ICONOS SVG
# =========================================================
ICON_PERSONAL = """<svg class="area-icon" viewBox="0 0 24 24" fill="#1071B8"><path d="M12 12c2.7 0 5-2.3 5-5S14.7 2 12 2 7 4.3 7 7s2.3 5 5 5zm0 2c-3.3 0-10 1.7-10 5v3h20v-3c0-3.3-6.7-5-10-5z"/></svg>"""
ICON_DESARROLLO = """<svg class="area-icon" viewBox="0 0 24 24" fill="#1071B8"><path d="M3 17l6-6 4 4 8-8v10H3z"/></svg>"""
ICON_SST = """<svg class="area-icon" viewBox="0 0 24 24" fill="#1071B8"><path d="M12 2l9 4v6c0 5-3.8 9.7-9 10-5.2-.3-9-5-9-10V6l9-4z"/></svg>"""

# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.title("📊 Portal Gestión Humana")
    st.caption("Seleccione una línea de gestión")

    col1, col2, col3 = st.columns(3)

    areas = [
        (ICON_PERSONAL, "Administración de Personal"),
        (ICON_DESARROLLO, "Desarrollo Organizacional"),
        (ICON_SST, "Seguridad y Salud en el Trabajo")
    ]

    for col, (icon, name) in zip([col1, col2, col3], areas):
        with col:

            st.markdown(f"""
            <div class="area-card">
                {icon}
                <div style="font-size:1.3rem;font-weight:700;color:#2E3788;text-align:center;">
                    {name}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Ingresar", key=name):
                st.session_state.area = name
                st.session_state.auth = False
                st.rerun()

# =========================================================
# LOGIN
# =========================================================
else:

    area = st.session_state.area

    if not st.session_state.auth:

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.markdown(f"""
            <div class="login-card">
                <h2 style="text-align:center;">🔐 Acceso Seguro</h2>
                <p style="text-align:center;color:#6b7280;">{area}</p>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("Contraseña", type="password")

            if st.button("Validar acceso", use_container_width=True):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Contraseña incorrecta")

            if st.button("⬅ Volver", use_container_width=True):
                st.session_state.area = None
                st.rerun()

# =========================================================
# CONTENIDO DE ÁREAS
# =========================================================
    else:

        st.title(area)

        if st.button("⬅ Cambiar área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        def report_card(titulo, desc, link):
            st.markdown(f"""
            <div class="report-card">
                <div>
                    <div style="font-weight:700;color:#2E3788">{titulo}</div>
                    <div style="color:#6b7280">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("Abrir reporte", link, use_container_width=True)

        # ADMINISTRACIÓN
        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                report_card("Vacaciones", "Saldo y planificación", "https://app.powerbi.com")

            with col2:
                report_card("Asistencia", "Puntualidad y ausentismo", "https://app.powerbi.com")

            with col3:
                report_card("Legajos", "Repositorio documental", "https://sharepoint.com")

        # DESARROLLO
        elif area == "Desarrollo Organizacional":

            col1, col2 = st.columns(2)

            with col1:
                report_card("Capacitaciones", "Plan anual", "https://app.powerbi.com")

            with col2:
                report_card("Clima Laboral", "Encuestas", "https://app.powerbi.com")

        # SST
        elif area == "Seguridad y Salud en el Trabajo":

            col1, col2 = st.columns(2)

            with col1:
                report_card("Incidentes", "Eventos SST", "https://app.powerbi.com")

            with col2:
                report_card("Bienestar", "Salud ocupacional", "https://app.powerbi.com")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<p style='text-align:center;color:#9ca3af;margin-top:40px;'>Gerencia de Control de Gestión | Transformación Digital</p>",
    unsafe_allow_html=True
)
