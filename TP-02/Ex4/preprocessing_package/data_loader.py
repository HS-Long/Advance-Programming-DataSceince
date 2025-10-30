# preprocessing_package/data_loader.py

import pandas as pd
from .config import DATA_PATH

def load_data():
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(DATA_PATH)
        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print("File not found at:", DATA_PATH)
        return None
