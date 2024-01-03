import streamlit as st
from utils.trending_analysis import perform_trending_analysis

st.set_page_config(page_title="Trending Analysis", page_icon="📈", layout="wide")

def display():
    st.title("Trending Historical Data Analysis")
    st.write("Analyze trends over time by selecting a time column and one or more numerical columns.")

    # Assuming df is stored in session_state
    df = st.session_state['df']

    if df is not None:
        perform_trending_analysis(df)
    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
