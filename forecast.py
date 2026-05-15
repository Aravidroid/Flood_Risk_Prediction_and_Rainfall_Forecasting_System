import joblib
import numpy as np


# Load trained AI model
model = joblib.load("rainfall_forecast_model.pkl")


def predict_rainfall(temp_max, temp_min, wind):

    features = np.array([[
        temp_max,
        temp_min,
        wind
    ]])

    prediction = model.predict(features)[0]

    return round(float(prediction), 2)