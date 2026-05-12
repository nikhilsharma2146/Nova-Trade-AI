import pandas as pd
import numpy as np
import datetime

def get_dummy_data(days=100):
    """Generate dummy stock data for demonstration"""
    np.random.seed(42)
    dates = pd.date_range(end=datetime.datetime.now(), periods=days)
    
    # Random walk
    close = 150 + np.random.randn(days).cumsum()
    high = close + np.random.rand(days) * 5
    low = close - np.random.rand(days) * 5
    open_p = close + np.random.randn(days) * 2
    volume = np.random.randint(1000000, 5000000, days)
    
    df = pd.DataFrame({
        'Open': open_p,
        'High': high,
        'Low': low,
        'Close': close,
        'Volume': volume
    }, index=dates)
    
    return df

def get_market_summary():
    return [
        {"name": "S&P 500", "value": "4,185.82", "change": "1.2%", "positive": True},
        {"name": "NASDAQ", "value": "12,888.28", "change": "1.5%", "positive": True},
        {"name": "DOW JONES", "value": "33,674.38", "change": "-0.4%", "positive": False},
        {"name": "BTC/USD", "value": "$28,450.00", "change": "3.2%", "positive": True}
    ]
