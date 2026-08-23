import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()

def get_weather(city_name):
    api_key = os.getenv("API_KEY_WEATHERA")
    base_url = "http://api.weatherapi.com/v1"
    res = requests.get(f"{base_url}/current.json?key={api_key}&q={city_name}")
    res = res.json()
    name_city = res["location"]["name"]
    weather_conditions = res["current"]["condition"]["text"]
    temp_in_c = res["current"]["temp_c"]
    humidity = res["current"]["humidity"]
    data_time = time.time()

    data = {
        "name_city": name_city,
        "weather_conditions": weather_conditions,
        "temp_in_c": temp_in_c,
        "humidity": humidity,
        "current_type": str(data_time)
    }
    return data