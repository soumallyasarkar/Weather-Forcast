from weather import get_weather

city = input("Enter city name: ")

data = get_weather(city)

if data.get("cod") == 200:
    print("\nWeather Details")
    print("----------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"])
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("Error:", data.get("message"))