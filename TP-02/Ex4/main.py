# main.py
from preprocessing_package import load_data, clean_data, MISSING_VALUE_THRESHOLD

def main():
    # Step 1: Load data
    df = load_data()
    
    # Step 2: Clean data
    cleaned_df = clean_data(df, MISSING_VALUE_THRESHOLD)

    # Step 3: Display result
    if cleaned_df is not None:
        print("Final cleaned dataset shape:", cleaned_df.shape)

if __name__ == "__main__":
    main()
