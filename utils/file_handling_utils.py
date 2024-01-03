# file_handling_utils.py
import os
import tarfile
import tempfile
import pandas as pd
import numpy as np

def extract_tar_file(tar_path, extract_path):
    with tarfile.open(tar_path, 'r') as tar:
        tar.extractall(path=extract_path)

def merge_csv_from_directory(directory_path):
    csv_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.csv')]
    df_list = [pd.read_csv(file) for file in csv_files]
    return pd.concat(df_list, ignore_index=True)

def handle_uploaded_files(uploaded_files):
    all_dfs = []
    with tempfile.TemporaryDirectory() as temp_dir:
        for uploaded_file in uploaded_files:
            tar_path = os.path.join(temp_dir, uploaded_file.name)
            with open(tar_path, 'wb') as f:
                f.write(uploaded_file.getvalue())
            extract_tar_file(tar_path, temp_dir)
            all_dfs.append(merge_csv_from_directory(temp_dir))

    df = pd.concat(all_dfs, ignore_index=True)
    numerical_columns = df.select_dtypes(include=['float', 'int', 'Int64', 'uint', 'boolean']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object', 'string', 'category', 'datetime64[ns]', np.timedelta64]).columns.tolist()
    return df, numerical_columns, categorical_columns
