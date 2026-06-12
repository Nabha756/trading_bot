import argparse

from bot.client import BinanceClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()
try:
    # Validation
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)
    validate_price(args.type, args.price)

    # Client
    client = BinanceClient().get_client()

    # Order execution
    if args.type.upper() == "MARKET":
        response = place_market_order(
            client,
            args.symbol,
            args.side,
            args.quantity,
        )
    else:
        response = place_limit_order(
            client,
            args.symbol,
            args.side,
            args.quantity,
            args.price,
        )

    # Output
    print("\n===== ORDER SUMMARY =====")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.price:
        print(f"Price: {args.price}")

    print("\n===== ORDER RESPONSE =====")
    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")

    print("\nOrder submitted successfully")

except ValueError as ve:
    print(f"Validation Error: {ve}")

except Exception as e:
    print(f"Runtime/Error from API: {e}")