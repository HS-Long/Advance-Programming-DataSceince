import pytest
from Exercise3 import evaluate_model

def test_perfect_predictions():
    print("\n TEST 1: Perfect Predictions (Accuracy = 1.0)")
    y_true = [1, 0, 1, 0]
    y_pred = [1, 0, 1, 0]

    result = evaluate_model(y_true, y_pred)
    print("Evaluation result:", result)

    assert result["accuracy"] == 1.0, "Accuracy should be 1.0 for perfect predictions"
    print(" Test passed: Accuracy is 1.0")

    assert "f1_score" in result, "Result must contain f1_score key"
    print(" Test passed: Output contains f1_score key")


def test_all_predictions_wrong():
    print("\n TEST 2: All Predictions Wrong (F1 = 0.0)")
    y_true = [1, 1, 0, 0]
    y_pred = [0, 0, 1, 1]

    result = evaluate_model(y_true, y_pred)
    print("Evaluation result:", result)

    # Accuracy should be 0.0
    assert result["accuracy"] == 0.0, "Accuracy should be 0.0 when all predictions are wrong"
    # F1 should also be 0.0
    assert result["f1_score"] == 0.0, "F1 score should be 0.0 when all predictions are wrong"
    print(" Test passed: Accuracy = 0.0 and F1 = 0.0")


def test_output_contains_keys():
    print("\n TEST 3: Output Contains Both Keys")
    y_true = [1, 0, 1, 0]
    y_pred = [1, 1, 0, 0]

    result = evaluate_model(y_true, y_pred)
    print("Evaluation result:", result)

    assert "accuracy" in result and "f1_score" in result, "Output must contain both accuracy and f1_score keys"
    print(" Test passed: Output contains both required keys.")
