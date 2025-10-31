import streamlit as st
from PyPDF2 import PdfReader
import io
import json
from main import generate_complete_pipeline

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
# 2. LIGHT THEME STYLING
# ======================================================================================
st.markdown("""
<style>
html, body, [class*="st-"] {
    font-family: "Inter", sans-serif;
    color: #1E1E1E;
}
.stApp {
    background: linear-gradient(135deg, #F8FBFF 0%, #EAF3FF 50%, #FFFFFF 100%);
    background-attachment: fixed;
    height: 100vh;
    overflow-y: auto;
}
.block-container {
    max-width: 850px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.05);
    padding: 40px 50px;
    border: 1px solid rgba(0,0,0,0.08);
    margin-top: 2rem;
    margin-bottom: 2rem;
}
h1 {
    font-size: 2.6rem;
    text-align: center;
    color: #0066CC;
    font-weight: 800;
    text-shadow: 0 0 10px rgba(0,102,204,0.15);
    margin-bottom: 0.4rem;
}
.progress-container {
    width: 100%;
    background-color: rgba(0,0,0,0.05);
    border-radius: 50px;
    overflow: hidden;
    margin-bottom: 20px;
    border: 1px solid rgba(0,0,0,0.08);
}
.progress-bar {
    height: 12px;
    background: linear-gradient(90deg, #007BFF, #00C2FF, #00FFA3);
    border-radius: 50px;
    box-shadow: 0 0 12px rgba(0, 183, 255, 0.5);
    animation: pulseGlow 2s infinite alternate;
    transition: width 0.4s ease-in-out;
}
@keyframes pulseGlow {
    from { box-shadow: 0 0 10px rgba(0, 183, 255, 0.3); }
    to { box-shadow: 0 0 20px rgba(0, 255, 163, 0.6); }
}
footer {visibility: hidden;}
.stButton>button {
    background: linear-gradient(90deg, #007BFF, #00C2FF);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    padding: 0.6rem 1.5rem;
    box-shadow: 0 4px 12px rgba(0, 150, 255, 0.25);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #0066CC, #00A6E0);
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(0, 150, 255, 0.35);
}
</style>
""", unsafe_allow_html=True)

# ======================================================================================
# 3. INPUT SECTION
# ======================================================================================
st.title("🤖 AI Design Specification Coach")
st.markdown(
    "<p style='text-align:center; color:#444; font-size:1.1rem;'>Generate your full app design specification in minutes using AI.</p>",
    unsafe_allow_html=True
)

app_name = st.text_input("**App Name**", placeholder="e.g. WealthNest")
app_desc = st.text_area("**App Description**", placeholder="Describe your app purpose, users, and features.", height=120)
uploaded_file = st.file_uploader("📄 Upload PRD (PDF only)", type="pdf")

# ======================================================================================
# 4. DYNAMIC PROGRESS BAR (real-time as you fill fields)
# ======================================================================================
progress = 0
if app_name:
    progress += 33
if app_desc:
    progress += 33
if uploaded_file:
    progress += 34

st.markdown(f"""
<div class="progress-container">
    <div class="progress-bar" style="width:{progress}%"></div>
</div>
""", unsafe_allow_html=True)

# ======================================================================================
# 5. LOAD PDF CONTENT
# ======================================================================================
prd_text = ""
if uploaded_file:
    try:
        reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        prd_text = "".join(page.extract_text() or "" for page in reader.pages)
        st.success(f"✅ Loaded '{uploaded_file.name}' successfully!")
    except Exception as e:
        st.error(f"⚠️ Could not read PDF: {e}")

st.markdown("---")

# ======================================================================================
# 6. RUN PIPELINE
# ======================================================================================
if st.button("🚀 Generate Design Specification", disabled=not (app_name and app_desc and uploaded_file)):
    try:
        # Real-time progress UI (6 total steps)
        progress_bar = st.progress(0)
        status = st.empty()

        steps = [
            ("🔍 Step 1/6 — Finding Competitor Apps...", 15),
            ("📊 Step 2/6 — Extracting App Names...", 30),
            ("📱 Step 3/6 — Generating Competitor Screen Flows...", 45),
            ("🌳 Step 4/6 — Building Your App Flow Tree...", 60),
            ("🎨 Step 5/6 — Generating Competitor Design Specs...", 80),
            ("✨ Step 6/6 — Crafting Final Target App Design Spec...", 100),
        ]

        for label, pct in steps:
            status.info(label)
            progress_bar.progress(pct)
            if pct == 15:
                results = generate_complete_pipeline(app_desc, app_name)

        target_design_spec = results.get("target_design_spec", "")

        status.success("✅ All steps completed successfully!")
        progress_bar.progress(100)

        st.markdown("---")
        st.subheader("📄 Final Target App Design Specification Ready!")
        st.markdown(
            f"<p style='color:#006600;'>Your AI-generated design spec for <strong>{app_name}</strong> is ready for download.</p>",
            unsafe_allow_html=True
        )

        st.download_button(
            label="⬇️ Download Target Design Specification (.md)",
            data=target_design_spec,
            file_name=f"{app_name}_final_design_spec.md",
            mime="text/markdown"
        )

    except Exception as e:
        st.error(f"❌ An error occurred during generation: {str(e)}")
