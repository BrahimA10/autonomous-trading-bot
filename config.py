import os
from dataclasses import dataclass

@dataclass
class Settings:
    symbol: str = "BTCUSDT"
    interval_seconds: int = 30
    mode: str = "paper"
    testnet: bool = True
    api_key: str = ""
    api_secret: str = ""
    grid_step: float = 150.0
    lower_bound: float = 0.0
    upper_bound: float = 0.0
    quote_quantity: float = 20.0
    max_daily_loss: float = 0.05
    max_position_ratio: float = 0.30
    log_file: str = "bot.log"

    def __post_init__(self):
        self.api_key = os.getenv("API_KEY", self.api_key)
        self.api_secret = os.getenv("API_SECRET", self.api_secret)
        self.symbol = os.getenv("SYMBOL", self.symbol).upper()
        self.mode = os.getenv("MODE", self.mode).lower()
        self.testnet = os.getenv("TESTNET", "true").lower() == "true"
        self.interval_seconds = int(os.getenv("INTERVAL_SECONDS", self.interval_seconds))
        self.grid_step = float(os.getenv("GRID_STEP", self.grid_step))
        self.lower_bound = float(os.getenv("LOWER_BOUND", self.lower_bound))
        self.upper_bound = float(os.getenv("UPPER_BOUND", self.upper_bound))
        self.quote_quantity = float(os.getenv("QUOTE_QUANTITY", self.quote_quantity))
        self.max_daily_loss = float(os.getenv("MAX_DAILY_LOSS", self.max_daily_loss))
        self.max_position_ratio = float(os.getenv("MAX_POSITION_RATIO", self.max_position_ratio))
        self.log_file = os.getenv("LOG_FILE", self.log_file)
