import streamlit as st

# =========================================================
# CONFIGURACIÓN
# =========================================================
st.set_page_config(
    page_title="Portal Corporativo | Gestión Humana",
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
# ESTILO MODERNO
# =========================================================
st.markdown("""
<style>

.stApp { background-color: #f4f7fb; }

h1 { color: #2e3788; font-weight: 800; text-align:center; }

.card {
    background: white;
    padding: 2rem;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(0,0,0,0.12);
}

.area-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #2e3788;
}

.footer {
    text-align:center;
    margin-top: 3rem;
    color:#6b7280;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PORTADA — SELECCIÓN DE ÁREAS
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
                <div style="font-size:3rem">{icon}</div>
                <div class="area-title">{name}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Ingresar", key=name):
                st.session_state.area = name
                st.session_state.auth = False
                st.rerun()

# =========================================================
# LOGIN POR ÁREA
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
# CONTENIDO DE CADA ÁREA
# =========================================================
    else:

        st.title(area)

        if st.button("⬅ Cambiar área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        # -------- ADMINISTRACIÓN --------
        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("🏖️ Vacaciones")
                st.write("Uso, saldo y planificación.")
                st.link_button("Abrir reporte", "https://app.powerbi.com")

            with col2:
                st.subheader("⏰ Asistencia")
                st.write("Puntualidad y ausentismo.")
                st.link_button("Abrir reporte", "https://app.powerbi.com")

            with col3:
                st.subheader("📄 Legajos")
                st.write("Repositorio documental.")
                st.link_button("Abrir", "https://sharepoint.com")

        # -------- DESARROLLO --------
        elif area == "Desarrollo Organizacional":

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🎓 Capacitaciones")
                st.link_button("Abrir", "https://app.powerbi.com")

            with col2:
                st.subheader("😊 Clima Laboral")
                st.link_button("Abrir", "https://app.powerbi.com")

        # -------- SST --------
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
