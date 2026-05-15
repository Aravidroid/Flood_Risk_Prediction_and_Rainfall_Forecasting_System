import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


# =========================================================
# 1. LOAD DATASET
# =========================================================

print("=" * 60)
print("[INFO] Loading dataset...")
print("=" * 60)

df = pd.read_csv("train.csv")

print("[INFO] Dataset Shape:", df.shape)


# =========================================================
# 2. PREPARE FEATURES & TARGET
# =========================================================

# Use all features initially
X_all = df.drop(columns=["id", "FloodProbability"])
y = df["FloodProbability"]

print("\n[INFO] Total Features:", len(X_all.columns))


# =========================================================
# 3. TEMPORARY MODEL FOR FEATURE IMPORTANCE
# =========================================================

print("\n[INFO] Finding important features...")

temp_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

temp_model.fit(X_all, y)


# =========================================================
# 4. FEATURE IMPORTANCE ANALYSIS
# =========================================================

importance_df = pd.DataFrame({
    "Feature": X_all.columns,
    "Importance": temp_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\n========== FEATURE IMPORTANCE ==========\n")
print(importance_df)


# =========================================================
# 5. SELECT TOP FEATURES
# =========================================================

TOP_N_FEATURES = 5

top_features = importance_df.head(TOP_N_FEATURES)["Feature"].tolist()

print("\n[INFO] Selected Top Features:")
for i, feature in enumerate(top_features, start=1):
    print(f"{i}. {feature}")

# Final training data
X = df[top_features]


# =========================================================
# 6. TRAIN TEST SPLIT
# =========================================================

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n[INFO] Training Samples:", X_train.shape[0])
print("[INFO] Validation Samples:", X_val.shape[0])


# =========================================================
# 7. FEATURE SCALING
# =========================================================

print("\n[INFO] Scaling features...")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)


# =========================================================
# 8. TRAIN FINAL MODEL
# =========================================================

print("\n[INFO] Training Random Forest Model...")

model = RandomForestRegressor(
    n_estimators=150,
    max_depth=15,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train_scaled, y_train)

print("[SUCCESS] Model training completed!")


# =========================================================
# 9. MODEL EVALUATION
# =========================================================

print("\n[INFO] Evaluating model...")

y_pred = model.predict(X_val_scaled)

rmse = np.sqrt(mean_squared_error(y_val, y_pred))
r2 = r2_score(y_val, y_pred)

print("\n========== MODEL PERFORMANCE ==========")
print(f"RMSE Score : {rmse:.4f}")
print(f"R² Score   : {r2:.4f}")


# =========================================================
# 10. RAINFALL SIMULATION
# =========================================================

print("\n[INFO] Running rainfall simulation...")

X_simulated = X_val.copy()

# Increase all selected features by 30%
for col in top_features:
    X_simulated[col] = X_simulated[col] * 1.3

# Scale simulated data
X_simulated_scaled = scaler.transform(X_simulated)

# Predictions
baseline_predictions = model.predict(X_val_scaled)
simulated_predictions = model.predict(X_simulated_scaled)

print("[SUCCESS] Rainfall simulation completed!")


# =========================================================
# 11. GENERATE VISUALIZATIONS
# =========================================================

print("\n[INFO] Generating plots...")


# ---------------------------------------------------------
# Plot 1: Actual vs Predicted
# ---------------------------------------------------------

plt.figure(figsize=(7, 5))

plt.scatter(
    y_val[:3000],
    y_pred[:3000],
    alpha=0.4
)

plt.xlabel("Actual Flood Probability")
plt.ylabel("Predicted Flood Probability")
plt.title("Actual vs Predicted Flood Probability")

plt.savefig(
    "actual_vs_predicted.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------------------------------
# Plot 2: Feature Importance
# ---------------------------------------------------------

top_importance_df = importance_df.head(TOP_N_FEATURES)

plt.figure(figsize=(7, 5))

plt.barh(
    top_importance_df["Feature"],
    top_importance_df["Importance"]
)

plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.title("Top Important Features")

plt.gca().invert_yaxis()

plt.savefig(
    "feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------------------------------
# Plot 3: Rainfall Simulation
# ---------------------------------------------------------

plt.figure(figsize=(7, 5))

plt.hist(
    baseline_predictions,
    bins=50,
    alpha=0.6,
    label="Before Simulation"
)

plt.hist(
    simulated_predictions,
    bins=50,
    alpha=0.6,
    label="After Simulation"
)

plt.xlabel("Flood Probability")
plt.ylabel("Frequency")
plt.title("Flood Risk Before vs After Rainfall Simulation")

plt.legend()

plt.savefig(
    "rainfall_simulation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("[SUCCESS] All plots saved successfully!")


# =========================================================
# 12. SAVE MODEL & SCALER
# =========================================================

print("\n[INFO] Saving model and scaler...")

joblib.dump(model, "flood_risk_regressor.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(top_features, "top_features.pkl")

print("[SUCCESS] Model saved: flood_risk_regressor.pkl")
print("[SUCCESS] Scaler saved: scaler.pkl")
print("[SUCCESS] Features saved: top_features.pkl")


# =========================================================
# 13. FINAL SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("TRAINING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nSelected Features:")
for feature in top_features:
    print(f"✓ {feature}")

print(f"\nFinal RMSE Score : {rmse:.4f}")
print(f"Final R² Score   : {r2:.4f}")

print("\nGenerated Files:")
print("✓ flood_risk_regressor.pkl")
print("✓ scaler.pkl")
print("✓ top_features.pkl")
print("✓ actual_vs_predicted.png")
print("✓ feature_importance.png")
print("✓ rainfall_simulation.png")

print("\nProject Ready for Flask Integration 🚀")