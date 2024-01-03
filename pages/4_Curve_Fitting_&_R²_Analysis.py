import streamlit as st
import streamlit as st
from utils.curve_fitting_analysis import perform_curve_fitting_analysis

st.set_page_config(page_title="Curve Fitting Analysis", page_icon="🧬", layout="wide")
def display():
    st.title("Curve Fitting Analysis")
    st.write("Explore linear, polynomial, and exponential relationships between variables.")

    # Assuming df is stored in session_state
    df = st.session_state['df']
    numerical_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object', 'string', 'category']).columns.tolist()

    if df is not None:
        # Combining all possible column choices
        all_columns = numerical_columns + categorical_columns

        # Creating two columns for independent and dependent variable selection
        col1, col2 = st.columns(2)
        with col1:
            independent_var = st.selectbox("Select Independent Variable", options=all_columns)
        with col2:
            dependent_var = st.selectbox("Select Dependent Variable", options=all_columns)

        # Additional considerations for curve fitting
        relationship_type = st.selectbox("Select Relationship Type", options=["linear", "polynomial", "exponential"])
        degree = None
        if relationship_type == "polynomial":
            degree = st.number_input("Enter the Degree of Polynomial", min_value=1, max_value=10, value=2)

        if st.button("Perform Analysis"):
            try:
                # Ensure appropriate columns are selected for curve fitting
                if independent_var in categorical_columns or dependent_var in categorical_columns:
                    st.error("Please select appropriate numerical columns for curve fitting.")
                else:
                    fig, r2 = perform_curve_fitting_analysis(df, independent_var, dependent_var, relationship_type, degree)
                    st.plotly_chart(fig)
                    st.write(f"R² Value: {r2}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
