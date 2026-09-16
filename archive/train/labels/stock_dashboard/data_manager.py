import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def get_stock_data(symbol):
    try:
        # 1. Download data
        df = yf.download(symbol, period="1y", auto_adjust=True)
        
        if df.empty:
            return None, 0, 0, 0

        # 2. Handle Multi-Index
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.dropna()

        # 3. CALCULATE NEW METRICS
        # Daily Return: (Close - Open) / Open
        df['Daily_Return'] = (df['Close'] - df['Open']) / df['Open']
        
        # 7-Day Moving Average
        df['7MA'] = df['Close'].rolling(window=7).mean()


        # CREATIVE METRIC: Volatility Score (Standard Deviation of returns)
        # We multiply by 100 to make it a readable percentage
        volatility = float(df['Daily_Return'].std() * 100)

        # 4. Standard Metrics
        high_52 = float(df['High'].max())
        low_52 = float(df['Low'].min())
        
        # We return 4 values now: df, high, low, and volatility
        return df, high_52, low_52, volatility
        
    except Exception as e:
        print(f"Logic Error: {e}")
        return None, 0, 0, 0
    


def get_prediction(df):
    # Use last 30 days to predict tomorrow
    df_recent = df.tail(30).reset_index()
    X = np.array(df_recent.index).reshape(-1, 1)
    y = df_recent['Close'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    next_day = np.array([[30]])
    prediction = model.predict(next_day)
    return float(prediction[0])