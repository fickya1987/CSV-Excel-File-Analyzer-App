import streamlit as st
import plotly.express as px

def perform_upper_lower_limits_analysis(df, numerical_columns):
    st.markdown("#### Setting Acceptance Upper and Lower Limits:")
    st.write("This analysis requires one numerical column to set upper and lower limits.")
    selected_numerical = st.multiselect('Select Numerical Columns', numerical_columns, default=numerical_columns[:1])

    if selected_numerical:
        # Create two columns for the input fields
        col1, col2 = st.columns(2)

        with col1:
            lower_limit = st.number_input('Set Lower Limit', value=df[selected_numerical[0]].min())

        with col2:
            upper_limit = st.number_input('Set Upper Limit', value=df[selected_numerical[0]].max())

        # Apply the limits and display the data
        filtered_data = df[df[selected_numerical[0]].between(lower_limit, upper_limit)]
        st.write("Filtered Data based on specified limits:")

        # Create a scrollable container
        data_container = st.empty()
        with data_container.container():
            st.dataframe(filtered_data, height=300)  # Adjust the height as needed

        if not filtered_data.empty:
            # Create two columns for the plots
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### Box Plot")
                fig_box = px.box(filtered_data, y=selected_numerical, 
                                title="Box Plot of Filtered Data")
                st.plotly_chart(fig_box, use_container_width=True)

            with col2:
                st.markdown("#### Histogram")
                fig_hist = px.histogram(filtered_data, x=selected_numerical[0],
                                        title="Histogram of Filtered Data")
                st.plotly_chart(fig_hist, use_container_width=True)
