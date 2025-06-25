import streamlit as st
import pandas as pd

st.set_page_config(page_title="Insight Agent", layout="wide")

st.title("🤖 Insight Agent: Business Data Consultant")

# Layout: Upload, Question, and Action
col1, col2 = st.columns([2, 3])

with col1:
    st.header("1. Upload Your Data")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
    else:
        df = None

with col2:
    st.header("2. Ask a Business Question")
    question = st.text_area("Type your business question here", height=100)
    analyze_btn = st.button("Analyze & Generate Insights")

# Placeholder for insights and report
st.markdown("---")

if analyze_btn and df is not None and question:
    st.subheader("3. Insights & Analysis")
    # Placeholder: Call agent pipeline here
    st.markdown(
        "_Agentic GPT pipeline would analyze the data and answer:_"
    )
    st.success(f"**Question:** {question}")
    st.info("**Insights:**\n- Example trend\n- Example risk\n- Example recommendation")
    # Placeholder for chart
    st.bar_chart(df.select_dtypes(include='number'))
    # Placeholder for report download
    st.markdown("\n4. Download Your Report")
    st.download_button(
        label="Download PDF Report",
        data=b"PDF content would go here",
        file_name="insight_report.pdf",
        mime="application/pdf"
    )
else:
    st.info("Upload a CSV and enter a question to get started.")
