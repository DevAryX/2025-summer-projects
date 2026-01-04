# MoodBot Pro – Sentiment-Based Chatbot with Logging

## Overview

MoodBot Pro is an intelligent chatbot that responds to the user's emotional state based on natural language input. It uses both keyword matching and sentiment analysis (via TextBlob) to detect mood and reply accordingly. The bot also gives the option to save conversations with timestamps, making it feel more like a journaling assistant.

## Key Features

- Dual mood detection: keywords + sentiment score
- Personalized response based on emotional state
- Option to save the conversation to a log file with timestamp
- Uses `TextBlob` for natural language sentiment detection
- Clean terminal interface with clear instructions

## What I Learned

This project was a step up from basic CLI tools. I learned how to:

- Use third-party libraries like `textblob` for sentiment analysis
- Write mood-detection logic using both keywords and polarity scores
- Handle file writing and timestamps for saving conversations
- Build logic that feels more natural and less scripted
- Structure a larger Python script with clean, reusable functions

It also gave me more confidence in making small AI-like features using simple Python tools.

## How to Run

Install the required dependency if you haven’t already:

```bash
pip install textblob
