"""
Urdu Quote Bot – Display Random Urdu Quotes by Category

Features:
- Loads quotes from local JSON files per category
- Shows random quotes in Urdu with transliteration and English translation
- Supports romantic, wisdom, and life categories
"""

import json
import random
import os

def load_quotes(category):
    """
    Loads quotes from a JSON file for the given category.
    
    :param category: one of ['romantic', 'wisdom', 'life']
    :return: list of quotes or empty list if error occurs
    """
    filename = f"quotes_{category}.json"
    if not os.path.exists(filename):
        print("Quote file not found for category:", category)
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Error loading quotes:", e)
        return []

def get_random_quote(quotes):
    """
    Returns a random quote dictionary from the list.
    
    :param quotes: list of quote dictionaries
    :return: one quote (dict) or None if list is empty
    """
    if not quotes:
        return None
    return random.choice(quotes)

def main():
    """
    Main interactive loop: prompts user to select a category,
    then displays a random quote from that category.
    """
    categories = {
        "1": "romantic",
        "2": "wisdom",
        "3": "life",
        "4": "exit"
    }

    # Pre-load all quote files into memory
    quote_bank = {}
    for key in ["romantic", "wisdom", "life"]:
        quote_bank[key] = load_quotes(key)

    print("📜 Urdu Quote Bot")
    while True:
        print("\nChoose a category:")
        print("1. Romantic Urdu Quotes")
        print("2. Wisdom Urdu Quotes")
        print("3. Life Urdu Quotes")
        print("4. Exit")
        choice = input("Enter 1, 2, 3 or 4: ").strip()

        if choice == "4":
            print("Goodbye.")
            break

        category = categories.get(choice)
        if not category:
            print("Invalid option. Please choose 1–4.")
            continue

        quote = get_random_quote(quote_bank[category])
        if quote:
            print("\n📖 Urdu: " + quote.get("urdu", "N/A"))
            print("📜 Transliteration: " + quote.get("transliteration", "N/A"))
            print("💬 Translation: " + quote.get("translation", "N/A") + "\n")
        else:
            print("No quotes available in that category.\n")

if __name__ == "__main__":
    main()
