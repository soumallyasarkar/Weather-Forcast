# 🌦️ Weather Dashboard

A modern desktop weather dashboard built with **Python** and **CustomTkinter** that provides real-time weather updates, air quality information, and a 5-day forecast with a visually appealing interface.

---

## 📸 Preview

<div align="center">

Modern Weather Dashboard with:

- Dynamic weather illustrations
- Real-time weather information
- Air Quality Index (AQI)
- 5-Day Forecast
- Automatic location detection

</div>

---

## ✨ Features

### 🌍 Weather Information
- Real-time weather updates
- Current temperature
- Feels-like temperature
- Weather conditions
- Humidity
- Wind speed

### 📍 Location Features
- Automatic location detection using IP
- Search weather by city name
- Refresh current location weather

### 🌫️ Air Quality
- Live AQI information
- AQI category display:
  - 😊 Good
  - 🙂 Fair
  - 😐 Moderate
  - 😷 Poor
  - 🤢 Very Poor

### 📅 Forecast
- 5-Day weather forecast
- Daily temperature overview

### 🎨 User Interface
- Modern CustomTkinter dashboard
- Dynamic weather illustrations
- OpenWeather condition icons
- Side-by-side dashboard layout
- Responsive window resizing

### ⚡ Extra Features
- Auto refresh every 10 minutes
- Error handling
- Executable (.exe) support

---

## 🛠️ Technologies Used

- Python 3
- CustomTkinter
- Requests
- Pillow (PIL)
- python-dotenv
- OpenWeatherMap API
- IP-based Geolocation API
- PyInstaller

---

## 📂 Project Structure

```text
Weather-Forcast/
│
├── main.py
├── weather.py
├── location.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── assets/
│   └── images/
│       ├── clear.jpg
│       ├── cloud.jpg
│       ├── mist.jpg
│       ├── rain.jpg
│       ├── snow.jpg
│       ├── thunderstorm.jpg
│       └── images.png
│
├── dist/
│   └── WeatherForecast.exe
│
└── .venv/
```

---

# 🚀 Running the Project (Python)

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Weather-Forcast.git
cd Weather-Forcast
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create the Environment File

Create a file named:

```text
.env
```

Add your OpenWeather API key:

```env
OPENWEATHER_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://openweathermap.org/api

---

## 5. Run the Application

```bash
python main.py
```

---

# 🖥️ Running the EXE Version

If you downloaded the executable version:

### Windows

Simply open:

```text
WeatherForecast.exe
```

No Python installation is required.

---

## Notes for EXE Users

- Internet connection is required.
- Weather data is fetched live.
- Automatic location detection requires internet access.
- The first launch may take a few seconds.

---

# 📦 Building the EXE Yourself

Install PyInstaller:

```bash
pip install pyinstaller
```

Build:

```powershell
pyinstaller --clean --onefile --windowed --name WeatherForecast --add-data "assets;assets" --add-data ".env;." main.py
```

The executable will be generated in:

```text
dist/WeatherForecast.exe
```

---

# 🌤️ Supported Weather Illustrations

The dashboard dynamically changes illustrations based on weather conditions.

| Condition | Illustration |
|------------|--------------|
| Clear | ☀️ Sunny |
| Clouds | ☁️ Cloudy |
| Rain | 🌧️ Rain |
| Drizzle | 🌦️ Rain |
| Snow | ❄️ Snow |
| Thunderstorm | ⛈️ Thunderstorm |
| Mist/Fog/Haze | 🌫️ Mist |
| Unknown | 🖼️ Default |

---

# 📋 Future Improvements

- [ ] Forecast weather icons
- [ ] Sunrise and sunset information
- [ ] UV Index
- [ ] Weather alerts
- [ ] Unit conversion (°C / °F)
- [ ] Multi-language support
- [ ] Settings page

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

---

# 📄 License

This project is licensed under the MIT License.

Feel free to use and modify it for educational and personal purposes.

---

# 👨‍💻 Author

**Soumallya Sarkar**

Engineering Student at IIIT Kottayam

GitHub: https://github.com/soumallyasarkar

---

<div align="center">

### ⭐ If you liked this project, consider giving it a star!

Made with ❤️ using Python and CustomTkinter

</div>