from binance.enums import *
from bot.logging_config import logger


def place_market_order(client, symbol, side, quantity):

    request_data = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
    }

    logger.info(f"ORDER REQUEST: {request_data}")

    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity,
        )

        logger.info(f"ORDER RESPONSE: {response}")

        return response

    except Exception as e:
        logger.error(f"ORDER ERROR: {str(e)}")
        raise


def place_limit_order(client, symbol, side, quantity, price):

    request_data = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
    }

    logger.info(f"ORDER REQUEST: {request_data}")

    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        logger.info(f"ORDER RESPONSE: {response}")

        return response

    except Exception as e:
        logger.error(f"ORDER ERROR: {str(e)}")
        raise