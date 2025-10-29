import pandas as pd


def clean_data(df):
    """
    Simple function to clean missing values in a DataFrame.
    """
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df
