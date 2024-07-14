import requests
import pandas as pd

API_KEY = 'YOUR_API_KEY'

def get_stock_price(symbol):
    """Fetch the real-time stock price for the given symbol."""
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    try:
        response = requests.get(url)
        data = response.json()
        if 'Global Quote' in data:
            price = data['Global Quote'].get('05. price')
            if price:
                return float(price)
            else:
                print(f"No price data found for {symbol}.")
                return None
        else:
            print(f"Error fetching data for {symbol}: {data.get('Error Message', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        """Add shares of a stock to the portfolio."""
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares

    def remove_stock(self, symbol, shares):
        """Remove shares of a stock from the portfolio."""
        if symbol in self.stocks:
            self.stocks[symbol] -= shares
            if self.stocks[symbol] <= 0:
                del self.stocks[symbol]
        else:
            print(f"No shares of {symbol} found in the portfolio.")

    def get_portfolio_value(self):
        """Calculate the total value of the portfolio."""
        total_value = 0
        for symbol, shares in self.stocks.items():
            price = get_stock_price(symbol)
            if price is not None:
                total_value += price * shares
        return total_value

    def display_portfolio(self):
        """Display the current portfolio with real-time prices and total value."""
        portfolio_data = []
        for symbol, shares in self.stocks.items():
            price = get_stock_price(symbol)
            if price is not None:
                portfolio_data.append({
                    'Symbol': symbol,
                    'Shares': shares,
                    'Current Price': price,
                    'Total Value': price * shares
                })
        if portfolio_data:
            df = pd.DataFrame(portfolio_data)
            print(df)
            print(f"\nTotal Portfolio Value: ${self.get_portfolio_value():.2f}")
        else:
            print("Portfolio is empty.")

def main():
    portfolio = Portfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. View portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            print("Exiting the tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()