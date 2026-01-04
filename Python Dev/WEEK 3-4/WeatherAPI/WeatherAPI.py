"""
Live Weather Checker using OpenWeatherMap API

This script:
- Prompts user to enter a city name
- Fetches current weather data via OpenWeatherMap API
- Displays temperature and weather conditions
- Continues until user types 'exit'
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Securely load the API key from environment
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetches weather data for a given city using OpenWeatherMap API.

    :param city: City name (string)
    :return: Dictionary with weather description and temperature, or None on error
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return {
                "weather": weather,
                "temp": temperature
            }
        else:
            return None
    except Exception as e:
        print("Error contacting weather API:", e)
        return None

def main():
    """
    Main loop for user interaction and weather display.
    """
    print("Welcome to the Live Weather Checker!")
    while True:
        city = input("Enter your city (or type 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Exiting weather checker.")
            break

        result = get_weather(city)
        if result:
            print(f"Weather in {city.title()}: {result['weather']}")
            print(f"Temperature: {result['temp']}°C\n")
        else:
            print("City not found or API error.\n")

if __name__ == "__main__":
    main()
