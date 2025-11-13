import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows and rows containing null values.
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df
