"""
Joke Bot using JokeAPI

This script allows a user to:
- Request a random joke by typing 'joke'
- Exit the program by typing 'quit'
- Uses the JokeAPI (https://jokeapi.dev) to fetch jokes via HTTP
"""

import requests

print("Welcome to the Joke Bot!")
print("Type 'joke' to hear one, or 'quit' to exit.\n")

# --- Main Interaction Loop ---
while True:
    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Bot: Bye!")
        break

    elif user_input == "joke":
        try:
            # Fetch a random single-type joke from the JokeAPI
            response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
            data = response.json()

            # Display the joke
            print("Bot: " + data["joke"])
        except Exception as e:
            print("Bot: Couldn't fetch a joke right now.")
    
    else:
        print("Bot: Type 'joke' to get a laugh!")
