from bot.client import BinanceClient

client = BinanceClient().get_client()

print(client.ping())
print("Connected successfully!")