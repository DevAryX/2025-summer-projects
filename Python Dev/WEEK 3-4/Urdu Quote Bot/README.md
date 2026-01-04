# Urdu Quote Bot – CLI Quote Generator

## Overview

Urdu Quote Bot is a simple command-line application that displays random Urdu quotes based on the category selected by the user. Each quote comes with its original Urdu form, transliteration, and English translation. It supports categories like romantic, wisdom, and life quotes.

The quotes are stored in local JSON files (`quotes_romantic.json`, `quotes_wisdom.json`, etc.), and the app randomly selects one quote per request.

## Key Features

- Choose between romantic, wisdom, or life Urdu quotes
- Displays Urdu script, transliteration, and English meaning
- Uses external JSON files to store quotes
- Clean CLI interface for simple interaction
- Handles missing or invalid files gracefully

## What I Learned

This project gave me hands-on practice with:

- Reading and parsing JSON data in Python
- Using dictionaries to manage categories and quote banks
- Error handling for file access
- CLI design and user interaction flow
- Managing multilingual text data (UTF-8 Urdu content)

It also let me bring language and culture into a coding project, which made it both fun and personally meaningful.

## How to Run

Place the following JSON files in the same directory as the script:

- `quotes_romantic.json`
- `quotes_wisdom.json`
- `quotes_life.json`

Then run the script:

```bash
python urdu_quote_bot.py
