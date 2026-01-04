"""
Weather Predictor – Predicts Tomorrow's Average Temperature

This script:
- Fetches the past 7 days of average temperatures using WeatherAPI
- Trains a Linear Regression model on the data
- Predicts the next day's average temperature
- Visualizes the trend using matplotlib
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# Replace with your WeatherAPI key
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Number of past days to include in the prediction
DAYS = 7

def fetch_weather_data(city, days):
    """
    Pulls average daily temperatures for the past 'days' days for a given city.

    :param city: city name (string)
    :param days: number of past days to fetch (int)
    :return: DataFrame with columns ['date', 'temp_c'] or None on failure
    """
    weather_data = []

    for i in range(days):
        date = (datetime.datetime.now() - datetime.timedelta(days=i + 1)).strftime("%Y-%m-%d")
        url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={city}&dt={date}"

        response = requests.get(url)

        if response.status_code == 200:
            try:
                data = response.json()
                avg_temp = data['forecast']['forecastday'][0]['day']['avgtemp_c']
                weather_data.append((date, avg_temp))
            except (KeyError, IndexError):
                # If response is malformed or missing expected keys
                continue
        else:
            return None  # Bad request or city not found

    if not weather_data:
        return None

    return pd.DataFrame(weather_data, columns=["date", "temp_c"]).sort_values("date")

def run_weather_prediction():
    """
    Prompts user for a city, performs weather data fetching, prediction,
    and visualizes the forecast using a linear regression model.
    """
    while True:
        city_input = input("Enter a city name: ").strip()
        city = city_input.title()

        print(f"Getting weather data for {city}...")

        df = fetch_weather_data(city, DAYS)
        if df is not None:
            break
        else:
            print("Could not fetch data. Please enter a valid city.")

    # Add numeric day index
    df["day_num"] = range(1, len(df) + 1)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(df[["day_num"]], df["temp_c"])

    # Predict temperature for the next day
    next_day = pd.DataFrame([[DAYS + 1]], columns=["day_num"])
    predicted_temp = model.predict(next_day)[0]

    # Plot actual and predicted values
    plt.plot(df["day_num"], df["temp_c"], marker='o', label="Past Temperatures")
    plt.plot(DAYS + 1, predicted_temp, marker='x', color='red', label=f"Predicted: {predicted_temp:.2f}°C")

    plt.xlabel("Day Number")
    plt.ylabel("Average Temperature (°C)")
    plt.title(f"{city} – Avg Temp Over Last {DAYS} Days & Tomorrow's Forecast")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f"\nPredicted average temperature for tomorrow in {city}: {predicted_temp:.2f}°C")

def main():
    """
    Entry point for the weather prediction app.
    """
    print("Welcome to the Simple Weather Forecast Program")
    while True:
        run_weather_prediction()
        again = input("Would you like to check another city? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye Habibi.")
            break

# Start the program
if __name__ == "__main__":
    main()
