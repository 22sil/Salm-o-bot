
from flask import Flask, jsonify, request
import os
from binance.client import Client

app = Flask(__name__)

API_KEY = "k31TkNKee94QVeQ3Bg3gJbkQ9lCbXYc270t3bPsHQZz66zreCsDCPAIujbWY7hT8"
API_SECRET = "ZYx8fgSkwMEgVqKJbSeMNK4r0ewVp0JUPoo8bEpvcEO6spabHVvuhGtrrhGWXU83"
ALLOWED_IP = "216.24.57.1"

client = Client(API_KEY, API_SECRET)

@app.route("/api/status")
def status():
    user_ip = request.remote_addr
    if user_ip != ALLOWED_IP:
        return jsonify({"error": "Acesso negado"}), 403
    try:
        account = client.get_account()
        return jsonify(account)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
