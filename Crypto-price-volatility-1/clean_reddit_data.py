import pandas as pd
import re

# Step 1: Load the raw Reddit post data
df = pd.read_csv(r'C:\Users\dell\crypto-price-volatility\Crypto-price-volatility-1\data\reddit_bitcoin_posts.csv')


# Step 2: Drop duplicates
df.drop_duplicates(inplace=True)

# Step 3: Drop missing or null text rows
df.dropna(subset=['text'], inplace=True)

# Step 4: Remove unwanted characters, URLs, special symbols
def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]+", "", text)  # remove special characters
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text.lower()

df['clean_text'] = df['text'].apply(clean_text)

# Step 5: Save cleaned data
df.to_csv('reddit_bitcoin_cleaned.csv', index=False)
print("✅ Cleaned data saved to reddit_bitcoin_cleaned.csv")
