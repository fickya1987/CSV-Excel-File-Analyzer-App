# Statistical Data Analysis App

## Overview

This enhanced Streamlit application offers a sophisticated platform for statistical data analysis. With a focus on sensor data, it provides interactive and detailed analyses, catering to both advanced users and those new to data analysis. The app now supports multi-page navigation, allowing users to focus on specific types of analyses separately, enhancing the user experience.

## Features

- **Advanced File Upload:** Supports TAR files containing CSVs, allowing for bulk data processing.
- **Multi-Page Navigation:** Each analysis type is hosted on a separate page, improving navigation and user focus.
- **Comprehensive Data Analysis Techniques:** The application includes several sophisticated data analysis methods:
  - **Setting Acceptance Upper and Lower Limits:** Analyzes data within specified boundaries.
  - **Reporting Out of Boundary Data:** Identifies and reports data points that fall outside predefined limits.
  - **Trending Historical Data Analysis:** Investigates trends and patterns over time.
  - **Curve Fitting and R² Calculation:** Performs curve fitting (linear, polynomial, exponential) and calculates the coefficient of determination.
  - **Step-Shift Adjustments:** Detects and adjusts for sudden changes or shifts in the data.
  - **Comparative Linear Regression Analysis:** Compares linear relationships between variables across different groups.
  - **3-Sigma Envelope Analysis:** Implements the 3-sigma rule for outlier detection in data.
  - **Cook's Distance Analysis:** Identifies influential points in regression analysis.
- **Enhanced Data Visualization:** Integrates Plotly for dynamic, interactive charts and graphs.
- **User-Friendly Interface:** Easy-to-navigate interface with clear options and interactive elements for a smooth user experience.
- **Streamlined Code Structure:** Code for each analysis is modularized and organized within the `utils` and for Pages in `page` directory, following best practices.

## Installation

Ensure you have Python(3.11.6) installed on your system. The application relies on various Python libraries listed in `requirements.txt`.

1. **Clone the Repository**

```bash
git clone https://cplusoft-org@dev.azure.com/cplusoft-org/statistical-analysic-streamlit-local/_git/statistical-analysic-streamlit-local
cd statistical-analysic-streamlit-local
```

2. **Create and Activate a Virtual Environment (Recommended)**

- For Windows:

```bash
  python -m venv venv
  .\venv\Scripts\activate
```

- For macOS and Linux:

```bash
 python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Running the App**
   To start the Streamlit server:

```bash
streamlit run Upload_File.py
```

Access the app in your web browser at `http://localhost:8501`.

5. **Usage**

- **File Upload:** Click "Choose a CSV or Excel file" to upload.
- **Analysis Selection:** Navigate to different pages for each type of analysis.
- **Column Selection:** Choose appropriate columns for the selected analysis.
- **View Results:** Explore the interactive visualizations and data tables.
