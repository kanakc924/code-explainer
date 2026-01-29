import streamlit as st
import os
from dotenv import load_dotenv
from code_analyzer import CodeAnalyzer
from utils import (
    SUPPORTED_LANGUAGES, SAMPLE_CODES, detect_language, 
    validate_code, get_code_stats
)
from prompts import (
    get_code_explanation_prompt, get_specific_question_prompt,
    get_debugging_prompt, get_optimization_prompt, get_comparison_prompt
)

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Code Explainer AI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextArea textarea {
        font-family: 'Source Code Pro', monospace;
        background-color: #1e1e1e;
        color: #d4d4d4;
        border-radius: 8px;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .header-style {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    .sidebar .sidebar-content {
        background-color: #f1f3f5;
    }
    .result-container {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #e9ecef;
    }
    </style>
    """, unsafe_allow_html=True)

# App Header
st.markdown("""
    <div class="header-style">
        <h1>💻 Code Explainer AI</h1>
        <p>Expert AI-powered code analysis, debugging, and optimization</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = ""
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar Configuration
with st.sidebar:
    # st.image("https://img.icons8.com/layers/100/4a90e2/code.png", width=80)
    # st.title("Settings")
    
    # API Key Handling
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        st.warning("⚠️ API Key missing")
        api_key = st.text_input(
            "🔑 Enter Google API Key", 
            type="password",
            help="Get your free key from https://aistudio.google.com/"
        )
        if api_key:
            st.success("✅ Key entered temporarily")
    else:
        st.success("✅ API Key Configured")
    
    # st.divider()
    
    # Analysis Mode
    mode = st.selectbox(
        "Analysis Mode",
        ["Explain Code", "Ask Question", "Debug Code", "Optimize Code", "Compare Code"]
    )
    
    # Language Selection
    selected_lang = st.selectbox("Programming Language", SUPPORTED_LANGUAGES)
    
    # Detail Level (for Explain mode)
    detail_level = "Medium"
    if mode == "Explain Code":
        detail_level = st.select_slider(
            "Explanation Detail Level",
            options=["Basic", "Medium", "Advanced"],
            value="Medium"
        )
    
    # Sample Code Loader
    # st.divider()
    # sample_key = st.selectbox("Load Sample Code", ["None"] + list(SAMPLE_CODES.keys()))
    # if sample_key != "None":
    #     st.info(f"Loading {sample_key}...")
    
    st.divider()
    st.markdown("### 📜 History")
    
    if not st.session_state.history:
        st.caption("No analysis yet.")
    else:
        for i, item in enumerate(reversed(st.session_state.history[-5:])): # Show last 5
            with st.expander(f"{item['mode']} - {item['lang']}"):
                st.caption(item['result'][:150] + "...")
                if st.button("Load", key=f"hist_{i}"):
                    st.session_state.analysis_result = item['full_result']
                    st.rerun()

    st.divider()
    st.markdown("### 🛠️ How to use")
    st.write("1. Paste your code snippet.")
    st.write("2. Select mode and language.")
    st.write("3. Click 'Analyze Code'.")
    st.write("4. Download the expert analysis.")

# Main Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Input Code")
    
    # Code Input
    current_code = "" # SAMPLE_CODES.get(sample_key, "") if sample_key != "None" else ""
    code_snippet = st.text_area(
        "Paste your code here:",
        value=current_code,
        height=400,
        placeholder="public static void main(String[] args) { ... }",
        help="Paste the code you want analyzed here."
    )
    
    # Mode-specific inputs
    additional_input = {}
    if mode == "Ask Question":
        additional_input['question'] = st.text_input("What is your question about this code?", placeholder="How does the recursion work?")
    elif mode == "Debug Code":
        additional_input['error'] = st.text_input("Error message or symptoms (optional):", placeholder="Recursion depth exceeded...")
    elif mode == "Compare Code":
        st.subheader("📝 Second Code Snippet")
        code_snippet_2 = st.text_area(
            "Paste second snippet here:",
            height=300,
            placeholder="Alternative implementation...",
            key="code2"
        )
        additional_input['code2'] = code_snippet_2

    # Stats Display
    # if code_snippet:
    #     stats = get_code_stats(code_snippet)
    #     detected_lang = detect_language(code_snippet) if selected_lang == "Auto-detect" else selected_lang
        
    #     st.divider()
    #     st.subheader("📊 Code Insights")
    #     m1, m2, m3, m4 = st.columns(4)
    #     m1.metric("Lines", stats['lines'])
    #     m2.metric("Functions", stats['functions'])
    #     m3.metric("Complexity", stats['complexity'])
    #     m4.metric("Language", detected_lang)
    
    # Analyze Button
    analyze_btn = st.button("🚀 Analyze Code", use_container_width=True, type="primary")

with col2:
    st.subheader("🔍 Analysis Result")
    
    if analyze_btn:
        # Validations
        is_valid, error = validate_code(code_snippet)
        if not is_valid:
            st.error(error)
        elif mode == "Compare Code" and not code_snippet_2:
            st.error("Please provide the second code snippet for comparison.")
        elif mode == "Ask Question" and not additional_input['question']:
            st.error("Please enter a question to ask.")
        elif not api_key:
            st.error("🔑 Google API Key is required. Please provide it in the sidebar.")
        else:
            try:
                analyzer = CodeAnalyzer(api_key=api_key)
                
                # Determine Language
                final_lang = detect_language(code_snippet) if selected_lang == "Auto-detect" else selected_lang
                
                # Construct Prompt
                if mode == "Explain Code":
                    prompt = get_code_explanation_prompt(code_snippet, final_lang, detail_level)
                elif mode == "Ask Question":
                    prompt = get_specific_question_prompt(code_snippet, final_lang, additional_input['question'])
                elif mode == "Debug Code":
                    prompt = get_debugging_prompt(code_snippet, final_lang, additional_input.get('error', ""))
                elif mode == "Optimize Code":
                    prompt = get_optimization_prompt(code_snippet, final_lang)
                elif mode == "Compare Code":
                    prompt = get_comparison_prompt(code_snippet, additional_input['code2'], final_lang)
                
                # Run Analysis
                with st.spinner("🤖 AI is thinking... Please wait."):
                    result = analyzer.analyze_with_retry(prompt)
                    st.session_state.analysis_result = result
                    st.session_state.history.append({
                        "mode": mode,
                        "lang": final_lang,
                        "result": result,
                        "full_result": result
                    })
                
            except Exception as e:
                st.error(f"Initialization Error: {str(e)}")

    # Display Result
    if st.session_state.analysis_result:
        st.markdown(f'<div class="result-container">', unsafe_allow_html=True)
        st.markdown(st.session_state.analysis_result)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.divider()
        # Download Button
        st.download_button(
            label="📥 Download Analysis (.md)",
            data=st.session_state.analysis_result,
            file_name=f"code_analysis_{mode.lower().replace(' ', '_')}.md",
            mime="text/markdown",
            use_container_width=True
        )
    else:
        st.info("Paste code and click 'Analyze Code' to see the explanation here.")
        # st.image("https://img.icons8.com/illustrations/400/000000/artificial-intelligence.png", use_container_width=True)

# Footer
# st.divider()
# st.markdown("""
#     <div style="text-align: center; color: #6c757d; font-size: 14px;">
#         Made with ❤️ using Streamlit and Google Gemini AI<br>
#         © 2024 Code Explainer AI Pro
#     </div>
#     """, unsafe_allow_html=True)
