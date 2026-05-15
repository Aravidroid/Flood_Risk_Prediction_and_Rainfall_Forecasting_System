import joblib
import numpy as np

# Load model, scaler, and selected features
model = joblib.load("flood_risk_regressor.pkl")
scaler = joblib.load("scaler.pkl")
top_features = joblib.load("top_features.pkl")


def predict_flood_risk(input_features):

    # Convert to numpy array
    features_array = np.array(input_features).reshape(1, -1)

    # Scale input
    scaled_features = scaler.transform(features_array)

    # Predict flood probability
    flood_probability = model.predict(scaled_features)[0]

    # Assign risk level
    if flood_probability < 0.40:
        risk_level = "Low"
        risk_color = "green"

    elif flood_probability < 0.65:
        risk_level = "Medium"
        risk_color = "orange"

    else:
        risk_level = "High"
        risk_color = "red"

    return {
        "probability": round(float(flood_probability), 4),
        "risk_level": risk_level,
        "risk_color": risk_color
    }