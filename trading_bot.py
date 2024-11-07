import ccxt

    # Initialize the exchange with your API keys (optional)
    exchange = ccxt.binance({
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET_KEY'
    })

    def fetch_ticker(symbol):
        return exchange.fetch_ticker(symbol)

    def get_last_price(symbol):
        ticker = fetch_ticker(symbol)
        return ticker['last']

    def place_order(side, symbol, amount, price=None):
        if side not in ['buy', 'sell']:
            raise ValueError("Side must be either 'buy' or 'sell'")
        
        order_params = {
            'symbol': symbol,
            'side': side,
            'type': 'limit',
            'amount': amount,
            'price': price
        }
        
        return exchange.create_order(**order_params)

    def main():
        symbol = 'BTC/USDT'
        last_price = get_last_price(symbol)
        print(f"Current {symbol} price: {last_price}")

        # Example order placement (buy at the current market price)
        buy_order = place_order('buy', symbol, 0.1)
        print(f"Bought {buy_order['amount']} {symbol} for {buy_order['price']}")

    if __name__ == "__main__":
        main()
