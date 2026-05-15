# 🌊 AI-Based Urban Flood Risk Prediction and Rainfall Forecasting System
## 📌 Project Overview

This project is an AI-powered web application that predicts:

* 🌧️ Future Rainfall using Machine Learning
* 🌊 Urban Flood Risk using AI Models
* ☁️ Real-Time Weather Information using OpenWeather API

The system integrates:

* Machine Learning
* Real-Time Weather APIs
* Geospatial/Environmental Factors
* Flask Web Development

\---

# 🚀 Features

## ✅ Real-Time Weather Forecast

Uses OpenWeatherMap API to fetch:

* Temperature
* Humidity
* Wind Speed
* Weather Conditions

\---

## ✅ AI Rainfall Prediction

Machine Learning model predicts rainfall using:

* Temperature
* Minimum Temperature
* Wind Speed

\---

## ✅ AI Flood Risk Prediction

Flood probability is predicted using:

* Urbanization
* Coastal Vulnerability
* Drainage Systems
* Agricultural Practices
* Political Factors

\---

## ✅ Interactive Web Dashboard

Users can:

1. Enter city name
2. Input environmental parameters
3. View rainfall prediction
4. View flood risk analysis

\---

# 🧠 Technologies Used

|Technology|Purpose|
|-|-|
|Python|Core Programming|
|Flask|Web Framework|
|Scikit-Learn|Machine Learning|
|Pandas|Data Processing|
|NumPy|Numerical Operations|
|Matplotlib|Data Visualization|
|OpenWeatherMap API|Live Weather Data|
|HTML/CSS|Frontend UI|

\---

# 📂 Project Structure

```bash
Flood_Risk_Prediction_and_Rainfall_Forecasting_System/
│
├── .env
├── app.py
├── predict.py
├── weather_api.py
├── forecast.py
├── train_model.py
├── train_rainfall.py
├── flood_risk_regressor.pkl
├── scaler.pkl
├── rainfall_forecast_model.pkl
├── top_features.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md
```

\---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Aravidroid/Flood\_Risk\_Prediction\_and\_Rainfall\_Forecasting\_System.git
cd Flood_Risk_Prediction_and_Rainfall_Forecasting_System
```

\---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\\Scripts\\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

\---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

\---

# 🏋️ Train the Models First

Before running the Flask application, you must train both AI models.

Run the following files one by one:

## 1️⃣ Train Flood Prediction Model

```bash
python train_model.py
```

This generates:
- flood_risk_regressor.pkl
- scaler.pkl
- top_features.pkl

---

## 2️⃣ Train Rainfall Forecasting Model

```bash
python train_rainfall.py
```

This generates:
- rainfall_forecast_model.pkl

---

# ⚠️ Important

Do NOT run `app.py` before training the models.
The application requires all `.pkl` model files to exist.

# 🔑 OpenWeather API Setup

1. Create account:
https://openweathermap.org/
2. Generate API key
3. Open:

```python
weather_api.py
```

4. Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key.

\---

# ▶️ Run the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

\---

# 🌊 Example Inputs

|Parameter|Example|
|-|-|
|City|Chennai|
|Urbanization|9|
|Coastal Vulnerability|8|
|Drainage Systems|2|
|Agricultural Practices|7|
|Political Factors|6|

\---

# 📊 Example Output

```text
Forecasted Rainfall: 14.13 mm

Temperature: 24.88 °C

Humidity: 83%

Flood Probability: 0.50

Risk Level: Medium
```

\---

# 🧠 Machine Learning Models

## 🌧️ Rainfall Prediction Model

* Algorithm: Linear Regression
* Inputs:

  * Temperature
  * Wind Speed
  * Minimum Temperature

\---

## 🌊 Flood Prediction Model

* Algorithm: Random Forest Regressor
* Target:

  * Flood Probability

\---



# 🌍 Future Improvements

* Real flood zone maps
* Satellite rainfall integration
* LSTM weather forecasting
* GIS visualization
* SMS flood alerts
* Live dashboards

\---

# 👨‍💻 Author

Aravind A

\---

# 📜 License

This project is for educational and research purposes.