from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()


class BinanceClient:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            testnet=True
        )

    def get_client(self):
        return self.client