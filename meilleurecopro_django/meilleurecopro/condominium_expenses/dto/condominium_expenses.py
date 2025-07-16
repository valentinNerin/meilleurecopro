class CondominiumExpenses:

    def __init__(self, mean: float, quantile_10: float, quantile_90: float):
        self.mean = mean
        self.quantile_10 = quantile_10
        self.quantile_90 = quantile_90