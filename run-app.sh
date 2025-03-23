#!/bin/bash

echo "Starting Scratch Web App..."

# Assuming in proper working directory

# Start MySQL in background
service mysql start && mysql -u root -p$MYSQL_PASSWORD < $REPO_DIR/init.sql

# Activate Python virtual environment, which is assumed to have been set up parallel to repo
. venv/bin/activate

# .env environment variables are set in Python using `load_dotenv`

# Run the app!
#python3 app.py
flask run --host=0.0.0.0 --port=5000

echo "Ending Scratch Web App..."
