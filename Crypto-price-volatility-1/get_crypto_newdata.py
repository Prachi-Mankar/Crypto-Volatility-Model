import requests
import pandas as pd
import os
from datetime import datetime

# 🛠 Create 'data' folder if missing
os.makedirs("data", exist_ok=True)

def fetch_fear_greed_index(days=365):
    url = f"https://api.alternative.me/fng/?limit={days}&format=json"
    response = requests.get(url)
    data = response.json()

    records = data['data']
    df = pd.DataFrame(records)
    df['timestamp'] = pd.to_datetime(df['timestamp'].astype(int), unit='s')
    df.rename(columns={
        'value': 'fear_greed_score',
        'value_classification': 'sentiment_label',
        'timestamp': 'date'
    }, inplace=True)

    df = df[['date', 'fear_greed_score', 'sentiment_label']]
    df['fear_greed_score'] = df['fear_greed_score'].astype(int)

    return df.sort_values('date')

# 📦 Save the data
df_sentiment = fetch_fear_greed_index(365)
df_sentiment.to_csv("data/fear_greed_sentiment.csv", index=False)
print("✅ Sentiment data saved to data/fear_greed_sentiment.csv")
print(df_sentiment.head())
