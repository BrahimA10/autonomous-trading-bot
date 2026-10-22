import hashlib
import hmac
import time
from urllib.parse import urlencode

import requests


class BinanceClient:
    def __init__(self, api_key="", api_secret="", testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://testnet.binance.vision" if testnet else "https://api.binance.com"

    def _sign(self, params):
        query = urlencode(params)
        return hmac.new(self.api_secret.encode(), query.encode(), hashlib.sha256).hexdigest()

    def get_ticker(self, symbol):
        response = requests.get(
            f"{self.base_url}/api/v3/ticker/price",
            params={"symbol": symbol},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def get_account(self):
        if not self.api_key or not self.api_secret:
            raise RuntimeError("API_KEY and API_SECRET are required to fetch account information.")

        params = {
            "timestamp": int(time.time() * 1000),
            "recvWindow": 60000,
        }
        params["signature"] = self._sign(params)
        headers = {"X-MAX-APIKEY": self.api_key}

        response = requests.get(
            f"{self.base_url}/api/v3/account",
            params=params,
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def get_balance(self, asset):
        data = self.get_account()
        for item in data.get("balances", []):
            if item["asset"] == asset:
                return float(item["free"])
        return 0.0

    def place_order(self, side, symbol, quantity, price=None):
        if not self.api_key or not self.api_secret:
            raise RuntimeError("API_KEY and API_SECRET are required to send orders.")

        params = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT" if price else "MARKET",
            "quantity": str(quantity),
            "timestamp": int(time.time() * 1000),
            "recvWindow": 60000,
        }

        if price:
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        params["signature"] = self._sign(params)
        headers = {"X-MAX-APIKEY": self.api_key}

        response = requests.post(
            f"{self.base_url}/api/v3/order",
            params=params,
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
