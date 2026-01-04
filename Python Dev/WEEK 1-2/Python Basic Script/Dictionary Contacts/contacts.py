"""
Simple Contact Book in Python
Allows users to add, search, and view contacts using a dictionary-based system.
"""

# Empty dictionary to store contact name and number
contacts = {}

def add_contact(name, number):
    """
    Adds a contact to the contacts dictionary.
    
    :param name: Name of the contact (string)
    :param number: Phone number of the contact (string or int)
    """
    contacts[name] = number
    print(f"{name} added successfully!")

def search_contact(name):
    """
    Searches for a contact by name and displays the phone number if found.
    
    :param name: Name of the contact to search for (string)
    """
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"No contact found for '{name}'.")

def show_all_contacts():
    """
    Displays all saved contacts in the dictionary.
    """
    if not contacts:
        print("No contacts saved yet.")
    else:
        print("Your Contacts:")
        for name, number in contacts.items():
            print(f"- {name}: {number}")

# --- Main Menu Loop ---
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Exit")
    
    choice = input("Choose an option (1–4): ")

    if choice == "1":
        # Collect user input and add new contact
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)

    elif choice == "2":
        # Collect user input and search contact
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "3":
        # Show all saved contacts
        show_all_contacts()

    elif choice == "4":
        # Exit the loop and program
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 4.")
