from sklearn.metrics import accuracy_score, f1_score

def evaluate_model(y_true, y_pred):
    """
    Evaluate a model's predictions using accuracy and F1 score.
    Returns a dictionary with {'accuracy': ..., 'f1_score': ...}.
    """
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    return {"accuracy": acc, "f1_score": f1}
