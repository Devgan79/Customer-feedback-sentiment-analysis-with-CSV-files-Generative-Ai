import streamlit as st
import pandas as pd
from analysis import analyze_feedback

st.title("Customer Feedback Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    #DataFrame preview
    st.write("### Uploaded Data Preview")
    st.dataframe(df.head())

    # Let the user select the column containing reviews after seeing the data
    column_name = st.selectbox("Select the column containing reviews", df.columns)

    # Ask the user a few questions to customize the analysis
    st.write("### Customize Your Analysis")

    # Example questions for users to provide input
    analysis_focus = st.radio(
        "What would you like to focus on?",
        ('Sentiment Analysis', 'Theme Identification', 'Improvement Suggestions', 'All of the Above')
    )

    # If a column is selected and user inputs are given, proceed with analysis
    if column_name:
        feedback_list = df[column_name].dropna().tolist()

        if st.button("Analyze Feedback"):
            # Passing the user inputs to the analyze_feedback function
            result = analyze_feedback(feedback_list, analysis_focus)

            st.write("### Analysis Results")
            st.markdown(result)


#####TO RUN THIS TYPE THIS(streamlit run main.py)
