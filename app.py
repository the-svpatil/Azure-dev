
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Flask server is running successfully."

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Server is healthy"
    })

@app.route("/api")
def api():
    return jsonify({
        "message": "Python Flask API is working!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)