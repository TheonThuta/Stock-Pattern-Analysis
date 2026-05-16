import yfinance as yf

def get_stock_data(ticker, inter, peri):
    return yf.download(tickers=ticker, interval=inter, period=peri).droplevel(1, axis=1).reset_index()

def get_stock_info(ticker):
    data = yf.Ticker(ticker).info
    return {
        'currentPrice': data['currentPrice'],
        'previousClose': data['previousClose']
    }