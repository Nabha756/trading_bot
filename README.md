# Binance Futures Testnet Trading Bot (Python CLI)

## Description
A Python-based command-line trading bot that connects to Binance USDT-M Futures Testnet and allows users to place Market and Limit orders with proper validation, logging, and error handling.

---

## Features
- Place Market Orders on Futures Testnet
- Place Limit Orders on Futures Testnet
- Support for BUY and SELL orders
- Command Line Interface (CLI) using argparse
- Input validation for all parameters
- Structured logging (request, response, error logs)
- Exception handling for API and runtime errors
- Modular architecture (separation of concerns)

---

## Tech Stack
- Python 3.x
- python-binance
- argparse
- logging module
- Binance Futures Testnet API

---

## Project Structure

trading_bot/
├── bot/
│   ├── client.py              # Binance API wrapper
│   ├── orders.py              # Order execution logic
│   ├── validators.py         # Input validation
│   ├── logging_config.py     # Logging configuration
│
├── logs/
│   └── trading_bot.log       # Generated logs (requests/responses/errors)
│
├── cli.py                    # CLI entry point
├── requirements.txt
├── .env                      # API keys (NOT committed)
├── .gitignore
└── README.md

---

## How to Run

### Install dependencies
pip install -r requirements.txt

---

### Market Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

---

### Limit Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000

---

## Logging

All logs are stored in:
logs/trading_bot.log

### Logs include:
- API request payloads
- API responses
- Errors and exceptions

---

## Error Handling
- Invalid CLI inputs handled with validation errors
- API errors handled gracefully
- Network failures handled using try/except blocks

---

## API Response Example

===== ORDER SUMMARY =====
Symbol: BTCUSDT  
Side: BUY  
Type: MARKET  
Quantity: 0.001  

===== ORDER RESPONSE =====
Order ID: 15008165863  
Status: NEW  
Executed Qty: 0.0000  
Avg Price: N/A  

Order submitted successfully

---

## Notes
- Uses Binance Futures Testnet only
- No real money is used
- API keys must be stored in .env file
- .env must NOT be pushed to GitHub

---

## Status
- Market Orders Working
- Limit Orders Working
- CLI Interface Working
- Logging Implemented
- Validation Implemented
- Error Handling Implemented
- Testnet Integration Complete

---

## Author
Built as part of a Python Developer internship assignment:Nabha Kulkarni