import streamlit as st
from utils.sigma_envelope_analysis import perform_sigma_envelope_analysis
st.set_page_config(page_title="3-Sigma Envelope Analysis", page_icon="🔮", layout="wide")

def display():
    st.title("3-Sigma Envelope Analysis")
    st.write("""
        The 3-Sigma Envelope Analysis identifies data points that deviate significantly from the mean. 
        It is based on the statistical rule that in a normal distribution, most values (99.7%) 
        lie within three standard deviations (sigma) of the mean. Select the column to analyze 
        and choose the sigma level to visualize the envelope and highlight outliers.
    """)

    # Assuming df is stored in session_state
    df = st.session_state['df']
    numerical_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()

    if df is not None:
        # Create columns for user inputs
        col1, col2 = st.columns(2)
        with col1:
            column_to_analyze = st.selectbox("Select Column for Analysis", numerical_columns)
        with col2:
            sigma_level = st.selectbox("Select Sigma Level", [1, 2, 3], format_func=lambda x: f"{x}-Sigma")

        if st.button("Perform 3-Sigma Analysis"):
            try:
                # Call the analysis function and get the figure
                fig = perform_sigma_envelope_analysis(df, column_to_analyze, sigma_level)

                # Display the plot
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"An error occurred during the analysis: {e}")

    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
