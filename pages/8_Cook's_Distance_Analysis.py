import streamlit as st
from utils.cooks_distance_analysis import cooks_distance_analysis

st.set_page_config(page_title="Cook's Distance Analysis", page_icon="🍳", layout="wide")

def display():
    st.title("Cook's Distance Analysis")
    st.write("""
        Cook's Distance Analysis helps identify influential outliers in regression models. 
        It highlights data points that have a significant effect on the regression coefficients.
    """)

    # Assuming df is stored in session_state
    df = st.session_state['df']
    numerical_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()

    if df is not None:
        # Creating two columns for independent and dependent variable selection
        col1, col2 = st.columns(2)
        with col1:
            dependent_var = st.selectbox("Select Dependent Variable", numerical_columns)
        with col2:
            independent_vars = st.multiselect("Select Independent Variables", numerical_columns, default=numerical_columns[:1])

        if st.button("Perform Cook's Distance Analysis"):
            try:
                fig = cooks_distance_analysis(df, dependent_var, independent_vars)
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"An error occurred: {e}")

    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
