import streamlit as st
import models

st.set_page_config(layout="wide", page_title="Multimodal Health (Ollama Local)")

st.title("🩺 Multimodal Health Monitoring and Assessment System")
st.sidebar.header("Ollama Configuration")

ollama_host = st.sidebar.text_input("Host URL", "http://localhost:11434")
vision_model_name = st.sidebar.text_input("Vision Model", "llava", help="e.g., llava, bakllava")
llm_model_name = st.sidebar.text_input("LLM Model", "phi3", help="e.g., phi3, mistral, llama3")

st.sidebar.markdown("---")


server_up, server_msg = models.check_ollama_server(ollama_host)
models_ready = False

if server_up:
    st.sidebar.success("Server detected")
    
    vision_ready, vision_msg = models.check_ollama_model(vision_model_name)
    llm_ready, llm_msg = models.check_ollama_model(llm_model_name)
    
    if vision_ready:
        st.sidebar.success(f"Vision: {vision_model_name}")
    else:
        st.sidebar.error(f"{vision_msg}")
        
    if llm_ready:
        st.sidebar.success(f"LLM: {llm_model_name}")
    else:
        st.sidebar.error(f"{llm_msg}")
        
    models_ready = vision_ready and llm_ready
else:
    st.sidebar.error(f"{server_msg}")


col1, col2 = st.columns(2)

with col1:
    st.header("1. Visual Inputs")
    xray_file = st.file_uploader("Upload Chest X-Ray", type=['png', 'jpg', 'jpeg'])
    if xray_file:
        st.image(xray_file, caption="X-Ray Preview", use_container_width=True)
    
    ecg_file = st.file_uploader("Upload ECG Trace", type=['png', 'jpg', 'jpeg'])
    if ecg_file:
        st.image(ecg_file, caption="ECG Preview", use_container_width=True)

with col2:
    st.header("2. Clinical Notes")
    clinical_notes = st.text_area(
        "Paste Patient Notes", 
        height=400, 
        placeholder="Patient presents with..."
    )

st.divider()
submit_btn = st.button("Generate Assessment", type="primary", disabled=not models_ready)


if submit_btn:
    if not (xray_file and ecg_file and clinical_notes):
        st.error("Please provide all three inputs (X-Ray, ECG, Notes).")
    else:
        with st.spinner("Agents are working..."):
            
   
            st.write("Summarizing notes...")
            notes_summary = models.summarize_text(clinical_notes, llm_model_name)
            
            st.write("Analyzing X-Ray...")
            xray_prompt = "Analyze this chest X-ray image as a radiologist. Describe findings (opacity, infiltrates, etc.) and potential diagnosis."
            xray_bytes = xray_file.getvalue()
            xray_analysis = models.analyze_image(xray_bytes, xray_prompt, vision_model_name)
            
            st.write("Analyzing ECG...")
            ecg_prompt = "Analyze this ECG image as a cardiologist. Describe rhythm, heart rate, and any abnormalities."
            ecg_bytes = ecg_file.getvalue()
            ecg_analysis = models.analyze_image(ecg_bytes, ecg_prompt, vision_model_name)
            
            st.write("Synthesizing final report...")
            final_prompt = f"""
            You are an expert medical AI. Synthesize the following findings into a unified report.
            
            SOURCES:
            - Notes Summary: {notes_summary}
            - X-Ray Analysis: {xray_analysis}
            - ECG Analysis: {ecg_analysis}
            
            OUTPUT FORMAT (Markdown):
            1. **Risk Score** (Low/Medium/High)
            2. **Executive Summary**
            3. **Evidence by Modality**
            4. **Reasoning & Justification**
            5. **Disclaimer** (AI generated)
            """
            final_report = models.generate_synthesis(final_prompt, llm_model_name)
            
            st.success("Done!")
            st.divider()
            st.markdown(final_report)