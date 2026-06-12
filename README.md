# 📈 Binance Futures Testnet Trading Bot (Python CLI)

## 📌 Description
A Python-based command-line trading bot that connects to the **Binance USDT-M Futures Testnet** and allows users to place Market and Limit orders with proper validation, structured logging, and robust error handling.

This project demonstrates real-world API integration, modular backend design, and production-style CLI tooling.

---

## 🚀 Features
- Place **Market Orders** (BUY/SELL)
- Place **Limit Orders** (BUY/SELL)
- Binance Futures Testnet integration
- Command Line Interface (CLI) using `argparse`
- Strong input validation for all parameters
- Structured logging (requests, responses, errors)
- Graceful exception handling for API failures
- Modular and scalable architecture

---

## 🧰 Tech Stack
- Python 3.x
- python-binance
- argparse
- logging module
- Binance Futures Testnet API

---

## 📁 Project Structure

```bash
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py              # Binance API wrapper
│   ├── orders.py              # Order execution logic
│   ├── validators.py          # Input validation
│   └── logging_config.py      # Logging setup
│
├── logs/
│   └── trading_bot.log        # Generated logs
│
├── cli.py                     # CLI entry point
├── check_account.py
├── test_connection.py
├── test_order.py
├── test_logger.py
│
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd trading_bot
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

⚠️ Never push `.env` to GitHub.

---

## ▶️ How to Run

### 📊 Market Order Example
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 📉 Limit Order Example
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

---

## 📜 Logging

All logs are stored in:

```bash
logs/trading_bot.log
```

### Logs include:
- API request payloads
- API responses
- Errors and exceptions

---

## ⚠️ Error Handling
- Invalid CLI arguments handled via validation layer
- API errors handled gracefully
- Network failures handled using try/except blocks
- Safe failure without crashing the bot

---

## 📦 Sample Order Response

```text
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
```

---

## 🧠 Architecture Overview
- `cli.py` → Entry point for user commands
- `validators.py` → Input validation layer
- `client.py` → Binance API communication
- `orders.py` → Order execution logic
- `logging_config.py` → Centralized logging system

---

## 📌 Notes
- Works only with Binance Futures Testnet
- No real funds are used
- Requires valid API keys from Binance Testnet
- `.env` file must remain private

---

## 📊 Project Status
- ✅ Market Orders Working
- ✅ Limit Orders Working
- ✅ CLI Interface Working
- ✅ Logging Implemented
- ✅ Validation Implemented
- ✅ Error Handling Implemented
- ✅ Testnet Integration Complete

---

## 👤 Author
Built by **Nabha Kulkarni** as part of a Python Developer internship project.
