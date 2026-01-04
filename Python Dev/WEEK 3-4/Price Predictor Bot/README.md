# House Price Predictor (Linear Regression)

## Overview

This is a machine learning project that predicts house prices based on features like size, number of bedrooms, and age. It uses the `scikit-learn` library to train a linear regression model on housing data, with an interactive CLI for predictions and visualization of results.

## Key Features

- Loads housing data from `housing.csv` (or uses sample data as fallback)
- Trains a linear regression model using scikit-learn
- Calculates model accuracy on a test set
- CLI interface to:
  - Predict house prices based on user input
  - Visualize actual vs predicted prices using a scatter plot

## What I Learned

Through this project, I gained a practical understanding of:

- Preparing data for training using `pandas` and `train_test_split`
- Training and evaluating a regression model
- Making predictions based on user input
- Visualizing model performance using `matplotlib`
- Structuring a machine learning project for CLI use

It gave me hands-on experience combining multiple tools and concepts in a real-world use case.

## How to Run

Install the required libraries:

```bash
pip install pandas scikit-learn matplotlib
