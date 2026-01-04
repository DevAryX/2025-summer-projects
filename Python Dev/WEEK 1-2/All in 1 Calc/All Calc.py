def bmi_calculator():
    """
    Calculates Body Mass Index (BMI) based on user-provided weight and height.
    BMI = weight (kg) / height^2 (m^2)
    """
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi = weight / (height * height)
        print("Your BMI is: " + str(round(bmi, 2)))
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def tip_calculator():
    """
    Calculates the tip amount and total bill including tip.
    """
    try:
        bill_amount = float(input("Total bill amount: "))
        tip_percentage = float(input("Tip percentage (e.g. 15): "))
        tip_amount = bill_amount * (tip_percentage / 100)
        total_with_tip = bill_amount + tip_amount
        print("Tip: " + str(round(tip_amount, 2)))
        print("Total with tip: " + str(round(total_with_tip, 2)))
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def currency_converter():
    """
    Converts an amount from GBP to another currency using a provided conversion rate.
    """
    try:
        amount_gbp = float(input("Amount in GBP: "))
        conversion_rate = float(input("Conversion rate to your currency: "))
        converted_amount = amount_gbp * conversion_rate
        print("Converted amount: " + str(round(converted_amount, 2)))
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def age_in_days():
    """
    Estimates age in days by multiplying user-provided age in years by 365.
    (Does not account for leap years.)
    """
    try:
        age_years = int(input("Enter your age in years: "))
        days_alive = age_years * 365
        print("You are about " + str(days_alive) + " days old.")
    except ValueError:
        print("Please enter a valid number for age.")

def show_menu():
    """
    Displays the main menu with tool options.
    """
    print("\n--- Python Multi-Tool Calculator ---")
    print("1. BMI Calculator")
    print("2. Tip Calculator")
    print("3. Currency Converter")
    print("4. Age in Days Calculator")
    print("5. Exit")

# --- Main Program Loop ---
# Continuously show the menu until the user chooses to exit
while True:
    show_menu()
    user_choice = input("Enter your choice (1 to 5): ")

    if user_choice == "1":
        bmi_calculator()
    elif user_choice == "2":
        tip_calculator()
    elif user_choice == "3":
        currency_converter()
    elif user_choice == "4":
        age_in_days()
    elif user_choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
