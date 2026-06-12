from weather import get_weather
from location import get_location


print("Detecting your location...")

location = get_location()

if location is None:
    print("Could not detect location.")
    exit()

city = location["city"]
country = location["country"]

print(f"Location Found: {city}, {country}")

weather = get_weather(city)

if weather is None:
    print("Unable to fetch weather data.")
    exit()


if weather.get("cod") == 200:
    print("\nWeather Details")
    print("----------------")

    print("City:", weather["name"])
    print("Temperature:", weather["main"]["temp"], "°C")
    print("Feels Like:", weather["main"]["feels_like"], "°C")
    print("Humidity:", weather["main"]["humidity"], "%")
    print("Condition:", weather["weather"][0]["description"])
    print("Wind Speed:", weather["wind"]["speed"], "m/s")

else:
    print("Error:", weather.get("message"))