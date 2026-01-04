"""
Simple Mood-Based Chatbot
This script interacts with the user by:
1. Asking for their name
2. Asking how they're feeling
3. Responding with an appropriate message
"""

# Ask for the user's name
user_name = input("Hello! What’s your name? ")
print("Nice to meet you, " + user_name + "!")

# Ask how the user is feeling today
user_mood = input("How are you feeling today? (happy/sad/stressed/etc.): ")

# Respond with an appropriate message based on mood
if user_mood.lower() == "happy":
    print("That’s awesome! Keep spreading good vibes.")
elif user_mood.lower() == "sad":
    print("Sorry to hear that. I’m here if you ever need to talk.")
elif user_mood.lower() == "stressed":
    print("Take a deep breath. Maybe try a short walk or a quick break.")
else:
    print("Thanks for sharing. Everyone has ups and downs. You’ve got this!")

# Personalised follow-up message
print(user_name + ", I hear you’re feeling " + user_mood + ". Remember to take care of yourself!")
