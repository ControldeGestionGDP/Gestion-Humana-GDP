import streamlit as st

# =========================================================
# CONFIG
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
# ESTILO EJECUTIVO
# =========================================================
st.markdown("""
<style>

/* ===== FONDO ===== */
.stApp {
    background: linear-gradient(180deg, #f5f7fb 0%, #ffffff 100%);
    font-family: 'Segoe UI', sans-serif;
}

/* ===== TITULOS ===== */
h1, h2, h3 {
    color: #2E3788;
    font-weight: 800;
}

/* ===== TARJETAS PRINCIPALES ===== */
.area-card {
    background: white;
    border-radius: 18px;
    height: 240px;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    box-shadow: 0 18px 40px rgba(0,0,0,0.08);
    border-top: 6px solid #1071B8;
    transition: all 0.25s ease;
}

.area-card:hover {
    transform: translateY(-8px);
    border-top: 6px solid #C4579B;
    box-shadow: 0 28px 60px rgba(0,0,0,0.12);
}

/* Línea decorativa superior */
.area-accent {
    height: 4px;
    background: linear-gradient(90deg,#1071B8,#2E3788,#C4579B);
    border-radius: 2px;
    margin-bottom: 1.5rem;
}

/* ===== BOTONES ===== */
.stButton > button {
    background: linear-gradient(90deg, #1071B8, #2E3788);
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
    transition: 0.25s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #C4579B, #2E3788);
    transform: translateY(-1px);
}

/* ===== LOGIN ===== */
.login-box {
    background: white;
    padding: 38px;
    border-radius: 18px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.12);
    border-top: 5px solid #1071B8;
    animation: fadeIn 0.5s ease;
}

/* ===== REPORT CARDS ===== */
.report-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    height: 210px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    border-left: 5px solid #1071B8;
    transition: 0.25s;
}

.report-card:hover {
    transform: translateY(-6px);
    border-left: 5px solid #C4579B;
    box-shadow: 0 22px 48px rgba(0,0,0,0.12);
}

/* ===== ANIMACIÓN ===== */
@keyframes fadeIn {
    from {opacity:0; transform: translateY(15px);}
    to {opacity:1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.title("Portal Gestión Humana")
    st.caption("Seleccione una línea de gestión")

    col1, col2, col3 = st.columns(3)

    areas = [
        "Administración de Personal",
        "Desarrollo Organizacional",
        "Seguridad y Salud en el Trabajo"
    ]

    for col, name in zip([col1, col2, col3], areas):
        with col:

            st.markdown(f"""
            <div class="area-card">
                <div class="area-accent"></div>
                <div style="font-size:1.25rem;font-weight:700;color:#2E3788;">
                    {name}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Ingresar", key=name):
                st.session_state.area = name
                st.session_state.auth = False
                st.rerun()

# =========================================================
# LOGIN ELEGANTE
# =========================================================
else:

    area = st.session_state.area

    if not st.session_state.auth:

        col1, col2, col3 = st.columns([1,2,1])

        with col2:

            st.markdown(f"""
            <div class="login-box">
                <div style="font-size:1.3rem;font-weight:700;color:#2E3788;text-align:center;">
                    {area}
                </div>
                <div style="text-align:center;color:#6b7280;margin-bottom:20px;">
                    Ingrese su contraseña
                </div>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("", type="password")

            if st.button("Ingresar", use_container_width=True):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Contraseña incorrecta")

            if st.button("Volver", use_container_width=True):
                st.session_state.area = None
                st.rerun()

# =========================================================
# DASHBOARDS POR ÁREA
# =========================================================
    else:

        st.title(area)

        if st.button("Cambiar área"):
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

        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                report_card("Vacaciones", "Saldo y planificación", "https://app.powerbi.com")

            with col2:
                report_card("Asistencia", "Puntualidad y ausentismo", "https://app.powerbi.com")

            with col3:
                report_card("Legajos Digitales", "Repositorio documental", "https://sharepoint.com")

        elif area == "Desarrollo Organizacional":

            col1, col2 = st.columns(2)

            with col1:
                report_card("Capacitaciones", "Plan anual", "https://app.powerbi.com")

            with col2:
                report_card("Clima Laboral", "Encuestas", "https://app.powerbi.com")

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
