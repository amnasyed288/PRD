import streamlit as st
from PyPDF2 import PdfReader
import io
import os
from io import StringIO
import sys

# Import individual functions instead of the complete pipeline
from competitive_analysis import generate as generate_similar_apps, extract_app_names
from flow_tree_service import generate as generate_screen_flows
from app_flow import generate_flow_tree as generate_flow_tree
from flow_tree_design import generate as generate_design_specs
from target_app_design import generate as generate_target_design
from prd_summarizer import summarize_prd  # NEW IMPORT

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
.prd-summary-box {
    background: rgba(0, 102, 204, 0.05);
    border-left: 4px solid #0066CC;
    padding: 15px;
    border-radius: 8px;
    margin: 15px 0;
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

app_name = st.text_input("**App Name**", placeholder="e.g. Facebook")
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
# 6. RUN PIPELINE (STEP BY STEP) - NOW WITH 7 STEPS
# ======================================================================================
if st.button("🚀 Generate Design Specification", disabled=not (app_name and app_desc and uploaded_file)):
    try:
        # Real-time progress UI (7 total steps now)
        progress_bar = st.progress(0)
        status = st.empty()

        # Step 0: Summarize PRD (NEW STEP)
        status.info("📝 Step 1/7 — Analyzing and Summarizing PRD...")
        progress_bar.progress(10)
        prd_summary = summarize_prd(prd_text)
        
        
        # Step 1: Generate similar apps
        status.info("🔍 Step 2/7 — Finding Competitor Apps...")
        progress_bar.progress(20)
        similar_apps_data = generate_similar_apps(app_desc)

        # Step 2: Extract app names
        status.info("📊 Step 3/7 — Extracting App Names...")
        progress_bar.progress(35)
        app_names = extract_app_names(similar_apps_data)

        # Step 3: Generate screen flows
        status.info("📱 Step 4/7 — Generating Competitor Screen Flows...")
        progress_bar.progress(50)
        screen_flows_json = generate_screen_flows(app_names)

        # Step 4: Generate app flow tree (NOW WITH PRD SUMMARY)
        status.info("🌳 Step 5/7 — Building Your App Flow Tree...")
        progress_bar.progress(65)
        app_flow_tree = generate_flow_tree(
            app_name=app_name,
            app_description=app_desc,
            prd_summary=prd_summary,  
            app_flow_trees=screen_flows_json
        )

        # Step 5: Generate design specs of all apps
        status.info("🎨 Step 6/7 — Generating Competitor Design Specs...")
        progress_bar.progress(80)
        output_md = "all_design_specs.md"
        designs = generate_design_specs(app_flow_trees=screen_flows_json, output_file=output_md)

        if not os.path.exists(output_md):
            raise FileNotFoundError(f"Expected file '{output_md}' not found after design spec generation.")

        with open(output_md, "r", encoding="utf-8") as f:
            designs_text = f.read().strip()

        # Step 6: Generate design specs for the target app
        status.info("✨ Step 7/7 — Crafting Final Target App Design Spec...")
        progress_bar.progress(90)
        
        buffer = StringIO()
        stdout_backup = sys.stdout
        sys.stdout = buffer

        try:
            generate_target_design(app_flow_tree=app_flow_tree, designs=designs_text)
        finally:
            sys.stdout = stdout_backup

        target_design_spec = buffer.getvalue().strip()
        buffer.close()

        # Save final design spec to Markdown
        target_output_md = f"{app_name}_final_design_spec.md"
        with open(target_output_md, "w", encoding="utf-8") as f:
            f.write(target_design_spec)

        status.success("✅ All steps completed successfully!")
        progress_bar.progress(100)

        st.markdown("---")
        st.subheader("📄 Final Target App Design Specification Ready!")
        st.markdown(
            f"<p style='color:#006600;'>Your AI-generated design spec for <strong>{app_name}</strong> is ready for download.</p>",
            unsafe_allow_html=True
        )

        # Download buttons for both PRD summary and final spec
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="⬇️ Download PRD Summary (.md)",
                data=prd_summary,
                file_name=f"{app_name}_PRD_summary.md",
                mime="text/markdown"
            )
        with col2:
            st.download_button(
                label="⬇️ Download Design Specification (.md)",
                data=target_design_spec,
                file_name=f"{app_name}_final_design_spec.md",
                mime="text/markdown"
            )

    except Exception as e:
        st.error(f"❌ An error occurred during generation: {str(e)}")