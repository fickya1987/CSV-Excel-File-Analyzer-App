import streamlit as st
from utils.out_of_boundary_analysis import perform_out_of_boundary_analysis
st.set_page_config(page_title="Out of Boundary Analysis", page_icon="🚧", layout="wide")
def display():
    st.title("Reporting Out of Boundary Data")
    st.write("Select numerical column to identify data points that fall outside the specified limits.")

    # Assuming df is stored in session_state
    df = st.session_state['df']
    numerical_columns = st.session_state['numerical_columns']

    if df is not None:
        perform_out_of_boundary_analysis(df, numerical_columns)
    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
