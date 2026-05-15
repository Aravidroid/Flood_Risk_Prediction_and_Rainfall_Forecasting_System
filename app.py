from flask import Flask, render_template, request
from predict import predict_flood_risk
from weather_api import get_weather_forecast
from forecast import predict_rainfall


app = Flask(__name__)


# =========================================================
# HOME ROUTE
# =========================================================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    risk_level = None
    risk_color = None

    future_rainfall = None

    temperature = None
    humidity = None
    weather = None
    wind_speed = None

    city = None

    if request.method == "POST":

        # -------------------------------------------------
        # GET USER INPUTS
        # -------------------------------------------------

        city = request.form["City"]

        urbanization = float(
            request.form["Urbanization"]
        )

        coastal_vulnerability = float(
            request.form["CoastalVulnerability"]
        )

        drainage_systems = float(
            request.form["DrainageSystems"]
        )

        agricultural_practices = float(
            request.form["AgriculturalPractices"]
        )

        political_factors = float(
            request.form["PoliticalFactors"]
        )


        # -------------------------------------------------
        # GET LIVE WEATHER DATA
        # -------------------------------------------------

        weather_data = get_weather_forecast(city)

        temperature = weather_data["temperature"]

        humidity = weather_data["humidity"]

        weather = weather_data["weather"]

        wind_speed = weather_data["wind"]


        # -------------------------------------------------
        # AI RAINFALL PREDICTION
        # -------------------------------------------------

        # Approximate minimum temperature
        temp_min = temperature - 3

        future_rainfall = predict_rainfall(

            temperature,
            temp_min,
            wind_speed

        )


        # -------------------------------------------------
        # FLOOD RISK PREDICTION
        # -------------------------------------------------

        input_features = [

            urbanization,
            coastal_vulnerability,
            drainage_systems,
            agricultural_practices,
            political_factors

        ]

        result = predict_flood_risk(input_features)

        prediction = result["probability"]

        risk_level = result["risk_level"]

        risk_color = result["risk_color"]


    # -----------------------------------------------------
    # RENDER TEMPLATE
    # -----------------------------------------------------

    return render_template(

        "index.html",

        prediction=prediction,

        risk_level=risk_level,

        risk_color=risk_color,

        future_rainfall=future_rainfall,

        temperature=temperature,

        humidity=humidity,

        weather=weather,

        wind_speed=wind_speed,

        city=city

    )


# =========================================================
# RUN FLASK APP
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)