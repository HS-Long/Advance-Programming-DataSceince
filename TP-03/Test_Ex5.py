from Exercise5 import load_data, train_model, evaluate_model

def test_end_to_end_pipeline():
    print("\n TEST: End-to-End ML Pipeline")

    # Step 1: Load data
    df = load_data()
    print(" Data loaded successfully:\n", df.head())

    # Verify data correctness
    assert not df.empty, "DataFrame is empty"
    assert all(col in df.columns for col in ['X1', 'X2', 'y']), "Missing required columns"
    print(f" Data columns OK: {list(df.columns)}")

    # Step 2: Train model
    model, X_test, y_test = train_model(df)
    print(" Model trained successfully.")
    print(f"Test data shape: {X_test.shape}")

    # Step 3: Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    print(f" Model evaluated. Accuracy = {accuracy:.2f}")

    # Assertions
    assert 0.0 <= accuracy <= 1.0, "Accuracy is not within [0, 1]"
    print(" Test passed: Accuracy is within range [0, 1].")
