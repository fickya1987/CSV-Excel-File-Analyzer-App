import streamlit as st
from utils.file_handling_utils import handle_uploaded_files
from st_aggrid import AgGrid

# Set page configuration with wide layout
st.set_page_config(page_title="Statistical Analysis Dashboard", page_icon="📊", layout="wide")

# Title of the main app
st.title('Statistical Data Analysis App')

# Introduction and instructions
st.markdown("""
Welcome to the Statistical Data Analysis App! This interactive tool offers a variety of analyses to explore and understand your data. Simply upload your TAR file containing CSVs, and choose the type of analysis you want to perform from the sidebar.

### How to Use:
1. **Upload Your Data**: Drag and drop your TAR files containing CSV datasets.
2. **Select Analysis**: Choose an analysis from the sidebar.
3. **Interactive Results**: View the results and visualizations.

Please note that the analysis options are accessible from the sidebar. Each analysis provides unique insights into your data, ranging from trend analysis to outlier detection.
""")

# File upload functionality
uploaded_files = st.file_uploader("Choose TAR files containing CSVs", type=['tar'], accept_multiple_files=True)

# Global variables to store data
if 'df' not in st.session_state:
    st.session_state['df'] = None
    st.session_state['numerical_columns'] = None
    st.session_state['categorical_columns'] = None

# If files are uploaded, handle the files and get the dataframe
if uploaded_files:
    st.session_state['df'], st.session_state['numerical_columns'], st.session_state['categorical_columns'] = handle_uploaded_files(uploaded_files)
    # Displaying the dataframe
    AgGrid(st.session_state['df'].head())
    # Confirmation message
    st.success("Data successfully uploaded! Please select an analysis from the sidebar.")
else:
    st.info("Awaiting data upload. Please upload a TAR file containing CSV datasets.")
