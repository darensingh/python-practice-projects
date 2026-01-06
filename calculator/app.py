from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        # Evaluate safely in Python
        result = eval(expression)
    except Exception:
        result = "Error"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)