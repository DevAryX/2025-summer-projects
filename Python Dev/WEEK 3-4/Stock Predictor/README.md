# Stock Market Predictor (Logistic Regression)

## Overview

This is a Python-based stock analysis tool that uses logistic regression to predict the next day's movement (up or down) for a selected stock. It pulls real-time historical stock data using the `yfinance` library, performs feature engineering, trains a machine learning model, and visualizes the closing price trends using matplotlib.

The project also gives users control over how the data is visualized — daily, every 5 days, monthly, or yearly.

## Key Features

- Choose from a list of 20 major publicly traded stocks (Apple, Tesla, Google, etc.)
- Downloads recent historical stock data via Yahoo Finance
- Generates new features for price change and volatility
- Trains a logistic regression model to predict price direction
- Visualizes resampled closing prices based on chosen interval
- Interactive CLI interface for analyzing multiple stocks in one session

## What I Learned

This project helped me combine machine learning and data visualization in a real-world context. I gained experience with:

- The `yfinance` API for pulling financial data
- Preprocessing data for ML (feature engineering, target labels)
- Training and using logistic regression for binary classification
- Resampling time series data (daily, 5D, monthly, yearly)
- Visualizing financial data using `matplotlib`
- Structuring larger Python programs with multiple user inputs

## How to Run

Install the required libraries:

```bash
pip install yfinance pandas matplotlib scikit-learn
