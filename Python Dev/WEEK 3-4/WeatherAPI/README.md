# Live Weather Checker (OpenWeatherMap API)

## Overview

This is a simple command-line Python application that fetches real-time weather data using the OpenWeatherMap API. Users can enter any city, and the program will return the current weather description and temperature in Celsius. The loop continues until the user types `"exit"`.

Now updated to use a `.env` file for secure API key handling.

---

## Key Features

- Retrieves live weather data from OpenWeatherMap
- Displays temperature and conditions in a clear format
- Input loop allows checking multiple cities
- Uses metric units by default (Celsius)
- Graceful handling of invalid inputs and API errors
- Uses `.env` file to keep your API key secure (GitHub-safe)

---

## What I Learned

This project helped me understand how to:

- Make GET requests using the `requests` library
- Securely manage API keys with `python-dotenv`
- Handle JSON API responses and extract values
- Build a clean user input loop
- Work with real-time external data safely

---

## How to Run

1. **Install the required libraries**:

```bash
pip install -r requirements.txt
