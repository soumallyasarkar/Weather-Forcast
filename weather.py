import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={API_KEY}"
            f"&units=metric"
        )

        response = requests.get(url, timeout=5)

        data = response.json()

        return data

    except requests.exceptions.RequestException:
        return None