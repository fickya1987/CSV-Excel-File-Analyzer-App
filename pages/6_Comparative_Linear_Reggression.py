import streamlit as st
from utils.comparative_linear_regression import perform_comparative_linear_regression

st.set_page_config(page_title="Comparative Linear Regression", page_icon="📊", layout="wide")

def display():
    st.title("Comparative Linear Regression Analysis")
    st.write("""
        Analyze Relationships Across Groups with Comparative Linear Regression.
        Select the dependent variable, independent variables, and the group variable to compare regression across groups.
    """)

    # Assuming df is stored in session_state
    df = st.session_state['df']
    numerical_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

    if df is not None:
        # Creating columns for user input options
        col1, col2, col3 = st.columns(3)
        with col1:
            dependent_var = st.selectbox("Select Dependent Variable", numerical_columns)
        with col2:
            independent_vars = st.multiselect("Select Independent Variables", numerical_columns, default=numerical_columns[:1])
        with col3:
            group_var = st.selectbox("Select Group Variable", categorical_columns)

        if st.button("Perform Regression Analysis"):
            fig, results = perform_comparative_linear_regression(df, dependent_var, independent_vars, group_var)
            
            # Display the plot
            st.plotly_chart(fig)

            # Display results
            for result in results:
                st.write(f"Group: {result['Group']}, R²: {result['R²']}, Coefficients: {result['Coefficients']}")

    else:
        st.warning("Please upload a file on the main page.")

# Call the display function
display()
