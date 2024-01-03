import streamlit as st
import plotly.express as px

def perform_out_of_boundary_analysis(df, numerical_columns):
    selected_numerical = st.multiselect('Select Numerical Columns', numerical_columns, default=numerical_columns[:1])

    if selected_numerical:
        # Create two columns for the input fields
        col1, col2 = st.columns(2)

        with col1:
            lower_limit = st.number_input('Set Lower Limit', value=df[selected_numerical[0]].min())

        with col2:
            upper_limit = st.number_input('Set Upper Limit', value=df[selected_numerical[0]].max())

        # Identifying Outliers
        outliers_data = df[~df[selected_numerical[0]].between(lower_limit, upper_limit)]
        st.write("Data Points Outside the Specified Limits:")

        # Create a scrollable container for the outliers
        outliers_container = st.empty()
        with outliers_container.container():
            st.dataframe(outliers_data, height=300)  # Adjust the height as needed

        # Visualization (example: Box Plot highlighting outliers)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Box Plot with Outliers Highlighted")
            fig_box = px.box(df, y=selected_numerical, 
                             title="Box Plot with Outliers")
            st.plotly_chart(fig_box, use_container_width=True)
        with col2:
            st.markdown("#### Histogram with Outliers")
            fig_hist = px.histogram(df, x=selected_numerical[0], 
                                    color=df[selected_numerical[0]].apply(lambda x: 'Outlier' if x < lower_limit or x > upper_limit else 'Inlier'),
                                    title="Histogram Highlighting Outliers")
            st.plotly_chart(fig_hist, use_container_width=True)

