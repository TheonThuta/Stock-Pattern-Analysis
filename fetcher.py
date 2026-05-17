import yfinance as yf

def get_stock_data(ticker, inter, peri):
    return yf.download(tickers=ticker, interval=inter, period=peri).droplevel(1, axis=1).reset_index()

def get_stock_info(ticker):
    data = yf.Ticker(ticker).info
    return {
        'currentPrice': data['currentPrice'],
        'previousClose': data['previousClose']
    }

def get_stock_news(tick):
    data = yf.Ticker(ticker=tick).news
    stories = []
    for i in data[:5]:
        article = {
            'title': i['content']['title'],
            'url': i['content']['clickThroughUrl']['url'],
            'source': i['content']['provider']['displayName'],
            'image': i['content']['thumbnail']['originalUrl']
        }
        stories.append(article)
    return stories