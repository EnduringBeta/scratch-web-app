"""
Run the API to manage data CRUD requests

Use via `python3 app.py` or `flask run`
"""

from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)

animals = [
    {"id": 1, "name": "Lorelei", "type": "hamster"},
    {"id": 2, "name": "Woo", "type": "hamster"},
    {"id": 3, "name": "Demi", "type": "dog"},
]

def _find_next_id():
    return max(animal["id"] for animal in animals) + 1

@app.get("/animals")
def get_animals():
    # Flask doesn’t automatically convert lists to JSON
    return jsonify(animals)

@app.post("/animals")
def add_animal():
    if request.is_json:
        animal = request.get_json()
        animal["id"] = _find_next_id()
        animals.append(animal)
        return animal, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    app.run()
