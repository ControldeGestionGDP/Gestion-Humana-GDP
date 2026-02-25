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
# ESTADO
# =========================================================
if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False

# =========================================================
# ESTILO CORPORATIVO PRO
# =========================================================
st.markdown("""
<style>

.stApp {
    background-color: #f4f7fb;
}

/* TITULO */
h1 {
    color: #2E3788;
    font-weight: 800;
    text-align: center;
}

/* CARD IGUAL PARA TODOS */
.card {
    background: white;
    border-radius: 18px;
    height: 260px;
    padding: 2rem 1.5rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    border-top: 6px solid #1071B8;
    transition: 0.25s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 22px 45px rgba(0,0,0,0.12);
    border-top: 6px solid #C4579B;
}

/* ICONO */
.icon {
    font-size: 3.2rem;
}

/* TITULO AREA */
.area-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #2E3788;
    text-align: center;
}

/* FOOTER */
.footer {
    text-align:center;
    margin-top: 3rem;
    color:#6b7280;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.title("📊 Portal Gestión Humana")
    st.caption("Seleccione una línea de gestión")

    col1, col2, col3 = st.columns(3)

    areas = [
        ("👥", "Administración de Personal"),
        ("📈", "Desarrollo Organizacional"),
        ("🦺", "Seguridad y Salud en el Trabajo")
    ]

    for col, (icon, name) in zip([col1, col2, col3], areas):
        with col:

            st.markdown(f"""
            <div class="card">
                <div class="icon">{icon}</div>
                <div class="area-title">{name}</div>
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

        st.title(f"🔐 Acceso — {area}")

        pwd = st.text_input("Ingrese contraseña", type="password")

        if st.button("Validar acceso"):
            if pwd == PASSWORDS[area]:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

        if st.button("⬅ Volver"):
            st.session_state.area = None
            st.rerun()

# =========================================================
# CONTENIDO
# =========================================================
    else:

        st.title(area)

        if st.button("⬅ Cambiar área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("🏖️ Vacaciones")
                st.link_button("Abrir reporte", "https://app.powerbi.com")

            with col2:
                st.subheader("⏰ Asistencia")
                st.link_button("Abrir reporte", "https://app.powerbi.com")

            with col3:
                st.subheader("📄 Legajos")
                st.link_button("Abrir", "https://sharepoint.com")

        elif area == "Desarrollo Organizacional":

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🎓 Capacitaciones")
                st.link_button("Abrir", "https://app.powerbi.com")

            with col2:
                st.subheader("😊 Clima Laboral")
                st.link_button("Abrir", "https://app.powerbi.com")

        elif area == "Seguridad y Salud en el Trabajo":

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("⚠️ Incidentes")
                st.link_button("Abrir", "https://app.powerbi.com")

            with col2:
                st.subheader("❤️ Bienestar")
                st.link_button("Abrir", "https://app.powerbi.com")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<div class='footer'>Gerencia de Control de Gestión | Transformación Digital</div>",
    unsafe_allow_html=True
)
