import streamlit as st
from PyPDF2 import PdfReader
import io

# ======================================================================================
# 1. PAGE CONFIGURATION
# ======================================================================================
st.set_page_config(
    page_title="AI Design Specification Coach",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ======================================================================================
# 2. DARK + GLASSMORPHIC THEME STYLING
# ======================================================================================

st.markdown("""
<style>
html, body, [class*="st-"] {
    font-family: "Inter", sans-serif;
    color: #F5F5F5;
}
.stApp {
    background: linear-gradient(135deg, #1A0033 0%, #003366 50%, #001F3F 100%);
    background-attachment: fixed;
}
.block-container {
    max-width: 850px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    backdrop-filter: blur(16px);
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.25), 0 0 60px rgba(255, 0, 255, 0.15);
    padding: 40px 50px;
    border: 1px solid rgba(255,255,255,0.1);
}
h1 {
    font-size: 2.6rem;
    text-align: center;
    color: #00FFFF;
    font-weight: 800;
    text-shadow: 0 0 15px rgba(0,255,255,0.5);
    margin-bottom: 0.4rem;
}
h2, h3 {
    color: #B0E3FF;
    font-weight: 600;
    text-align: center;
}
.info-box {
    background: rgba(0, 255, 170, 0.1);
    border-left: 5px solid #00FFB3;
    padding: 16px;
    border-radius: 12px;
    margin: 20px 0;
    font-size: 0.95rem;
    color: #D6D6D6;
}
textarea, input, .stTextInput>div>div>input, .stTextArea>div>textarea {
    color: #0D0D0D !important;
    background-color: #FFFFFF !important;
    border-radius: 10px !important;
    border: 1px solid #CCC !important;
    font-size: 1rem !important;
}
.stButton>button {
    background: linear-gradient(90deg, #6A5ACD, #00BFFF);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.8em 1.8em;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.25s ease;
    box-shadow: 0 0 10px rgba(0, 191, 255, 0.2);
    width: 100%;
}

.stButton>button:hover:enabled {
    background: linear-gradient(90deg, #7B68EE, #1E90FF);
    box-shadow: 0 0 18px rgba(30, 144, 255, 0.35);
    transform: translateY(-1px);
}

.stButton>button:disabled {
    background-color: #e0e0e0;
    color: #888;
    cursor: not-allowed;
    box-shadow: none;
}

.progress-container {
    width: 100%;
    background-color: rgba(255,255,255,0.08);
    border-radius: 50px;
    overflow: hidden;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}
.progress-bar {
    height: 12px;
    background: linear-gradient(90deg, #FF00FF, #00FFFF, #00FF9D);
    border-radius: 50px;
    box-shadow: 0 0 12px rgba(255,0,255,0.5);
    animation: pulseGlow 2s infinite alternate;
    transition: width 0.4s ease-in-out;
}
            
@keyframes pulseGlow {
    from { box-shadow: 0 0 10px rgba(255,0,255,0.4); }
    to { box-shadow: 0 0 25px rgba(0,255,255,0.7); }
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ======================================================================================
# 3. MAIN INTERFACE
# ======================================================================================
st.title("🤖 AI Design Specification Coach")
st.markdown(
    "<p style='text-align:center; color:#9E9E9E; font-size:1.1rem;'>Your intelligent assistant for crafting world-class design specifications.</p>",
    unsafe_allow_html=True
)

# ======================================================================================
# 4. INPUT + DYNAMIC PROGRESS
# ======================================================================================
if "processing_complete" not in st.session_state:
    st.session_state.processing_complete = False
    st.session_state.pdf_text = ""

app_name = st.text_input("**App Name**", placeholder="e.g. Visionary AI Planner")
app_desc = st.text_area("**App Description**", placeholder="Describe your app purpose, users, and features.", height=120)
uploaded_file = st.file_uploader("📄 Upload PRD (PDF only)", type="pdf")

# --- Dynamic progress calculation ---
progress = 0
if app_name:
    progress += 33
if app_desc:
    progress += 33
if uploaded_file:
    progress += 34

# --- Display dynamic progress bar ---
st.markdown(f"""uv pip show linkup

<div class="progress-container">
    <div class="progress-bar" style="width:{progress}%"></div>
</div>
""", unsafe_allow_html=True)

# ======================================================================================
# 5. LOAD PDF + BUTTON STATE
# ======================================================================================
if uploaded_file and not st.session_state.processing_complete:
    try:
        reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        st.session_state.pdf_text = "".join(page.extract_text() or "" for page in reader.pages)
        st.success(f"✅ Loaded '{uploaded_file.name}' successfully!")
    except Exception as e:
        st.error(f"⚠️ Could not read PDF: {e}")

st.markdown("---")

# --- Generate Button Disabled Logic ---
all_inputs_provided = bool(app_name and app_desc and uploaded_file)

# Display the button (disabled dynamically), but no processing logic yet
st.button("Generate Design Specification", disabled=not all_inputs_provided)


