class RiskManager:
    def __init__(self, max_daily_loss=0.05, max_position_ratio=0.30):
        self.max_daily_loss = max_daily_loss
        self.max_position_ratio = max_position_ratio
        self.daily_loss = 0.0

    def should_stop(self):
        return self.daily_loss >= self.max_daily_loss
