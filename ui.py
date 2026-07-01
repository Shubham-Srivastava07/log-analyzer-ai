import streamlit as st

def show_header():
    st.title("🤖 AI Log Analyzer")
    st.caption("Upload any log file and instantly generate health summary.")
    st.markdown("---")

def show_summary_cards(total, error_count, health):
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Logs", total)
    col2.metric("Errors", error_count)
    
    # Health status ke liye color coding
    if "Critical" in health:
        col3.error(health)
    elif "Warning" in health:
        col3.warning(health)
    else:
        col3.success(health)

def show_table(title, data):
    st.subheader(title)
    # Data ko 2 columns mein convert karna
    import pandas as pd
    df = pd.DataFrame(data, columns=["Error Message", "Count"])
    st.table(df)
