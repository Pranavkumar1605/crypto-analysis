# Cryptocurrency Price Analysis & Strategy Backtester

A beginner-friendly data science project for analyzing cryptocurrency prices and backtesting simple trading strategies.

## Project Goals
- Fetch historical cryptocurrency data
- Perform exploratory data analysis (EDA)
- Visualize price trends and patterns
- Implement and backtest simple trading strategies
- Calculate performance metrics

## Project Structure
```
crypto-analysis/
├── README.md
├── requirements.txt
├── data/
│   └── raw/
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_strategy_backtest.ipynb
├── src/
│   ├── data_fetcher.py
│   ├── indicators.py
│   └── backtester.py
└── results/
    └── plots/
```

## Getting Started

### Installation
```bash
git clone https://github.com/yourusername/crypto-analysis.git
cd crypto-analysis
pip install -r requirements.txt
```

## Features

### Phase 1: Data Collection
- Fetch data from free APIs (CoinGecko, Binance)
- Collect Bitcoin, Ethereum, and other major cryptocurrencies
- Store data in CSV format

### Phase 2: Exploratory Data Analysis
- Price trends over time
- Volatility analysis
- Correlation between different cryptocurrencies
- Volume analysis
- Basic statistical metrics (mean, std, returns)

### Phase 3: Technical Indicators
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- Bollinger Bands
- MACD (Moving Average Convergence Divergence)

### Phase 4: Strategy Backtesting
- **Moving Average Crossover Strategy**
  - Buy when short MA crosses above long MA
  - Sell when short MA crosses below long MA
- **RSI Strategy**
  - Buy when RSI < 30 (oversold)
  - Sell when RSI > 70 (overbought)
- Calculate returns, Sharpe ratio, max drawdown

## Learning Resources
- [Python for Finance](https://www.python.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Quantitative Finance Basics]()

## Contributing
This is a learning project, but suggestions are welcome!

## 👤 Author
Your Name - [GitHub](https://github.com/Pranavkumar1605)
```
