import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portal de Gestión Humana",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Portal de Transformación Digital – Gestión Humana")
st.markdown(
    "Repositorio central de desarrollos, reportes y aplicaciones por línea de Gestión Humana."
)

# Menú lateral
linea = st.sidebar.selectbox(
    "Selecciona una línea",
    [
        "Administración de Personal",
        "Desarrollo Organizacional",
        "Seguridad y Salud en el Trabajo"
    ]
)

# -----------------------------
# ADMINISTRACIÓN DE PERSONAL
# -----------------------------
if linea == "Administración de Personal":
    st.header("👥 Administración de Personal")
    st.write(
        "Dashboards y aplicaciones para el control y seguimiento del personal."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🏖️ Vacaciones")
        st.markdown("[🔗 Ver reporte Power BI](https://tu-link-powerbi.com)")

    with col2:
        st.subheader("⏰ Asistencia")
        st.markdown("[🔗 Ver reporte Power BI](https://tu-link-powerbi.com)")

    with col3:
        st.subheader("📄 Legajos Digitales")
        st.markdown("[🔗 Ver repositorio](https://github.com/tu-repo)")

# -----------------------------
# DESARROLLO ORGANIZACIONAL
# -----------------------------
elif linea == "Desarrollo Organizacional":
    st.header("📈 Desarrollo Organizacional")
    st.write(
        "Indicadores de desempeño, capacitación y clima laboral."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎓 Capacitación")
        st.markdown("[🔗 Ver dashboard](https://tu-link-powerbi.com)")

    with col2:
        st.subheader("😊 Clima Laboral")
        st.markdown("[🔗 Ver resultados](https://tu-link-powerbi.com)")

# -----------------------------
# SEGURIDAD Y SALUD EN EL TRABAJO
# -----------------------------
elif linea == "Seguridad y Salud en el Trabajo":
    st.header("🦺 Seguridad y Salud en el Trabajo")
    st.write(
        "Seguimiento de incidentes, riesgos y bienestar."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚠️ Incidentes")
        st.markdown("[🔗 Ver dashboard](https://tu-link-powerbi.com)")

    with col2:
        st.subheader("❤️ Bienestar")
        st.markdown("[🔗 Ver app](https://tu-app-streamlit.com)")

# Footer
st.markdown("---")
st.caption("Gestión Humana | Transformación Digital")
