# Stock Intelligence Dashboard 🚀

A professional FinTech dashboard built with **FastAPI**, **YFinance**, and **Chart.js**.

## Features
- **Real-time Data:** Fetches live market data using Yahoo Finance API.
- **Risk Metrics:** Calculates a custom "Volatility Score" to assess investment risk.
- **Visualization:** Interactive 30-day price trend charts.

## Setup Instructions
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate`
3. Install requirements: `pip install fastapi uvicorn pandas yfinance`
4. Run the server: `uvicorn main:app --reload`
5. Open `index.html` in your browser.


"During development, I resolved a NoneType subscriptable error in the yfinance library by implementing a robust data-validation check and standardizing Multi-Index columns. This ensures the dashboard remains stable even when third-party data providers return inconsistent formats."