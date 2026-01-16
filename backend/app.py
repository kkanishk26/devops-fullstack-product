from flask import Flask, jsonify
from flask_cors import CORS
import socket
import datetime

app = Flask(__name__)
CORS(app)   # <-- This line is what allows frontend to connect

@app.route("/")
def home():
    return jsonify({
        "service": "DevOps Product Backend",
        "status": "running",
        "hostname": socket.gethostname(),
        "time": str(datetime.datetime.now())
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
