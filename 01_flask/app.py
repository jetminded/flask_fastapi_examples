from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

character = {
    "name": "Arin",
    "class": "Rogue",
    "hp": 20
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/character", methods=["GET"])
def get_character():
    return jsonify(character)

@app.route("/roll", methods=["GET"])
def roll_dice():
    sides = int(request.args.get("sides", 20))
    result = random.randint(1, sides)
    return jsonify({"roll": result, "sides": sides})

@app.route("/damage", methods=["POST"])
def take_damage():
    data = request.json
    dmg = data.get("damage", 0)
    character["hp"] -= dmg
    return jsonify({"hp": character["hp"]})

if __name__ == "__main__":
    app.run(debug=True)