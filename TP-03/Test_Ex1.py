import pandas as pd
from Exercise1 import clean_data

def test_remove_duplicates():
    data = {'A': [1, 1, 2], 'B': [3, 3, 4]}
    df = pd.DataFrame(data)
    cleaned = clean_data(df)

    print("\n TEST 1: Remove Duplicates")
    print("Before cleaning:\n", df)
    print("After cleaning:\n", cleaned)
    print(f" Rows before: {len(df)}, after: {len(cleaned)}")

    assert len(cleaned) == 2
    assert cleaned.duplicated().sum() == 0
    print(" Test passed: Duplicates removed correctly.")


def test_remove_nulls():
    data = {'A': [1, 2, None], 'B': [3, None, 5]}
    df = pd.DataFrame(data)
    cleaned = clean_data(df)

    print("\n TEST 2: Remove Nulls")
    print("Before cleaning:\n", df)
    print("After cleaning:\n", cleaned)
    print(f" Rows before: {len(df)}, after: {len(cleaned)}")

    assert cleaned.isnull().sum().sum() == 0
    assert len(cleaned) == 1
    print(" Test passed: Null values removed correctly.")


def test_rows_decrease_after_cleaning():
    data = {'A': [1, 1, 2, None], 'B': [3, 3, 4, 5]}
    df = pd.DataFrame(data)
    cleaned = clean_data(df)

    print("\n TEST 3: Rows Decrease After Cleaning")
    print("Before cleaning:\n", df)
    print("After cleaning:\n", cleaned)
    print(f" Rows before: {len(df)}, after: {len(cleaned)}")

    assert len(cleaned) < len(df)
    print(" Test passed: Number of rows decreased after cleaning.")
