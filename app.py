"""
Run the API to manage data CRUD requests

Use via `python3 app.py` or `flask run`
"""

import os
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

MYSQL_DATABASE=os.environ.get('MYSQL_DATABASE', 'mydatabase')
MYSQL_USER=os.environ.get('MYSQL_USER', 'myuser')
MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD', 'insecure')

table_animals='animals'

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': MYSQL_DATABASE
}

SUPPLY_INIT_DATA=True

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

init_animals = [
    {"name": "Lexi", "type": "hamster"},
    {"name": "Lorelei", "type": "hamster"},
    {"name": "Woo", "type": "hamster"},
    {"name": "Demi", "type": "dog"},
]

def _initialize_db(supply_init_data = False):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create database if it doesn't exist
        query_database = f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}"
        cursor.execute(query_database)
        conn.commit()

        # Create animals table if it doesn't exist
        query_animals = f"""CREATE TABLE IF NOT EXISTS {table_animals} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            type VARCHAR(255) NOT NULL
        )"""
        cursor.execute(query_animals)

        if supply_init_data:
            query_check_empty = f"SELECT COUNT(*) FROM {table_animals}"
            cursor.execute(query_check_empty)
            result = cursor.fetchone()

            # Only insert data during init if no data present
            if result[0] == 0:
                query_add_animals = f"INSERT INTO {table_animals} (name, type) VALUES (%s, %s)"
                cursor.executemany(query_add_animals, init_animals)
                print('Added initial animals!')

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise e

@app.route('/')
def index():
    return 'No animals here... Try "/animals"!'

@app.get("/animals")
def get_animals():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT * FROM {table_animals}"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        # Flask doesn’t automatically convert lists to JSON
        return jsonify(rows)
    except Exception as e:
        print(f"Error getting animals: {e}")
        raise e

@app.post("/animals")
def add_animal():
    if request.is_json:
        animal = request.get_json()
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {table_animals} (name, type) VALUES (%s, %s)"
            cursor.execute(query, animal['name'], animal['type'])
            conn.commit()
            conn.close()

            return jsonify({'message': 'Animal added successfully!'}), 201
        except Exception as e:
            print(f"Error adding animal: {e}")
            raise e
    return {"error": "Request must be JSON"}, 415

# TODOROSS: PUT, DELETE

if __name__ == "__main__":
    with app.app_context():
        _initialize_db(SUPPLY_INIT_DATA)
    app.run()
