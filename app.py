import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Executive Hub | Don Pollo", layout="wide", page_icon="⚡")

# 2. CREDENCIALES
PASSWORDS = {"nominas": "pollo123", "sst": "seguridad2024", "desarrollo": "talento2024"}

# 3. CSS PARA EL DISEÑO PREMIUM
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;800&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif !important; }
    .stApp { background: radial-gradient(circle at top right, #ffffff, #f0f4f8); }
    
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem; font-weight: 800; text-align: center;
        background: linear-gradient(90deg, #1071b8, #2e3788, #c4579b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 50px;
    }
</style>
""", unsafe_allow_html=True)

# 4. FUNCIÓN MAESTRA: EL CÍRCULO QUE SÍ HACE CLIC
def clickable_circle(id, emoji, label):
    # Este es un pequeño componente HTML con JavaScript que "grita" a Streamlit cuando lo tocas
    component_code = f"""
    <div id="btn-{id}" style="
        width: 250px; height: 250px; 
        border-radius: 50%; background: white; 
        border: 2px solid #1071b8; 
        display: flex; flex-direction: column; 
        align-items: center; justify-content: center; 
        cursor: pointer; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: 0.3s; margin: auto;
        font-family: 'Inter', sans-serif;">
        <div style="font-size: 60px;">{emoji}</div>
        <div style="font-weight: 800; color: #2e3788; margin-top: 10px; letter-spacing: 1px;">{label}</div>
    </div>

    <script>
        const btn = document.getElementById('btn-{id}');
        btn.onclick = function() {{
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                value: '{id}'
            }}, '*');
        }};
        btn.onmouseover = function() {{ btn.style.transform = 'scale(1.05)'; btn.style.borderColor = '#c4579b'; }};
        btn.onmouseout = function() {{ btn.style.transform = 'scale(1)'; btn.style.borderColor = '#1071b8'; }};
    </script>
    """
    # Retornamos el valor del clic a Streamlit
    return components.html(component_code, height=280)

# 5. LÓGICA DE NAVEGACIÓN
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'auth' not in st.session_state: st.session_state.auth = False

# --- VISTA HOME ---
if st.session_state.view == 'home':
    st.markdown('<h1 class="main-title">COMMAND CENTER</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if clickable_circle("nominas", "💼", "NÓMINAS"):
            st.session_state.view = "nominas"
            st.rerun()
    with col2:
        if clickable_circle("sst", "🦺", "SEGURIDAD"):
            st.session_state.view = "sst"
            st.rerun()
    with col3:
        if clickable_circle("desarrollo", "📈", "DESARROLLO"):
            st.session_state.view = "desarrollo"
            st.rerun()

# --- VISTA LOGIN / DASHBOARD ---
else:
    if st.button("⬅️ VOLVER AL INICIO"):
        st.session_state.view = 'home'
        st.session_state.auth = False
        st.rerun()

    area = st.session_state.view
    if not st.session_state.auth:
        st.markdown(f"<h2 style='text-align:center;'>🔐 ACCESO: {area.upper()}</h2>", unsafe_allow_html=True)
        _, col_login, _ = st.columns([1, 0.6, 1])
        with col_login:
            pw = st.text_input("Clave", type="password")
            if st.button("ENTRAR"):
                if pw == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Clave incorrecta")
    else:
        st.success(f"Bienvenido al Dashboard de {area.upper()}")
        # Aquí puedes poner tus tarjetas render_card de antes
