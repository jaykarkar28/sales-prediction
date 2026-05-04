from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model(X, y, model_path="models/model.pkl"):
    # Ensure models folder exists
    os.makedirs("models", exist_ok=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    print("Train Score:", model.score(X_train, y_train))
    print("Test Score:", model.score(X_test, y_test))


    joblib.dump(model, model_path)
    print("Model saved at:", model_path)

    return model