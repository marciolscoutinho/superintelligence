import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    df = df.dropna()
    return df
