import numpy as np
import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

MODEL_PATH = "model/soil_model.pkl"

def load_or_create_model():
    if not os.path.exists(MODEL_PATH):
        # Create model folder if missing
        os.makedirs("model", exist_ok=True)

        # Synthetic soil dataset
        data = {
            "N": [20, 50, 80, 60, 40, 70, 90, 30, 55, 65, 25, 85],
            "P": [15, 40, 70, 50, 35, 60, 80, 25, 45, 55, 20, 75],
            "K": [10, 30, 50, 40, 25, 45, 65, 15, 35, 50, 12, 60],
            "pH": [6.0, 6.5, 7.0, 6.8, 6.2, 7.1, 7.2, 6.1, 6.6, 6.9, 6.3, 7.0],
            "Moisture": [20, 30, 40, 35, 25, 38, 45, 22, 32, 37, 24, 42],
            "SoilType": [
                "Sandy", "Loamy", "Clayey", "Loamy", "Sandy", "Clayey",
                "Clayey", "Sandy", "Loamy", "Clayey", "Sandy", "Loamy"
            ]
        }
        df = pd.DataFrame(data)
        X = df[["N", "P", "K", "pH", "Moisture"]]
        y = df["SoilType"]

        model = DecisionTreeClassifier()
        model.fit(X, y)

        joblib.dump(model, MODEL_PATH)
    
    # Load model
    model = joblib.load(MODEL_PATH)
    return model

def predict_soil(model, nitrogen, phosphorus, potassium, ph, moisture):
    features = np.array([[nitrogen, phosphorus, potassium, ph, moisture]])
    return model.predict(features)[0]
