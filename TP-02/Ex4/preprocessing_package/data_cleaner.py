# preprocessing_package/data_cleaner.py

def clean_data(df, missing_value_threshold):
    """Clean the dataset by dropping columns with too many missing values."""
    if df is None:
        print("No data to clean!")
        return None

    initial_shape = df.shape
    df = df.dropna(thresh=len(df) * (1 - missing_value_threshold), axis=1)
    print(f"Cleaned data: dropped {initial_shape[1] - df.shape[1]} columns.")
    return df
