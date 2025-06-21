import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="Crypto Volatility Classifier", layout="centered")

st.title("📊 Cryptocurrency Volatility Classifier")

# User selects coin and model type
coin = st.selectbox("Choose Cryptocurrency", ["bitcoin", "ethereum", "solana", "cardano"])
model_type = st.selectbox("Choose Model Type", [
    "Random Forest - Return", 
    "Random Forest - Volatility", 
    "XGBoost - Return", 
    "XGBoost - Volatility"
])

# Map selection to filename
def get_model_filename(coin, model_type):
    if "Random Forest" in model_type:
        algo = "rf"
    else:
        algo = "xgb"

    if "Return" in model_type:
        target = "ret"
    else:
        target = "vol"

    return f"{coin}_{algo}_{target}_model.pkl"

model_filename = get_model_filename(coin, model_type)

# Load model
@st.cache_data
def load_model(model_path):
    import joblib
    model = joblib.load(model_path)
    st.write(f"Loaded model type: {type(model)}")
    return model


model_path = os.path.join("models", model_filename)

try:
    model = load_model(model_path)

    st.subheader("📝 Enter Lagged Features")

    feature_1 = st.number_input("returns_lag1", value=0.001)
    feature_2 = st.number_input("sentiment_lag1", value=0.1)
    feature_3 = st.number_input("returns_lag2", value=0.001)
    feature_4 = st.number_input("sentiment_lag2", value=0.1)
    feature_5 = st.number_input("returns_lag3", value=0.001)
    feature_6 = st.number_input("sentiment_lag3", value=0.1)

    X_input = pd.DataFrame([[feature_1, feature_2, feature_3, feature_4, feature_5, feature_6]],
                           columns=['returns_lag1', 'sentiment_lag1',
                                    'returns_lag2', 'sentiment_lag2',
                                    'returns_lag3', 'sentiment_lag3'])

    if st.button("Predict Volatility Regime"):
        try:
            pred = model.predict(X_input)[0]
            pred_label = "🔴 High Volatility" if pred == 1 else "🟢 Low/Stable Volatility"
            st.success(f"Prediction: {pred_label}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

except FileNotFoundError:
    st.error(f"Model file not found: `{model_filename}`. Please make sure it exists in the `models/` folder.")


