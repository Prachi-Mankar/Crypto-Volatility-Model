# import os
# os.makedirs('data', exist_ok=True)
from pycoingecko import CoinGeckoAPI
import pandas as pd
import time
import os

cg = CoinGeckoAPI()

def fetch_price_data(coin_id, vs_currency='usd'):
    # Get current UNIX time (end date) and subtract 365 days (start date)
    end_time = int(time.time())
    start_time = end_time - 365 * 24 * 60 * 60

    data = cg.get_coin_market_chart_range_by_id(
        id=coin_id,
        vs_currency=vs_currency,
        from_timestamp=start_time,
        to_timestamp=end_time
    )

    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', f'{coin_id}_price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.set_index('timestamp').resample('1D').mean().reset_index()
    return df

# Fetch data for multiple coins
coins = ['bitcoin', 'ethereum', 'solana', 'cardano']
dataframes = []

for coin in coins:
    try:
        print(f"Fetching data for {coin}...")
        df = fetch_price_data(coin)
        dataframes.append(df)
    except Exception as e:
        print(f"Error fetching data for {coin}: {e}")

# Save each coin's data to a separate CSV file
os.makedirs('data', exist_ok=True)

for coin, df in zip(coins, dataframes):
    file_path = f'data/{coin}.csv'
    df.to_csv(file_path, index=False)
    print(f"✅ Saved {coin} data to {file_path}")
