import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from src.config import MODEL_DIR

def train_models(X_train, X_test, y_train, y_test):

    models = {
        "lr": LinearRegression(),
        "rf": RandomForestRegressor(n_estimators=150, max_depth=12)
    }

    best_model = None
    best_score = -999
    best_name = None

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        mse = mean_squared_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        print(f"{name} -> MSE: {mse:.3f}, R2: {r2:.3f}")

        if r2 > best_score:
            best_score = r2
            best_model = model
            best_name = name

    joblib.dump(best_model, MODEL_DIR / f"best_model_{best_name}.pkl")

    return best_name, best_score
