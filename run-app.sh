#!/bin/bash

echo "Starting Scratch Web App..."

# Assuming in proper working directory

# Start MySQL in background
service mysql start

# .env environment variables are set in Python using `load_dotenv`

# Run the app!
#python3 app.py
flask run

echo "Ending Scratch Web App..."
