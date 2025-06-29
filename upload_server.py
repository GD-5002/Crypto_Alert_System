# upload_server.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Crypto Alert Upload API is running."

@app.route("/upload", methods=["POST"])
def upload_config():
    try:
        config = request.get_json()
        with open("alert_config.json", "w") as f:
            json.dump(config, f, indent=2)
        print("✅ alert_config.json updated via Streamlit UI")
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
