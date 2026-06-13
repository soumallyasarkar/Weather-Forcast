import customtkinter as ctk
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from weather import get_weather,get_forecast,get_aqi
from location import get_location
from constant import WEATHER_IMAGES,AQI_LABELS



IMAGE_CACHE = {}
for condition, path in WEATHER_IMAGES.items():
    IMAGE_CACHE[condition] = ctk.CTkImage(
        light_image=Image.open(path),
        dark_image=Image.open(path),
        size=(140, 140)
    )
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
app.geometry("1000x750")
app.resizable(True, True)


# -----------------------------
# Function to Update Weather Illustration
# -----------------------------
def update_weather_illustration(condition):
    try:
        illustration = IMAGE_CACHE.get(
            condition,
            IMAGE_CACHE["Default"]
        )

        illustration_label.configure(
            image=illustration,
            text=""
        )

        illustration_label.image = illustration

    except Exception as e:
        print("Illustration Error:", e)
        reset_illustration()


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
# -----------------------------
# reset_illustration
# -----------------------------
def reset_illustration():
    default = IMAGE_CACHE["Default"]

    illustration_label.configure(
        image=default,
        text=""
    )

    illustration_label.image = default


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
    aqi_label.configure(
    text="AQI: --"
    )


# -----------------------------
# Reset Forecast Cards
# -----------------------------
def reset_forecast():
    for widget in forecast_cards.winfo_children():
        widget.destroy()

    empty_label = ctk.CTkLabel(
        forecast_cards,
        text="No forecast available",
        font=("Arial", 14)
    )

    empty_label.pack(pady=10)

def reset_ui(message):
    city_label.configure(text=message)
    temp_label.configure(text="--°C")
    condition_label.configure(text="")
    reset_illustration()
    reset_details()
    reset_forecast()



# -----------------------------
# Function to Load Weather Data
# -----------------------------
def load_weather(city=None):
    city_label.configure(text="Loading...")
    temp_label.configure(text="--°C")
    condition_label.configure(text="")
    app.update()
    country = ""

    # -----------------------------
    # Detect Location
    # -----------------------------
    if city is None:

        location = get_location()

        if location is None:
            reset_ui("Location Unavailable")
            return

        city = location["city"]
        country = location["country"]

    # -----------------------------
    # Get Current Weather
    # -----------------------------
    weather = get_weather(city)

    if weather is None:
        reset_ui("Weather Unavailable")
        return

    if weather.get("cod") != 200:
        reset_ui("City Not Found")
        app.after(3000,lambda: load_weather()) #Load default location after 3 seconds
        return

    # -----------------------------
    # AQI Information
    # -----------------------------
    lat = weather["coord"]["lat"]
    lon = weather["coord"]["lon"]

    aqi_data = get_aqi(lat, lon)

    if aqi_data:
        aqi = aqi_data["list"][0]["main"]["aqi"]

        aqi_label.configure(
            text=f"AQI: {AQI_LABELS[aqi]}"
        )
    else:
        aqi_label.configure(
            text="AQI: Unavailable"
        )

    # -----------------------------
    # Dynamic Weather Illustration
    # -----------------------------
    condition = weather["weather"][0]["main"]
    update_weather_illustration(condition)

    # -----------------------------
    # Dynamic Weather Icon
    # -----------------------------
    icon_code = weather["weather"][0]["icon"]
    update_weather_icon(icon_code)

    # -----------------------------
    # Update Weather Information
    # -----------------------------
    if country:
        city_label.configure(
            text=f"{weather['name']}, {country}"
        )
    else:
        city_label.configure(
            text=weather["name"]
        )

    temp_label.configure(
        text=f"{weather['main']['temp']:.2f}°C"
    )

    condition_label.configure(
        text=weather["weather"][0]["description"].title()
    )

    feels_label.configure(
        text=f"Feels Like: {weather['main']['feels_like']:.2f} °C"
    )

    humidity_label.configure(
        text=f"Humidity: {weather['main']['humidity']}%"
    )

    wind_label.configure(
        text=f"Wind Speed: {weather['wind']['speed']:.2f} m/s"
    )

    # -----------------------------
    # Update Forecast
    # -----------------------------
    update_forecast(weather["name"])




