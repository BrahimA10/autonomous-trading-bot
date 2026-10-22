# Autonomous Trading Bot

Local-only trading bot for Binance testnet. It runs on your PC and does not require a VPS.

## What it does
- Fetches live market prices
- Works in paper mode by default
- Uses Binance testnet by default
- Logs to `bot.log`
- Runs automatically in a loop
- Can be extended to real trading later

## Requirements
- Python 3.10+
- Internet connection

## Setup on Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

## Setup on Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python main.py
```

## Default behavior
- `MODE=paper`
- `TESTNET=true`
- `SYMBOL=BTCUSDT`

This means the bot runs safely without real money until you change the mode intentionally.

## Important
This project is for learning and testing. Do not run with real funds unless you understand the logic and risks.
