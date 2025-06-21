# 🚀 Cryptocurrency Volatility Modeling and Recommendation Engine

## 📌 Project Overview

This project analyzes and models **cryptocurrency price volatility** using statistical and machine learning models, with the end goal of building a **recommendation engine** based on volatility, returns, and investor risk appetite.

---

## 🔍 Objectives

* **Model and Forecast Volatility Using Stochastic Models**

  * Applied **GARCH(1,1)** to model conditional volatility for each coin.
  * Compared with rolling volatility and forecasted future risk levels.

* **Cluster Cryptocurrencies Based on Risk and Return**

  * Feature engineering on: average return, volatility, and sentiment.
  * Used **PCA + K-Means** to identify meaningful crypto clusters.

* **Predict Volatility Regimes Using Machine Learning**

  * XGBoost and Random Forest were used to classify time periods as high or low volatility based on lagged returns and engineered features.

* **Recommend Top Cryptocurrencies**

  * Final **ranking score** created using normalized volatility, return, and sentiment.
  * Investor profiles mapped as: 🟢 Conservative, 🟡 Balanced, 🔴 Aggressive.

---

## 💡 Executive Summary

This project presents a full volatility-return modeling pipeline for key cryptocurrencies (Bitcoin, Ethereum, Solana, Cardano). Using GARCH models, clustering, and ML classification, we evaluate each coin and generate tailored recommendations. Feature importance was visualized to understand ML decisions, and final coin scores were computed.

### 📌 Key Outcomes:

* **Bitcoin** had the best combination of low volatility and moderate returns — best for conservative investors.
* **Cardano** had the highest normalized return but at significantly higher risk.
* **Ethereum** showed moderate volatility with lowest return — not ideal.
* **Solana** was highly volatile with modest returns, making it aggressive.

---

## 📈 Model Comparison Table

| Model            | Target              | MSE                        | MAE    | R²    |
| ---------------- | ------------------- | -------------------------- | ------ | ----- |
| **XGBoost**      | Volatility Score    | 0.00089                    | 0.0150 | -1.97 |
| **RandomForest** | Volatility Score    | 0.00019                    | 0.0110 | 0.367 |
| **GARCH(1,1)**   | Volatility Forecast | Evaluated via AIC, BIC, LL | ✔️     | ✔️    |

---

## 📊 Final Recommendation Score (Bar Chart)

![Crypto Recommendation Score](./results/c9b0b01d-62bf-4191-8852-3ab7f9acb21a.png)

| Coin     | Final Score | Recommendation     |
| -------- | ----------- | ------------------ |
| Bitcoin  | 0.2158      | 🟢 Safe            |
| Cardano  | 0.1000      | 🟡 Balanced        |
| Solana   | 0.0054      | 🔴 Aggressive      |
| Ethereum | -0.1057     | ⚠️ Not Recommended |

---

## 🔍 Cluster Analysis: Returns, Volatility & Sentiment

![Crypto Clusters](./results/770ad3af-3c0a-4a16-890f-49a01f50962f.png)

| Coin     | Cluster | Volatility | Return |
| -------- | ------- | ---------- | ------ |
| Bitcoin  | 0       | 0.0261     | 0.0017 |
| Ethereum | 0       | 0.0386     | 0.0000 |
| Solana   | 0       | 0.0456     | 0.0013 |
| Cardano  | 1       | 0.0617     | 0.0032 |

---

## 🧠 Feature Importance – Volatility Classification

![Feature Importance](./results/b3549c90-0305-46f5-81b1-0a88d373ad62.png)

Top features used by XGBoost for volatility classification:

* `bitcoin_returns`
* `ethereum_returns`
* `solana_returns`
* `cardano_returns`

---

## 💡 Business Insights Box

| Coin | Market Stability | Volatility Level   | Sensitivity to Events | Ideal For               |
| ---- | ---------------- | ------------------ | --------------------- | ----------------------- |
| BTC  | High             | Low–Moderate       | Medium                | Conservative Investors  |
| ETH  | Medium           | Moderate           | High                  | Active Traders          |
| SOL  | Low              | High               | Very High             | Risk-Tolerant Investors |
| ADA  | Low              | Very High (spikes) | Extremely High        | Event-Driven Trading    |

---

## 📊 Additional Insights

* **Fear & Greed Score Correlation with Returns**:

  * BTC: `0.2544`
  * ETH: `0.2600`
  * SOL: `0.1876`
  * ADA: `0.1432`

* **Classification Report (Volatility Regimes)**:

  * Overall accuracy: **0.45**
  * Best F1 score: **0.59** for class 3.0 (High Volatility)

---

## 🗂 Data Sources

* 📉 **Crypto Data**: Historical daily price data fetched using [`yfinance`](https://pypi.org/project/yfinance/) for BTC, ETH, SOL, ADA.
* 😱 **Sentiment Data**: Daily sentiment score from [Alternative.me Fear & Greed Index](https://alternative.me/crypto/fear-and-greed-index/).

---

## 🛠 Technologies Used

* **Languages**: Python (Pandas, NumPy)
* **Modeling Libraries**: `ARCH`, `statsmodels`, `XGBoost`, `scikit-learn`
* **Visualization**: Matplotlib, Seaborn, Plotly
* **Sentiment**: VADER (used partially)
* **Development**: VS Code, Jupyter Notebook
* **Version Control**: Git + GitHub

---

## 📁 Project Structure

```
crypto-price-volatility/
├── App.py
├── data/
├── models/     ← trained .pkl files
├── outputs/    ← merged sentiment + price CSVs
├── results/    ← model prediction plots
├── utils/      ← helper functions
└── requirements.txt
```

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Note on Model Files

`.pkl` model files are binary and **cannot be previewed on GitHub**, but they are loadable in the app and notebook.

---

## ✅ Credits

Project by \[Your Name], combining financial time series modeling with machine learning and sentiment analysis.

---

Let me know if you'd like help deploying this on Hugging Face Spaces or Streamlit Cloud!