# -----------------------------
# Search Function
# -----------------------------
def search_weather():
    city = city_entry.get().strip()

    if city:
        load_weather(city)
        city_entry.delete(0, "end")
    else:
        reset_ui("Please enter a city name") 



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
# Main Content Frame
# -----------------------------
content_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

content_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

# -----------------------------
# Weather Card
# -----------------------------
weather_frame = ctk.CTkFrame(
    content_frame,
    width=350,
    height=320
)

weather_frame.pack(
    side="left",
    padx=10,
    fill="both",
    expand=True
)

weather_frame.pack_propagate(False)

weather_image_frame = ctk.CTkFrame(
    weather_frame,
    width=180,
    height=220
)

weather_image_frame.pack(
    side="left",
    padx=20,
    pady=20
)

weather_image_frame.pack_propagate(False)


weather_info_frame = ctk.CTkFrame(
    weather_frame,
    fg_color="transparent"
)

weather_info_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=20
)

illustration_label = ctk.CTkLabel(
    weather_image_frame,
    text=""
)

illustration_label.pack(
    expand=True
)






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

icon_label.pack(
    in_=weather_info_frame,
    anchor="w",
    pady=(20, 5)
)

# -----------------------------
# City Label
# -----------------------------
city_label = ctk.CTkLabel(
    app,
    text="Loading...",
    font=("Arial", 24, "bold")
)

city_label.pack(
    in_=weather_info_frame,
    anchor="w",
    pady=(20, 5)
)


# -----------------------------
# Temperature Label
# -----------------------------
temp_label = ctk.CTkLabel(
    app,
    text="--°C",
    font=("Arial", 50, "bold")
)

temp_label.pack(
    in_=weather_info_frame,
    anchor="w"
)



# -----------------------------
# Weather Condition Label
# -----------------------------
condition_label = ctk.CTkLabel(
    app,
    text="Please wait...",
    font=("Arial", 18)
)

condition_label.pack(
    in_=weather_info_frame,
    anchor="w",
    pady=5
)

# -----------------------------
# Weather Details Frame
# -----------------------------
details_frame = ctk.CTkFrame(app)

details_frame.pack(
    in_=content_frame,
    side="left",
    padx=10,
    fill="both",
    expand=True
)

details_frame.pack_propagate(False)

#details title
details_title = ctk.CTkLabel(
    details_frame,
    text="Details",
    font=("Arial", 24, "bold")
)
details_title.pack(pady=(10, 5))

#AQI Label
aqi_label = ctk.CTkLabel(
    details_frame,
    text="AQI: --",
    font=("Arial", 20, "bold")
)

aqi_label.pack(pady=10, padx=10, anchor="w")


# Feels Like
feels_label = ctk.CTkLabel(
    details_frame,
    text="Feels Like: -- °C",
    font=("Arial", 20, "bold")
)

feels_label.pack(pady=8, padx=10, anchor="w")


# Humidity
humidity_label = ctk.CTkLabel(
    details_frame,
    text="Humidity: -- %",
    font=("Arial", 20, "bold")
)

humidity_label.pack(pady=8, padx=10, anchor="w")


# Wind Speed
wind_label = ctk.CTkLabel(
    details_frame,
    text="Wind Speed: -- m/s",
    font=("Arial", 20, "bold")
)

wind_label.pack(pady=8, padx=10, anchor="w")

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
    font=("Arial", 24, "bold")
)

forecast_title.pack(pady=5)
forecast_cards = ctk.CTkFrame(
    forecast_frame,
    fg_color="transparent",
    width=120,
    height=100
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


def auto_refresh():
    load_weather()

    app.after(
        600000,
        auto_refresh
    )


# -----------------------------
# Start Application
# -----------------------------
auto_refresh()
app.mainloop()