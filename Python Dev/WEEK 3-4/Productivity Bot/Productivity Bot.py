"""
Productivity Bot – Your Personal Focus and Motivation Assistant

Features:
1. Focus timer
2. Live motivational quote (via ZenQuotes API)
3. Simple reminder system (in-memory)
"""

import time
import requests

# Global list to store user reminders
reminders = []

def greet_user():
    """
    Greets the user and asks for their name.
    :return: user's name (string)
    """
    name = input("Hi! I am THE Productivity Bot. What's your name? ")
    print("Nice to meet you, " + name + "! Let's get you focused and productive.")
    return name

def focus_timer():
    """
    Asks the user how many minutes they'd like to focus, then starts a simulated timer.
    """
    try:
        mins = int(input("How many minutes would you like to focus? "))
        print(f"Great! Starting your {mins}-minute focus timer now. Stay focused!")
        time.sleep(2)  # Simulated wait for demo. Replace with: time.sleep(mins * 60) for real use.
        print("Time's up! You did great!")
    except ValueError:
        print("Please enter a valid number.")

def get_live_quote():
    """
    Fetches and displays a motivational quote from the ZenQuotes API.
    """
    print("Getting a motivational quote for you...")
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            print(f'Quote: "{quote}" – {author}')
        else:
            print("Couldn't get a quote right now. Please try again later.")
    except Exception as e:
        print("Oops! Something went wrong while getting the quote.")

def add_reminder():
    """
    Adds a task to the reminders list.
    """
    task = input("What would you like to be reminded about? ")
    reminders.append(task)
    print("Got it! I've added that to your list of reminders.")

def show_reminders():
    """
    Displays all saved reminders.
    """
    if not reminders:
        print("You don't have any reminders yet.")
    else:
        print("Here's what's on your reminder list:")
        for index, task in enumerate(reminders, start=1):
            print(f"{index}. {task}")

def main():
    """
    Main command loop for interacting with the bot.
    """
    name = greet_user()

    while True:
        print("\nWhat can I help you with today?")
        print("1. Set a focus timer")
        print("2. Get a motivational quote")
        print("3. Add a reminder")
        print("4. Show my reminders")
        print("5. Exit")

        choice = input("Enter a number or type a command: ").strip().lower()

        if choice in ["1", "focus", "timer"]:
            focus_timer()
        elif choice in ["2", "quote", "motivate"]:
            get_live_quote()
        elif choice in ["3", "reminder", "add"]:
            add_reminder()
        elif choice in ["4", "show", "reminders"]:
            show_reminders()
        elif choice in ["5", "exit", "bye"]:
            print("Goodbye " + name + "! Keep up the great work!")
            break
        else:
            print("Hmm, I didn't get that. Please try choosing from the list.")

# Entry point
if __name__ == "__main__":
    main()
