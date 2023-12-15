import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title('CSV/Excel File Analyzer')

# Create a file uploader to accept CSV or Excel files
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # Read the file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, encoding='utf-8')
        else:
            df = pd.read_excel(uploaded_file)

        # Display the dataframe
        st.write(df)

        # Select columns for visualization
        st.subheader('Select Columns for Visualization')
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect('Select two columns', all_columns, default=all_columns[:2])
        
        if len(selected_columns) != 2:
            st.error('Please select exactly two columns for visualization.')
        else:
            # Preprocessing selected columns
            df_vis = df[selected_columns].dropna()
            df_vis = df_vis.apply(pd.to_numeric, errors='coerce').dropna()

            # Visualization options
            plot_type = st.radio("Select Plot Type", ('Line Plot', 'Histogram'))

            # Visualization: Line Plot
            if plot_type == 'Line Plot' and st.button('Show Line Plot'):
                plt.figure(figsize=(10, 4))
                sns.lineplot(data=df_vis)
                st.pyplot(plt)

            # Visualization: Histogram
            if plot_type == 'Histogram' and st.button('Show Histogram'):
                plt.figure(figsize=(10, 4))
                for col in selected_columns:
                    sns.histplot(df_vis[col], kde=True, label=col)
                plt.legend()
                st.pyplot(plt)

    except Exception as e:
        st.error(f"An error occurred: {e}")
