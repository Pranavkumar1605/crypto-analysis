import yfinance as yf
import pandas as pd
from datetime import datetime
import os


class CryptoDataFetcher:
    # fetch data

    def __init__(self):

        self.ticker_map = {
            "bitcoin": "BTC-USD",
            "ethereum": "ETH-USD",
            "cardano": "ADA-USD",
            "solana": "SOL-USD",
            "ripple": "XRP-USD",
        }

    def get_historical_data(self, coin_id="bitcoin", days=365):
        """
        Fetch historical price data

        Parameters:
        -----------
        coin_id : str
            Cryptocurrency name (e.g., 'bitcoin', 'ethereum')
        days : int
            Number of days of historical data

        Returns:
        --------
        pd.DataFrame with OHLCV data
        """

        try:
            ticker = self.ticker_map.get(coin_id.lower(), "BTC-USD")
            print(f"fetching {days} days of data for {coin_id}...")
            data = yf.download(ticker, period=f"{days}d", interval="1d", progress=False)
            if data.empty:
                print(f"❌ No data found for {coin_id}")
                return None

            print(f"✅ Successfully fetched {len(data)} days of data!")
            return data

        except Exception as e:
            print(f"❌ Error fetching data: {e}")
            return None

    def get_multiple_coins(self, coins=["ethereum", "bitcoin"], days=365):
        data_dict = {}
        print(f" fetchinf data for {len(coins)} cryptos for {days} days")
        for coin in coins:
            data_dict[coins] = self.get_historical_data(coin, days)
        return data_dict

    def save_to_csv(self, data, coin_id="bitcoin"):
        filename = f'crypto-analysis/data/raw/{coin_id}_{datetime.now().strftime("%Y%m%d")}.csv'
        data.to_csv(filename)
        print(f"💾 Data saved to {filename}")
        return filename


if __name__ == "__main__":
    print("🚀 Starting Crypto Data Fetcher...\n")

    fetcher = CryptoDataFetcher()
    btc_data = fetcher.get_historical_data("bitcoin", days=365)

    if btc_data is not None:
        print("\n" + "=" * 50)
        print(" Bitcoin Data Summary:")
        print("=" * 50)
        print(btc_data.head())
        print("\n Statistics:")
        print(btc_data["Close"].describe())

        fetcher.save_to_csv(btc_data, "bitcoin")
        print("setup commplete")
