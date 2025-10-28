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
    height: 100vh;
    overflow-y: auto;
}

/* Custom scrollbar styling */
.stApp::-webkit-scrollbar {
    width: 12px;
}

.stApp::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 10px;
}

.stApp::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #6A5ACD, #00BFFF);
    border-radius: 10px;
    border: 2px solid rgba(0, 0, 0, 0.3);
}

.stApp::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #7B68EE, #1E90FF);
}

/* Firefox scrollbar */
.stApp {
    scrollbar-width: thin;
    scrollbar-color: #6A5ACD rgba(0, 0, 0, 0.3);
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
    margin-top: 2rem;
    margin-bottom: 2rem;
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
.success-box {
    background: rgba(0, 255, 170, 0.15);
    border-left: 5px solid #00FF9D;
    padding: 16px;
    border-radius: 12px;
    margin: 20px 0;
    font-size: 1rem;
    color: #E0E0E0;
}
.competitor-container {
    max-height: 500px;
    overflow-y: auto;
    padding-right: 10px;
    margin: 20px 0;
}

.competitor-container::-webkit-scrollbar {
    width: 8px;
}

.competitor-container::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 10px;
}

.competitor-container::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #00FFFF, #00FFB3);
    border-radius: 10px;
}

.competitor-container::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #00FFD9, #00FF9D);
}

.competitor-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(0, 255, 255, 0.2);
    border-radius: 12px;
    padding: 12px 16px;
    margin: 8px 0;
    transition: all 0.3s ease;
}
.competitor-card:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(0, 255, 255, 0.4);
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.2);
}
.flow-section {
    background: rgba(138, 43, 226, 0.08);
    border-left: 4px solid #8A2BE2;
    padding: 20px;
    border-radius: 10px;
    margin: 15px 0;
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

.json-viewer {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 20px;
    color: #E0E0E0;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    overflow-x: auto;
    max-height: 600px;
    overflow-y: auto;
}

/* Custom scrollbar for JSON viewer */
.json-viewer::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

.json-viewer::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 10px;
}

.json-viewer::-webkit-scrollbar-thumb {
    background: rgba(106, 90, 205, 0.6);
    border-radius: 10px;
}

