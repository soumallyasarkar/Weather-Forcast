# 🌦️ Weather Forecast App

A modern Python desktop application that retrieves and displays real-time weather information with automatic user location detection.

The application uses geolocation to identify the user's current city and fetches live weather data using the OpenWeatherMap API. It is designed with simplicity, reliability, and an intuitive user experience in mind.

---

## 📌 Features

- 🌍 Automatic user location detection using IP geolocation
- ☁️ Real-time weather updates
- 🌡️ Current temperature and "feels like" temperature
- 💧 Humidity information
- 🌬️ Wind speed details
- 🏙️ Displays city and country information
- 🔒 Secure API key management using environment variables
- ⚠️ Error handling for network failures and invalid responses
- 🎨 Modern desktop interface using CustomTkinter *(Coming Soon)*

---

## 🛠️ Technologies Used

- **Python 3**
- **Requests**
- **CustomTkinter**
- **Pillow**
- **python-dotenv**
- **OpenWeatherMap API**
- **IP-API**

---

## 📂 Project Structure

```text
Weather-Forcast/
│
├── main.py
├── weather.py
├── location.py
├── requirements.txt
├── .gitignore
├── README.md
├── .env                # Ignored by Git
└── assets/
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Weather-Forcast.git
cd Weather-Forcast
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENWEATHER_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://openweathermap.org/api

---

### 5. Run the Application

```bash
python main.py
```

---

## 📸 Current Output

```text
Detecting your location...
Location Found: Kolkata, India

Weather Details
----------------
City: Kolkata
Temperature: 30.8 °C
Feels Like: 35.1 °C
Humidity: 80 %
Condition: Broken Clouds
Wind Speed: 2.3 m/s
```

---

## 🔮 Future Improvements

- [ ] Modern GUI using CustomTkinter
- [ ] Weather icons
- [ ] Search weather by city
- [ ] 5-day weather forecast
- [ ] Automatic weather refresh
- [ ] Air Quality Index (AQI)
- [ ] Dark/Light mode toggle
- [ ] Export as standalone executable (.exe)

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Soumallya Sarkar**

Engineering Student at IIIT Kottayam

If you found this project helpful, consider giving it a ⭐ on GitHub!
