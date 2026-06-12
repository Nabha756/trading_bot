from bot.client import BinanceClient
from bot.orders import place_market_order

client = BinanceClient().get_client()

response = place_market_order(
    client,
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001
)

print(response)