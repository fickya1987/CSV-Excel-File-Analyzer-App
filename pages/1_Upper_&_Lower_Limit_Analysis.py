import streamlit as st
from utils.upper_lower_limits_analysis import perform_upper_lower_limits_analysis

st.set_page_config(page_title="Upper & Lower Limits Analysis", page_icon="📏", layout="wide")

def display():
    st.title("Upper and Lower Limits Analysis")
    
    # Assuming df is stored in session_state
    df = st.session_state['df']
    numerical_columns = st.session_state['numerical_columns']

    if df is not None:
        perform_upper_lower_limits_analysis(df, numerical_columns)
    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
