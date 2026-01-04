"""
User Age Predictor Script

This short script:
1. Asks the user for their name and age.
2. Calculates their age in 10 years.
3. Displays a personalized message with the result.
"""

# Ask the user for their name
user_name = input("What is your name? ")

# Ask the user for their age and convert it to an integer
try:
    user_age = int(input("What is your age? "))
except ValueError:
    print("Please enter a valid number for age.")
    exit()

# Calculate the user's age after 10 years
age_in_10_years = user_age + 10

# Display a personalized message
print("Hey " + user_name + ", you'll be " + str(age_in_10_years) + " in 10 years time.")
