import streamlit as st
import pandas as pd
import plotly.express as px

def perform_trending_analysis(df):
    all_columns = df.columns.tolist()
    numerical_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()

    # Create two columns for selectors
    col1, col2 = st.columns(2)

    with col1:
        selected_time = st.selectbox('Select Time Column', all_columns)

    with col2:
        if 'selected_numerical' not in st.session_state:
            st.session_state.selected_numerical = numerical_columns[:2]  # Default selection
        selected_numerical = st.multiselect('Select Numerical Columns', numerical_columns, default=st.session_state.selected_numerical)

    if selected_time and selected_numerical:
        try:
            # Attempt to convert the selected column to datetime
            df[selected_time] = pd.to_datetime(df[selected_time], errors='coerce')

            # Check if conversion was successful
            if pd.api.types.is_datetime64_any_dtype(df[selected_time]):
                df.set_index(selected_time, inplace=True)  # Set the time column as index

                # Plotting the trends
                fig = px.line(df, y=selected_numerical, title='Trend Analysis Over Time')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Could not convert the selected column to a datetime format. Please select a different column or check the data format.")
        except Exception as e:
            st.error(f"An error occurred while processing the column: {e}")

