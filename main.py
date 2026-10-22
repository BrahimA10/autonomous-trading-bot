import os
from datetime import datetime


class GridStrategy:
    def __init__(self, symbol, grid_step, lower_bound, upper_bound, quote_quantity):
        self.symbol = symbol
        self.grid_step = grid_step
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.quote_quantity = quote_quantity
        self.last_signal = None

    def reset_signal(self):
        self.last_signal = None

    def paper_run(self, price, exchange, logger):
        logger.info(f"Paper mode check at {price} for {self.symbol}")

        if self.lower_bound and price <= self.lower_bound:
            logger.warning(f"Lower bound reached: {price}")
            self.last_signal = "LOWER_BOUND"

        if self.upper_bound and price >= self.upper_bound:
            logger.warning(f"Upper bound reached: {price}")
            self.last_signal = "UPPER_BOUND"

        if self.last_signal is None:
            logger.info(f"No trigger. Price is in range: {price}")

    def live_run(self, price, exchange, logger):
        logger.info(f"Live mode check at {price} for {self.symbol}")

        if self.lower_bound and price <= self.lower_bound:
            logger.warning(f"Lower bound triggered at {price}")
            self.last_signal = "LOWER_BOUND"

        if self.upper_bound and price >= self.upper_bound:
            logger.warning(f"Upper bound triggered at {price}")
            self.last_signal = "UPPER_BOUND"

        if self.last_signal is None:
            logger.info(f"No action. Price remains stable: {price}")
