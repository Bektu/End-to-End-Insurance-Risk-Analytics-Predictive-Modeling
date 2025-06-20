# src/modeling/evaluate_models.py

from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate_models(models, X_test, y_test):
    results = {}
    for name, model in models.items():
        preds = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        r2 = r2_score(y_test, preds)
        results[name] = {"RMSE": rmse, "R2": r2}
    return results
