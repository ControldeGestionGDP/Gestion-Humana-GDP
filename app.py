# =========================================================
# DASHBOARDS POR ÁREA
# =========================================================
    else:

        st.markdown(f'<div class="main-title">{area}</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

        if st.button("Cambiar área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        # =====================================================
        # ADMINISTRACIÓN DE PERSONAL (3 REALES)
        # =====================================================
        if area == "Administración de Personal":

            col1, col2, col3 = st.columns(3)

            with col1:
                report_card(
                    "Vacaciones",
                    "Saldo y planificación",
                    "https://app.powerbi.com",
                    "assets/Vacaciones.jpg"
                )

            with col2:
                report_card(
                    "Descansos Médicos",
                    "Subsidios y ausencias",
                    "https://app.powerbi.com",
                    "assets/Descansos.jpg"
                )

            with col3:
                report_card(
                    "Exámenes Médicos",
                    "Seguimiento ocupacional",
                    "https://app.powerbi.com",
                    "assets/Examenes.jpg"
                )

        # =====================================================
        # DESARROLLO ORGANIZACIONAL (1 FICTICIO)
        # =====================================================
        elif area == "Desarrollo Organizacional":

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                report_card(
                    "Capacitaciones",
                    "Panel en construcción",
                    "https://app.powerbi.com",
                    "assets/Capacitaciones.jpg"
                )

        # =====================================================
        # SEGURIDAD Y SALUD (1 FICTICIO)
        # =====================================================
        elif area == "Seguridad y Salud en el Trabajo":

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                report_card(
                    "Incidentes SST",
                    "Panel en construcción",
                    "https://app.powerbi.com",
                    "assets/Incidentes.jpg"
                )
