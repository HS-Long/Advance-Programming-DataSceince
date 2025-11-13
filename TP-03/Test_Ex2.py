import pandas as pd
import pytest
from Exercise2 import normalize_column

def test_normalized_values_within_range():
    print("\n TEST 1: Normalized Values Within [0, 1]")
    df = pd.DataFrame({'A': [10, 20, 30, 40, 50]})
    print("Before normalization:\n", df)

    normalized = normalize_column(df.copy(), 'A')
    print("After normalization:\n", normalized)

    assert (normalized['A'] >= 0).all() and (normalized['A'] <= 1).all(), "Values not within [0,1]"
    print(" Test passed: All normalized values are within [0, 1].")


def test_output_length_matches_input():
    print("\n TEST 2: Output Length Matches Input")
    df = pd.DataFrame({'A': [5, 15, 25, 35]})
    print("Before normalization:\n", df)

    normalized = normalize_column(df.copy(), 'A')
    print("After normalization:\n", normalized)

    assert len(normalized) == len(df), "Output length does not match input"
    print(f" Test passed: Output has {len(normalized)} rows (same as input).")


def test_invalid_column_raises_keyerror():
    print("\n TEST 3: Invalid Column Raises KeyError")
    df = pd.DataFrame({'A': [1, 2, 3]})
    print("DataFrame:\n", df)

    try:
        normalize_column(df, 'B')
    except KeyError as e:
        print(f" Test passed: Caught expected error → {e}")
        return

    # If no exception is raised
    pytest.fail(" Expected KeyError was not raised.")
