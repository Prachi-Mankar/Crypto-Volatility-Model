import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

# 📁 Path to merged sentiment files
coin_info = {
    "bitcoin": "outputs/bitcoin_merged_sentiment.csv",
    "ethereum": "outputs/ethereum_merged_sentiment.csv",
    "solana": "outputs/solana_merged_sentiment.csv",
    "cardano": "outputs/cardano_merged_sentiment.csv"
}

# ✅ Lag feature generator
def create_lag_features(df, n_lags=3):
    for lag in range(1, n_lags + 1):
        df[f"lag_{lag}_ret"] = df['returns'].shift(lag)
        df[f"lag_{lag}_sent"] = df['Avg_Sentiment'].shift(lag)
    return df.dropna()

# 🚀 Loop through each coin
for coin, path in coin_info.items():
    print(f"\n=== Training models for {coin.upper()} ===")
    
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue

    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = create_lag_features(df)

    # Generate volatility if not available
    if 'volatility' not in df.columns:
        df['volatility'] = df['returns'].rolling(7).std()

    df.dropna(inplace=True)

    # Features and targets
    features = [col for col in df.columns if 'lag' in col]
    X = df[features]
    y_ret = df['returns']
    y_vol = df['volatility']

    # Train-test split
    X_train, X_test, y_ret_train, y_ret_test = train_test_split(X, y_ret, test_size=0.2, shuffle=False)
    _, _, y_vol_train, y_vol_test = train_test_split(X, y_vol, test_size=0.2, shuffle=False)

    # --- Train & Save 4 models ---
    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)

    # 1. Random Forest - Return
    rf_ret = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_ret.fit(X_train, y_ret_train)
    joblib.dump(rf_ret, f"{models_dir}/{coin}_rf_ret_model.pkl")

    # 2. Random Forest - Volatility
    rf_vol = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_vol.fit(X_train, y_vol_train)
    joblib.dump(rf_vol, f"{models_dir}/{coin}_rf_vol_model.pkl")

    # 3. XGBoost - Return
    xgb_ret = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    xgb_ret.fit(X_train, y_ret_train)
    joblib.dump(xgb_ret, f"{models_dir}/{coin}_xgb_ret_model.pkl")

    # 4. XGBoost - Volatility
    xgb_vol = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    xgb_vol.fit(X_train, y_vol_train)
    joblib.dump(xgb_vol, f"{models_dir}/{coin}_xgb_vol_model.pkl")

    print(f"✅ Saved all models for {coin}")
