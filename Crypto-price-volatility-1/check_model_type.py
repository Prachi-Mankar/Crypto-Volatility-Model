import pickle

files = [
    "bitcoin_rf_ret_model.pkl",
    "bitcoin_rf_vol_model.pkl",
    "bitcoin_xgb_ret_model.pkl",
    "bitcoin_xgb_vol_model.pkl"
]

for file in files:
    try:
        with open(f"models/{file}", "rb") as f:
            obj = pickle.load(f)
            print(f"{file} → {type(obj)}")
    except Exception as e:
        print(f"{file} → ❌ Failed to load: {e}")
