
import time
from binance.client import Client
from flask import Flask, request, render_template

# Chaves da Binance (API REAL liberada apenas para IP 216.24.57.1)
API_KEY = "k31TkNKee94QVeQ3Bg3gJbkQ9lCbXYc270t3bPsHQZz66zreCsDCPAIujbWY7hT8"
API_SECRET = "ZYx8fgSkwMEgVqKJbSeMNK4r0ewVp0JUPoo8bEpvcEO6spabHVvuhGtrrhGWXU83"

client = Client(API_KEY, API_SECRET)

app = Flask(__name__)

@app.route("/")
def dashboard():
    account_info = client.get_account()
    return render_template("dashboard.html", balances=account_info['balances'])

@app.route("/start", methods=["POST"])
def start_trade():
    mode = request.form.get("modo", "conservador")
    try:
        if mode == "conservador":
            quantity = 0.0002
        elif mode == "moderado":
            quantity = 0.0004
        elif mode == "agressivo":
            quantity = 0.0006
        else:
            return "Modo inválido", 400

        order = client.order_market_buy(
            symbol='BTCUSDT',
            quantity=quantity
        )
        return f"Ordem executada com sucesso: {order}"
    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
