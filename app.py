import streamlit as st
from parser import parse_log
from analyzer1 import count_severity, count_services, top_errors, overall_health
import ui

st.set_page_config(page_title="Log Analyzer", layout="wide")

ui.show_header()

log_type = st.sidebar.selectbox("Select log Type", ["nginx", "jenkins", "app"])
uploaded_file = st.sidebar.file_uploader("Upload Log File", type=["log", "txt"])

if uploaded_file is not None:
    
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    
    logs = parse_log(log_type, temp_file_path)

    
    severity = count_severity(logs)
    services = count_services(logs)
    errors = top_errors(logs)
    health = overall_health(logs)

    
    ui.show_summary_cards(len(logs), severity.get('ERROR', 0), health)
    ui.show_table("Top Errors", errors)
