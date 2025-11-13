import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data():
    """
    Loads sample dataset as a DataFrame.
    Returns: DataFrame with features X1, X2 and target y.
    """
    data = {
        'X1': [1, 2, 3, 4, 5, 6, 7, 8],
        'X2': [5, 4, 3, 2, 1, 0, 1, 2],
        'y':  [0, 0, 0, 0, 1, 1, 1, 1]
    }
    df = pd.DataFrame(data)
    return df


def train_model(df):
    """
    Trains a simple Logistic Regression model.
    Returns: trained model and test data for evaluation.
    """
    X = df[['X1', 'X2']]
    y = df['y']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    """
    Evaluates model and returns accuracy score.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
