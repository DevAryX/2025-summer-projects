# Predictive Mood Chatbot

## Overview

This is a simple Python chatbot that asks the user for their name and mood, then gives a response based on how they're feeling. It also offers to save the interaction to a local file. The chatbot uses predefined categories like happy, sad, bored, and angry to give supportive or encouraging responses.

## Key Features

- Responds based on user's stated mood
- Personalized greetings using the user's name
- Uses a dictionary to manage mood-based responses
- Offers the option to save each conversation
- Appends saved chats to a file called `chat_log.txt`

## What I Learned

This project helped reinforce my understanding of:

- Using dictionaries to structure response logic
- Handling user input with `.lower()` to make it case-insensitive
- Creating a friendly chatbot that reacts based on emotion
- Reading from and writing to local files for chat logging
- Using conditionals to branch logic in user flow

It also gave me more confidence in building simple conversational tools with some memory.

## How to Run

Make sure Python is installed, then run:

```bash
python predictive_chatbot.py
