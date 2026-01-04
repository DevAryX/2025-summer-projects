"""
Simple OOP Example in Python

This script defines a Person class and:
1. Takes user input for name, age, and mood.
2. Creates a Person object.
3. Calls methods to greet and predict the user's age in 10 years.
"""

class Person:
    def __init__(self, name, age, mood):
        """
        Initializes a new Person object.
        
        :param name: User's name (string)
        :param age: User's current age (int)
        :param mood: User's current mood (string)
        """
        self.name = name
        self.age = age
        self.mood = mood

    def greet(self):
        """
        Greets the user by name and mentions their mood.
        """
        print("Hello, my name is " + self.name + " and I'm feeling " + self.mood + ".")

    def predict_future(self):
        """
        Predicts and displays the user's age in 10 years.
        """
        future_age = self.age + 10
        print("In 10 years, I’ll be " + str(future_age) + " years old.")

# --- User Input Section ---

# Get user's name
user_name = input("Enter your name: ")

# Get user's age
user_age = input("Enter your age: ")

# Get user's mood
user_mood = input("How are you feeling today? ")

# Convert age input to integer (with basic validation)
try:
    user_age = int(user_age)
except ValueError:
    print("Invalid age entered. Please enter a number.")
    exit()

# --- Create Person object and use class methods ---

# Create a new instance of Person using user input
person1 = Person(user_name, user_age, user_mood)

# Output user's greeting and future age
print("\n--- Your Info ---")
person1.greet()
person1.predict_future()
