import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_forecast(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    data = response.json()

    print("API Response:", data)


    # -------------------------------------------------
    # CHECK IF API FAILED
    # -------------------------------------------------

    if "list" not in data:

        return {
            "rainfall": 0,
            "temperature": 0,
            "humidity": 0,
            "weather": "API Error"
        }


    # -------------------------------------------------
    # GET FORECAST DATA
    # -------------------------------------------------

    forecast = data["list"][0]

    rainfall = 0

    if "rain" in forecast:
        rainfall = forecast["rain"].get("3h", 0)

    temperature = forecast["main"]["temp"]

    humidity = forecast["main"]["humidity"]

    weather = forecast["weather"][0]["description"]


    return {
    "rainfall": rainfall,
    "temperature": temperature,
    "humidity": humidity,
    "weather": weather,
    "wind": forecast["wind"]["speed"]
}