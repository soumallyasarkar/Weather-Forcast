import customtkinter as ctk
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from weather import get_weather,get_forecast
from location import get_location


# -----------------------------
# App Configuration
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -----------------------------
# Create Main Window
# -----------------------------
app = ctk.CTk()
app.title("Weather Forecast")
app.geometry("720x1000")
app.resizable(True, True)




# -------------------------------
# Function to Update Weather Icon
# -------------------------------
def update_weather_icon(icon_code):
    try:
        icon_url = (
            f"https://openweathermap.org/img/wn/"
            f"{icon_code}@4x.png"
        )

        response = requests.get(icon_url, timeout=5)

        image = Image.open(BytesIO(response.content))

        weather_icon = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(100, 100)
        )

        icon_label.configure(
            image=weather_icon,
            text=""
        )

        icon_label.image = weather_icon

    except Exception:
        icon_label.configure(
            text="🌍",
            image=None
        )



def reset_forecast():
    for widget in forecast_cards.winfo_children():
        widget.destroy()

    empty_label = ctk.CTkLabel(
        forecast_cards,
        text="No forecast available",
        font=("Arial", 14)
    )

    empty_label.pack(pady=10)

# -----------------------------
# Function to Load Weather Data
# -----------------------------
def load_weather(city=None):
    city_label.configure(text="Loading...")
    temp_label.configure(text="--°C")
    condition_label.configure(text="")
    icon_label.configure(text="🌍")

    app.update()

    country = ""

    if city is None:

        location = get_location()

        if location is None:
            city_label.configure(text="Location Error")
            temp_label.configure(text="--°C")
            condition_label.configure(text="Could not detect location")
            reset_details()
            reset_forecast()
            return  

        city = location["city"]
        country = location["country"]


    weather = get_weather(city)

    if weather is None:
        city_label.configure(text="Weather Error")
        condition_label.configure(
            text="Unable to fetch weather data"
        )
        reset_details()
        reset_forecast()
        return

    if weather.get("cod") != 200:
        city_label.configure(text="City Not Found")
        condition_label.configure(
            text=weather.get("message", "Invalid city")
        )
        reset_details()
        reset_forecast()
        return
    



    # Weather Data
    icon_code = weather["weather"][0]["icon"]
    update_weather_icon(icon_code)
    
    if country:
        city_label.configure(
            text=f"{weather['name']}, {country}"
        )
    else:
        city_label.configure(
            text=weather["name"]
        )

    temp_label.configure(
        text=f"{weather['main']['temp']}°C"
    )

    condition_label.configure(
        text=weather["weather"][0]["description"].title()
    )

    feels_label.configure(
        text=f"Feels Like: {weather['main']['feels_like']} °C"
    )

    humidity_label.configure(
        text=f"Humidity: {weather['main']['humidity']}%"
    )

    wind_label.configure(
        text=f"Wind Speed: {weather['wind']['speed']} m/s"
    )
    update_forecast(weather["name"])

# -----------------------------
# Search Function
# -----------------------------
def search_weather():
    city = city_entry.get().strip()

    if city:
        load_weather(city)
        city_entry.delete(0, "end")


# -----------------------------
# Reset Weather Details
# -----------------------------
def reset_details():
    feels_label.configure(
        text="Feels Like: -- °C"
    )

    humidity_label.configure(
        text="Humidity: -- %"
    )

    wind_label.configure(
        text="Wind Speed: -- m/s"
    )

# -----------------------------
# Update Forecast Function
# -----------------------------


def update_forecast(city):
    forecast = get_forecast(city)

    if (
        forecast is None
        or forecast.get("cod") != "200"
    ):
        return

    for widget in forecast_cards.winfo_children():
        widget.destroy()

    shown = 0

    for item in forecast["list"]:
        if "12:00:00" in item["dt_txt"]:

            day = datetime.strptime(
                item["dt_txt"],
                "%Y-%m-%d %H:%M:%S"
            ).strftime("%a")

            temp = round(item["main"]["temp"])

            label = ctk.CTkLabel(
                forecast_cards,
                text=f"{day}\n{temp}°C"
            )

            label.pack(
                side="left",
                expand=True,
                padx=5,
                pady=10
            )

            shown += 1

            if shown == 5:
                break

# -----------------------------
# Title
# -----------------------------
title_label = ctk.CTkLabel(
    app,
    text="🌦 Weather Forecast",
    font=("Arial", 28, "bold")
)

title_label.pack(pady=(20, 10))


# -----------------------------
# Search Section
# -----------------------------
search_frame = ctk.CTkFrame(app)

search_frame.pack(pady=10)

city_entry = ctk.CTkEntry(
    search_frame,
    placeholder_text="Enter city name",
    width=220
)

city_entry.pack(
    side="left",
    padx=5,
    pady=10
)

search_button = ctk.CTkButton(
    search_frame,
    text="Search",
    command=search_weather,
    width=80
)

search_button.pack(
    side="left",
    padx=5
)


# -----------------------------
# Weather Icon
# -----------------------------
icon_label = ctk.CTkLabel(
    app,
    text=""
)

icon_label.pack(pady=(20, 5))

# -----------------------------
# City Label
# -----------------------------
city_label = ctk.CTkLabel(
    app,
    text="Loading...",
    font=("Arial", 24, "bold")
)

city_label.pack(pady=5)


# -----------------------------
# Temperature Label
# -----------------------------
temp_label = ctk.CTkLabel(
    app,
    text="--°C",
    font=("Arial", 50, "bold")
)

temp_label.pack()


# -----------------------------
# Weather Condition Label
# -----------------------------
condition_label = ctk.CTkLabel(
    app,
    text="Please wait...",
    font=("Arial", 18)
)

condition_label.pack(pady=5)


# -----------------------------
# Weather Details Frame
# -----------------------------
details_frame = ctk.CTkFrame(app)

details_frame.pack(
    pady=30,
    padx=20,
    fill="x"
)


# Feels Like
feels_label = ctk.CTkLabel(
    details_frame,
    text="Feels Like: -- °C",
    font=("Arial", 16)
)

feels_label.pack(pady=8)


# Humidity
humidity_label = ctk.CTkLabel(
    details_frame,
    text="Humidity: -- %",
    font=("Arial", 16)
)

humidity_label.pack(pady=8)


# Wind Speed
wind_label = ctk.CTkLabel(
    details_frame,
    text="Wind Speed: -- m/s",
    font=("Arial", 16)
)

wind_label.pack(pady=8)

# ------------------------------
# Forecast Frame
# ------------------------------
forecast_frame = ctk.CTkFrame(app)
forecast_frame.pack(
    pady=10,
    padx=20,
    fill="x"
)
forecast_title = ctk.CTkLabel(
    forecast_frame,
    text="5-Day Forecast",
    font=("Arial", 18, "bold")
)

forecast_title.pack(pady=5)
forecast_cards = ctk.CTkFrame(
    forecast_frame,
    fg_color="transparent"
)

forecast_cards.pack(fill="x")


# -----------------------------
# Refresh Button
# -----------------------------
refresh_button = ctk.CTkButton(
    app,
    text="Refresh Current Location",
    command=lambda: load_weather(),
    width=220,
    height=40
)

refresh_button.pack(pady=30)


# -----------------------------
# Load Weather Initially
# -----------------------------
load_weather()


# -----------------------------
# Start Application
# -----------------------------
app.mainloop()