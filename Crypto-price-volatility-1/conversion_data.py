import pandas as pd

# Load bitcoin price data
price_df = pd.read_csv("../data/bitcoin.csv")

# Convert timestamp to datetime format
price_df['date'] = pd.to_datetime(price_df['timestamp'])

# Optional: Rename bitcoin_price to price
price_df.rename(columns={'bitcoin_price': 'price'}, inplace=True)

# Calculate returns
price_df['returns'] = price_df['price'].pct_change()

# Drop missing values from returns
price_df.dropna(inplace=True)

# Preview
price_df.head()
