from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_manager import get_stock_data

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows your HTML file to talk to the API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome! Go to /docs"}

@app.get("/summary/{symbol}")
def stock_summary(symbol: str):
    # Notice we added 'vol' here to catch the 4th value
    df, h52, l52, vol = get_stock_data(symbol)
    
    if df is None:
        return {"error": "Invalid symbol"}
    
    return {
        "symbol": symbol,
        "52_week_high": h52,
        "52_week_low": l52,
        "avg_close": float(df['Close'].mean()),
        "volatility": round(vol, 2)  # Sending the new metric to the UI
    }

@app.get("/data/{symbol}")
def get_chart_data(symbol: str):
    # Added 'vol' here to match the 4 values returned by data_manager
    df, h52, l52, vol = get_stock_data(symbol) 
    
    if df is None:
        return {"error": "Invalid symbol"}
    
    # Take the last 30 days
    last_30 = df.tail(30)
    
    return {
        "dates": last_30.index.strftime('%Y-%m-%d').tolist(),
        "prices": last_30['Close'].tolist()
    }

@app.get("/compare")
def compare_stocks(symbol1: str, symbol2: str):
    # You MUST catch 4 values: df, h52, l52, AND vol
    df1, h52_1, l52_1, vol1 = get_stock_data(symbol1)
    df2, h52_2, l52_2, vol2 = get_stock_data(symbol2)
    
    if df1 is None or df2 is None:
        return {"error": "Invalid symbols"}
    
    # Calculate which one performed better in the last 30 days
    ret1 = float(((df1['Close'].iloc[-1] - df1['Close'].iloc[-30]) / df1['Close'].iloc[-30]) * 100)
    ret2 = float(((df2['Close'].iloc[-1] - df2['Close'].iloc[-30]) / df2['Close'].iloc[-30]) * 100)
    
    return {
        "comparison": {
            symbol1: {"30d_return": round(ret1, 2), "volatility": round(vol1, 2)},
            symbol2: {"30d_return": round(ret2, 2), "volatility": round(vol2, 2)}
        },
        "winner": symbol1 if ret1 > ret2 else symbol2
    }