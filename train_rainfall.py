import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

print("[INFO] Loading rainfall dataset...")

df = pd.read_csv("weather.csv")

print(df.head())
df = df.dropna()
# Weather features
X = df[[
    "temp_max",
    "temp_min",
    "wind"
]]

# Target rainfall
y = df["precipitation"]


# =========================================================
# TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================================================
# TRAIN MODEL
# =========================================================

print("[INFO] Training AI Rainfall Model...")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("[SUCCESS] Model trained!")


# =========================================================
# EVALUATE MODEL
# =========================================================

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print(f"MAE Score : {mae:.4f}")
print(f"R² Score  : {r2:.4f}")


# =========================================================
# SAVE MODEL
# =========================================================

joblib.dump(model, "rainfall_forecast_model.pkl")

print("[SUCCESS] rainfall_forecast_model.pkl saved!")