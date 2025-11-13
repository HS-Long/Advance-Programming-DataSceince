import pandas as pd

def normalize_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Normalize the specified column values to a range between 0 and 1.
    Returns a new DataFrame with the normalized column.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame")

    min_val = df[column].min()
    max_val = df[column].max()

    # Handle case where all values are identical
    if min_val == max_val:
        df[column] = 0.0
    else:
        df[column] = (df[column] - min_val) / (max_val - min_val)

    return df
