# CSV/Excel File Analyzer App

## Overview
This application is a simple, intuitive tool for analyzing and visualizing data from CSV and Excel files. Built with Streamlit, it allows users to upload a data file, select columns, and generate basic visualizations such as line plots and histograms.

## Features
- **File Upload**: Users can upload CSV or Excel files.
- **Column Selection**: Interactive selection of two columns from the uploaded file for visualization.
- **Data Visualization**: Generates line plots and histograms based on the selected data columns.
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