.json-viewer::-webkit-scrollbar-thumb:hover {
    background: rgba(106, 90, 205, 0.8);
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
# 4. SESSION STATE INITIALIZATION
# ======================================================================================
if "processing_complete" not in st.session_state:
    st.session_state.processing_complete = False
    st.session_state.pdf_text = ""
    st.session_state.competitor_data = None
    st.session_state.screen_flows = None
    st.session_state.app_names = None
    st.session_state.app_flow_tree = None

# ======================================================================================
# 5. INPUT + DYNAMIC PROGRESS
# ======================================================================================

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
st.markdown(f"""
<div class="progress-container">
    <div class="progress-bar" style="width:{progress}%"></div>
</div>
""", unsafe_allow_html=True)

# ======================================================================================
# 6. LOAD PDF
# ======================================================================================
if uploaded_file and not st.session_state.pdf_text:
    try:
        reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        st.session_state.pdf_text = "".join(page.extract_text() or "" for page in reader.pages)
        st.success(f"✅ Loaded '{uploaded_file.name}' successfully!")
    except Exception as e:
        st.error(f"⚠️ Could not read PDF: {e}")

st.markdown("---")

# ======================================================================================
# 7. GENERATE BUTTON WITH PIPELINE
# ======================================================================================

all_inputs_provided = bool(app_name and app_desc and uploaded_file)

if st.button("Generate Design Specification", disabled=not all_inputs_provided):
    # Reset previous results
    st.session_state.competitor_data = None
    st.session_state.screen_flows = None
    st.session_state.app_names = None
    st.session_state.app_flow_tree = None
    st.session_state.processing_complete = False
    
    try:
        # STEP 1: Finding Competitors
        with st.spinner("🔍 Finding Competitors..."):
            results = generate_complete_pipeline(app_desc, app_name)
            
            if results and results.get("competitor_apps"):
                st.session_state.competitor_data = results["competitor_apps"]
                st.session_state.app_names = results["app_names"]
                
        # Show success message
        st.markdown("""
        <div class="success-box">
            ✅ <strong>Competitors Found!</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # STEP 2: Finding Visuals (Screen Flows)
        with st.spinner("🎨 Analyzing Competitor Screen Flows..."):
            # Screen flows already generated in pipeline
            st.session_state.screen_flows = results.get("screen_flows")
        
        # Show success message
        st.markdown("""
        <div class="success-box">
            ✅ <strong>Competitor Screen Flows Analyzed!</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # STEP 3: Generating App Flow Tree
        with st.spinner("🌳 Generating Your App's Flow Tree..."):
            # App flow tree already generated in pipeline
            st.session_state.app_flow_tree = results.get("app_flow_tree")
        
        # Show success message
        st.markdown("""
        <div class="success-box">
            ✅ <strong>App Flow Tree Generated!</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.session_state.processing_complete = True
        
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.session_state.processing_complete = False

# ======================================================================================
# 8. DISPLAY RESULTS
# ======================================================================================

if st.session_state.processing_complete and st.session_state.competitor_data:
    
    st.markdown("---")
    st.markdown("## 📊 Analysis Results")
    
    # Display Competitor Apps
    st.markdown("### 🏆 Competitor Apps")
    
    competitor_apps = st.session_state.competitor_data.get("apps", [])
    
    if competitor_apps:
        st.markdown(f"<p style='color:#B0E3FF; font-size:1rem;'>Found <strong>{len(competitor_apps)}</strong> similar apps:</p>", unsafe_allow_html=True)
        
        for i, app in enumerate(competitor_apps, 1):
            downloads = app.get("estimated_download_count", 0)
            downloads_formatted = f"{downloads:,}"
            
            st.markdown(f"""
            <div class="competitor-card">
                <strong style="color:#00FFFF; font-size:1.1rem;">{i}. {app.get('app_name', 'Unknown')}</strong><br>
                <span style="color:#9E9E9E; font-size:0.9rem;">📥 {downloads_formatted} downloads</span>
            </div>
            """, unsafe_allow_html=True)
    
    # Display Screen Flows
    if st.session_state.screen_flows:
        st.markdown("---")
        st.markdown("### 🎨 Competitor Screen Flow Analysis")
        
        try:
            # Parse and display the JSON
            flows_data = json.loads(st.session_state.screen_flows)
            
            st.markdown("""
            <div class="flow-section">
                <p style="color:#E0E0E0; font-size:1rem;">
                    Complete screen flow trees have been generated for the competitor apps. 
                    This data includes navigation paths, user actions, and screen transitions.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display formatted JSON
            with st.expander("📱 View Complete Competitor Screen Flows JSON", expanded=False):
                st.json(flows_data)
            
            # Optional: Display summary statistics
            if "apps_screen_flows" in flows_data:
                total_apps = len(flows_data["apps_screen_flows"])
                total_flows = sum(len(app.get("app_screen_flows", [])) for app in flows_data["apps_screen_flows"])
                
                st.markdown(f"""
                <div class="info-box">
                    📊 <strong>Summary:</strong> Analyzed {total_apps} apps with {total_flows} total user flows
                </div>
                """, unsafe_allow_html=True)
                
        except json.JSONDecodeError:
            st.code(st.session_state.screen_flows, language="json")
        except Exception as e:
            st.error(f"❌ Error displaying screen flows: {str(e)}")
    
    # Display App Flow Tree
    if st.session_state.app_flow_tree:
        st.markdown("---")
        st.markdown("### 🌳 Your App's Flow Tree")
        
        try:
            # Parse and display the JSON
            app_flow_data = json.loads(st.session_state.app_flow_tree)
            
            st.markdown("""
            <div class="flow-section">
                <p style="color:#E0E0E0; font-size:1rem;">
                    🎉 Your custom app flow tree has been generated based on competitor analysis and best UX practices. 
                    This represents the complete user journey through your app.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display formatted JSON
            with st.expander("🚀 View Your App's Complete Flow Tree", expanded=True):
                st.json(app_flow_data)
            
            # Display summary statistics
            if "app_flow_tree" in app_flow_data:
                flow_tree = app_flow_data["app_flow_tree"]
                total_flows = len(flow_tree.get("app_screen_flows", []))
                total_screens = sum(
                    len(flow.get("screens", [])) 
                    for flow in flow_tree.get("app_screen_flows", [])
                )
                based_on = flow_tree.get("based_on_competitors", [])
                
                st.markdown(f"""
                <div class="info-box">
                    📊 <strong>Flow Tree Summary:</strong><br>
                    • {total_flows} main user flows<br>
                    • {total_screens} total screens<br>
                    • Based on insights from {len(based_on)} competitor apps
                </div>
                """, unsafe_allow_html=True)
                
        except json.JSONDecodeError:
            st.code(st.session_state.app_flow_tree, language="json")
        except Exception as e:
            st.error(f"❌ Error displaying app flow tree: {str(e)}")
    
    # Download buttons
    st.markdown("---")
    st.markdown("### 💾 Download Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.session_state.competitor_data:
            competitor_json = json.dumps(st.session_state.competitor_data, indent=2)
            st.download_button(
                label="⬇️ Competitors",
                data=competitor_json,
                file_name="competitor_apps.json",
                mime="application/json"
            )
    
    with col2:
        if st.session_state.screen_flows:
            st.download_button(
                label="⬇️ Screen Flows",
                data=st.session_state.screen_flows,
                file_name="competitor_screen_flows.json",
                mime="application/json"
            )
    
    with col3:
        if st.session_state.app_flow_tree:
            st.download_button(
                label="⬇️ App Flow Tree",
                data=st.session_state.app_flow_tree,
                file_name=f"{app_name.lower().replace(' ', '_')}_flow_tree.json",
                mime="application/json"
            )