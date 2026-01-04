"""
Simple Predictive Chatbot with Mood-Based Responses

This script:
- Greets the user and asks how they feel
- Provides tailored responses based on predefined moods
- Optionally saves the mood to a chat log file
"""

# Predefined responses based on mood
responses = {
    "happy": [
        "That's awesome! Keep the good energy going!",
        "Love that for you! What made you happy today?"
    ],
    "sad": [
        "I'm here for you. Try doing something you enjoy.",
        "It's okay to feel sad. Maybe listen to music or talk to someone."
    ],
    "tired": [
        "Sounds like you need a break or a nap!",
        "Rest is important. Try relaxing for a while."
    ],
    "bored": [
        "How about reading, coding, or going for a walk?",
        "Try starting a mini project or watching a documentary."
    ],
    "angry": [
        "Take a deep breath. Want to talk about it?",
        "Try writing it out or stepping away for a bit."
    ]
}

# --- User Input Section ---

print("Hi, I'm your mood buddy.")
user_name = input("What's your name? ")
user_mood = input("How are you feeling today? (e.g., happy, sad, tired, bored, angry): ").lower()

# --- Respond to Mood ---
if user_mood in responses:
    print(f"Hi {user_name}, {responses[user_mood][0]}")
else:
    print(f"Hi {user_name}, I'm not sure how to respond to that. But I'm always here to chat!")

# --- Optional Chat Saving ---
save_choice = input("Do you want to save this chat? (yes/no): ").lower()
if save_choice == "yes":
    try:
        with open("chat_log.txt", "a") as file:
            file.write(f"{user_name} felt {user_mood}\n")
        print("Chat saved to 'chat_log.txt'")
    except Exception as e:
        print("Error saving chat:", e)
