import yfinance as yf
import os

cryptos = ["BTC-USD", "ETH-USD", "SOL-USD", "ADA-USD"]
start_date = "2022-01-01"
end_date = "2024-12-31"

os.makedirs("data", exist_ok=True)

for symbol in cryptos:
    data = yf.download(symbol, start=start_date, end=end_date, interval="1d")
    filename = f"data/{symbol.split('-')[0].lower()}_price.csv"
    data.to_csv(filename)
    print(f"{symbol} data saved to {filename}")

