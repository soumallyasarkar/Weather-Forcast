import requests

API_KEY = "ab62c8a7705ced6ade99f0a19e9dafc0"


def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    return data