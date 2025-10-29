import pandas as pd


def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded dataset.
    """
    data = pd.read_csv(file_path)
    print("Data loaded successfully.")
    return data


def filter_data(dataframe, min_age):
    """
    Filter rows in the DataFrame where 'age' is greater than a specified minimum.

    Args:
        dataframe (pandas.DataFrame): The dataset to filter.
        min_age (int): The minimum age threshold.

    Returns:
        pandas.DataFrame: Filtered DataFrame containing only rows above the threshold.
    """
    filtered_data = dataframe[dataframe["age"] > min_age]
    print(f"{len(filtered_data)} rows retained after filtering.")
    return filtered_data
