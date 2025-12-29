import numpy as np

def predict_soil(model, nitrogen, phosphorus, potassium, ph, moisture):
    """
    Predict soil type using a pre-trained model.
    """
    features = np.array([[nitrogen, phosphorus, potassium, ph, moisture]])
    prediction = model.predict(features)
    return prediction[0]
