import pandas as pd

def moving_average_forecast(series: pd.Series, window: int = 3, steps: int = 6):
    if series.isna().all():
        return []
    s = series.fillna(method="ffill").fillna(method="bfill")
    ma = s.rolling(window=window, min_periods=1).mean()
    last = ma.iloc[-1]
    return [float(last)] * steps
