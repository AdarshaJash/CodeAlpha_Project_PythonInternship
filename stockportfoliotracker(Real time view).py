import requests
import pandas as pd
import yfinance as yf # type: ignore
from datetime import datetime, timedelta
class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}
        self.historical_data = {}
    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        self.update_historical_data(symbol)
        print(f"Added {shares} shares of {symbol} to the portfolio.")
    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio and self.portfolio[symbol] >= shares:
            self.portfolio[symbol] -= shares
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            print(f"Removed {shares} shares of {symbol} from the portfolio.")
        else:
            print(f"Not enough shares of {symbol} to remove.")
    def get_stock_price(self, symbol):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if "Time Series (Daily)" in data:
            latest_date = list(data["Time Series (Daily)"].keys())[0]
            price = float(data["Time Series (Daily)"][latest_date]["1. open"])
            return price
        else:
            if "Error Message" in data:
                print(f"Error fetching data for {symbol}: {data['Error Message']}")
            elif "Note" in data:
                print(f"API call limit reached: {data['Note']}")
            else:
                print(f"Unexpected error fetching data for {symbol}: {data}")
            return None
    def update_historical_data(self, symbol):
        end_date = datetime.today().strftime('%Y-%m-%d')
        start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
        data = yf.download(symbol, start=start_date, end=end_date)
        self.historical_data[symbol] = data
        print(f"Updated historical data for {symbol}.")
    def get_historical_performance(self, symbol):
        if symbol in self.historical_data:
            return self.historical_data[symbol]
        else:
            print(f"No historical data available for {symbol}.")
            return None
    def get_portfolio_value(self):
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                total_value += price * shares
        return total_value
    def show_portfolio(self):
        portfolio_df = pd.DataFrame.from_dict(self.portfolio, orient='index', columns=['Shares'])
        portfolio_df.index.name = 'Symbol'
        return portfolio_df
if __name__ == "__main__":
    api_key = 'CTU0KKM9H8LMEQTC'
    portfolio = StockPortfolio(api_key)
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)
    portfolio.remove_stock("AAPL", 3)
    print(portfolio.show_portfolio())
    print(f"Total Portfolio Value: ${portfolio.get_portfolio_value():.2f}")
    print("Designed by Adarsha Jash")
    historical_data = portfolio.get_historical_performance("AAPL")
    if historical_data is not None:
        print(historical_data.tail())