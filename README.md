
# **AI Blockchain Finance Platform**

An advanced **Streamlit-based web application** for decentralized finance (**DeFi**) analysis, powered by **AI** and real-time **blockchain data**. This platform offers tools for:

- Cryptocurrency **price prediction**
- **Portfolio optimization**
- **Risk and sentiment analysis**
- **Network and transaction analysis**
- And more.

It uses cutting-edge machine learning models like **LightGBM**, **CatBoost**, **TabNet**, and **Prophet**, alongside blockchain APIs such as **CoinGecko**, **Blockchair**, and **DeFiLlama**, to deliver actionable insights for DeFi investors.

---

## 🔍 **Features**

- **Price Prediction**  
  Forecast crypto prices using an ensemble of **LightGBM**, **CatBoost**, **TabNet**, and **Prophet**, enhanced with sentiment data.

- **Portfolio Management**  
  Manage and optimize portfolios with constraints (e.g., max allocation, min return).

- **Risk Analysis**  
  Compute metrics like **Value at Risk (VaR)** and **Sharpe Ratio**.

- **Sentiment Analysis**  
  Evaluate news sentiment using **VADER**, **FinBERT**, and **DistilBERT** from CoinTelegraph headlines.

- **Network Analysis**  
  Visualize price correlations using **NetworkX** and **Plotly**.

- **Blockchain Monitor**  
  Real-time blockchain data via the **Blockchair API** (transactions, fees, etc.).

- **DeFi Insights**  
  Access **Total Value Locked (TVL)** from **DeFiLlama API**.

- **Trading Alerts**  
  Set alerts for price shifts, sentiment changes, or portfolio anomalies.

- **Explainable AI**  
  Interpret model predictions with **SHAP** visualizations.

- **Dynamic Rebalancing**  
  Optimize portfolios using **DQN-based reinforcement learning**.

- **Transaction Analysis**  
  Analyze blockchain graphs using **Graph Neural Networks (GNNs)**.

- **Market Scenarios**  
  Simulate markets with a **Variational Autoencoder (VAE)**.

- **Security**  
  Detect portfolio anomalies using **Isolation Forest**.

- **User Authentication**  
  Secure login using **SQLite** and **bcrypt** password hashing.

---

## 📁 **Repository Structure**

```
AI-Blockchain-Finance-Platform/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # License file
├── .gitignore             # Ignored files
├── data/
│   ├── portfolio.db       # User portfolios
│   └── users.db           # User credentials
├── scripts/
│   └── utils.py           # Helper functions
├── static/
│   └── styles.css         # Custom styles
└── tests/
    └── test_app.py        # Unit tests
```

---

## ⚙️ **Prerequisites**

- Python **3.8+**
- **Git**
- A modern web browser  
- API access to:
  - [CoinGecko](https://coingecko.com) *(no key needed)*
  - [Blockchair](https://blockchair.com) *(free tier available)*
  - [DeFiLlama](https://defillama.com) *(no key needed)*

---

## 🚀 **Installation**

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/AI-Blockchain-Finance-Platform.git
cd AI-Blockchain-Finance-Platform
```

2. **Create a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the App:**

```bash
streamlit run app.py
```

> App will be available at: [http://localhost:8501](http://localhost:8501)

---

## 🧑‍💼 **Usage**

### 🔐 Login/Register

- Register a new account or log in
- Passwords are hashed using **bcrypt**

### 🧭 Navigate Features

- Use the **sidebar** to access:
  - Price Prediction
  - Portfolio Management
  - Risk Analysis
  - DeFi TVL
  - Sentiment Trends
- Add/edit holdings and optimize allocations
- Monitor blockchain metrics and alerts

### 🔧 Customization

- Set thresholds for price/sentiment alerts
- Tune portfolio optimization constraints
- Simulate decentralized deployment (e.g., Ethereum oracle)

---

## 📦 **Dependencies**

Key Python packages:

```
streamlit, pandas, numpy, requests, sqlite3, bcrypt, scikit-learn,
plotly, networkx, prophet, lightgbm, catboost, pytorch-tabnet,
vaderSentiment, transformers, torch, torch-geometric,
beautifulsoup4, shap, scipy, optuna, ta, matplotlib,
stable-baselines3, streamlit-autorefresh
```

Generate requirements:

```bash
pip freeze > requirements.txt
```

---

## 🛠️ **Configuration**

- **Logging**: Saved to `app.log` with timestamps and errors
- **Caching**: Handled using `@st.cache_data` and `@st.cache_resource`
- **APIs**:
  - **CoinGecko** – Market data
  - **Blockchair** – Blockchain stats
  - **DeFiLlama** – DeFi protocol TVL
- **Database**: SQLite for users and portfolio storage

---

## ✅ **Testing**

Unit tests in the `tests/` directory.

Run:

```bash
pytest tests/test_app.py
```

*Note: `test_app.py` is a placeholder. Extend with tests for key functions.*

---

## 🤝 **Contributing**

1. **Fork** the repo  
2. **Create a branch**  
   `git checkout -b feature/your-feature`
3. **Commit your changes**  
   `git commit -m "Add your feature"`
4. **Push**  
   `git push origin feature/your-feature`
5. **Open a Pull Request**

---

## 📄 **License**

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 🙏 **Acknowledgments**

- [Streamlit](https://streamlit.io/) for the web app framework  
- [CoinGecko](https://coingecko.com) for market data  
- [Blockchair](https://blockchair.com) for blockchain data  
- [DeFiLlama](https://defillama.com) for DeFi analytics  
- [Hugging Face](https://huggingface.co) for sentiment models  

---

## 📬 **Contact**

For issues or suggestions:  
**[your email or GitHub issue tracker]**
