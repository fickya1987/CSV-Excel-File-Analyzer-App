import streamlit as st
from utils.step_shift_analysis import detect_step_shifts, plot_data_with_shifts
st.set_page_config(page_title="Step-Shift Adjustments", page_icon="🛠️", layout="wide")
def display():
    st.title("Step Shift Adjustments")
    st.write("""
        Detect sudden changes (step-shifts) in your data. Choose a column to analyze, 
        select a detection method, define window size for rolling analysis, and set 
        a threshold to identify significant shifts.
    """)

    # Assuming df is stored in session_state
    df = st.session_state['df']
    numerical_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()

    if df is not None:
        # Creating columns for input fields
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            column = st.selectbox("Select Column", numerical_columns)

        with col2:
            method = st.selectbox("Select Method", ['rolling_mean', 'rolling_median', 'cusum'])

        with col3:
            window_size = st.number_input("Window Size", min_value=1, max_value=50, value=10)

        with col4:
            threshold = st.number_input("Threshold", value=1.0)

        if st.button("Detect Shifts"):
            shifts = detect_step_shifts(df, column, method=method, window_size=window_size, threshold=threshold)
            fig = plot_data_with_shifts(df, column, shifts)
            st.plotly_chart(fig)
    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
