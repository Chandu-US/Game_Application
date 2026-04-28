from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "simple-game-secret-key"

@app.route("/")
def home():
    session["number"] = random.randint(1, 5)
    session["attempts"] = 0
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    user_guess = int(data["guess"])

    session["attempts"] += 1
    number = session["number"]

    if user_guess < number:
        message = "Too low! Try again."
    elif user_guess > number:
        message = "Too high! Try again."
    else:
        message = f"Correct! You guessed in {session['attempts']} attempts."

    return jsonify({
        "message": message,
        "attempts": session["attempts"]
    })

if __name__ == "__main__":
    app.run(debug=True)