# CSV/Excel File Analyzer App

## Overview
This Streamlit application provides an intuitive interface for analyzing and visualizing data from CSV and Excel files. It now includes user authentication for added security and uses Plotly for interactive data visualization, offering a more dynamic and engaging user experience.

## Features
- **User Authentication:** Secure login system to restrict access to authorized users.
- **Interactive Data Visualization:** Utilizes Plotly for creating interactive line plots, bar charts, scatter plots, and histograms.
- **File Upload**: Users can upload CSV or Excel files.
- **Column Selection**: Interactive selection of two columns from the uploaded file for visualization.
- **Plotly Integration:** Offers enhanced, interactive charts with hover-over details for a deeper data exploration.
- **Error Handling**: Robust error handling for file reading and data processing.

## Installation
To run this application, you will need Python installed on your system. The application depends on several Python libraries, which are listed in `requirements.txt`.

1. **Clone the Repository**
```bash
    git clone https://github.com/Kheem-Dh/CSV-Excel-File-Analyzer-App.git
    cd CSV-Excel-File-Analyzer-App
```

2. **Create and Activate a Virtual Environment (Optional but Recommended)**
- For Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Install Dependencies**
- Install Requirements 
```bash
pip install -r requirements.txt
```

## Running the App
- Execute the following command in your terminal to start the Streamlit server and run the application:
```bash
streamlit run app.py
```
Navigate to the local URL provided by Streamlit (usually `http://localhost:8501`) in your web browser to view the app.

## Usage
- **Uploading a File**: Click on the "Choose a CSV or Excel file" button to upload a file.
- **Selecting Columns**: Choose two columns from your file for analysis and visualization.
- **Visualizing Data**: Select either a line plot or a histogram, and click the corresponding button to generate the visualization.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## Contact
For any queries or further assistance, please contact Kheem Dharmani at dharmanikheem@gmail.com.
