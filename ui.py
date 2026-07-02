import streamlit as st

def show_header():
    st.title("🤖 AI Log Analyzer")
    st.caption("Upload any log file and instantly generate health summary.")
    st.markdown("---")

def show_summary_cards(total, error_count, health):
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Logs", total)
    col2.metric("Errors", error_count)
    col3.metric("Health", health)
    
def show_health_badge(health):
    if "Healthy" in health:
        st.markdown("### Status: 🟢 Healthy")
    elif "Warning" in health:
        st.markdown("### Status: 🟡 Warning")
    else:
        st.markdown("### Status: 🔴 Critical")

def show_table(title, data):
    st.subheader(title)
    # Data ko 2 columns mein convert karna
    import pandas as pd
    df = pd.DataFrame(data, columns=["Error Message", "Count"])
    st.table(df)
