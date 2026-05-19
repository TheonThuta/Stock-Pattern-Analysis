import yfinance as yf

def get_stock_data(ticker, inter, peri):
    return yf.download(tickers=ticker, interval=inter, period=peri).droplevel(1, axis=1).reset_index()

def get_stock_info(ticker):
    data = yf.download(ticker, period='2d', interval='1d')
    return {
        'currentPrice': round(data['Close'].iloc[-1].item(), 2),
        'previousClose': round(data['Close'].iloc[-2].item(), 2)
    }

def get_stock_news(tick):
    data = yf.Ticker(ticker=tick).news
    stories = []
    for i in data[:5]:
        if not i['content']['clickThroughUrl']:
            continue
        article = {
            'title': i['content']['title'],
            'url': i['content']['clickThroughUrl']['url'],
            'source': i['content']['provider']['displayName'],
            'image': i['content']['thumbnail']['originalUrl']
        }
        stories.append(article)
    return stories

def get_indicators(tick):
    data = yf.download(tickers=tick, period='60d', interval='1d')
    daily_change = data['Close'].diff()
    avg_gain = daily_change.clip(lower=0).rolling(14).mean()
    avg_loss = daily_change.clip(upper=0).abs().rolling(14).mean()
    RS = avg_gain/avg_loss
    RSI = 100 - (100/(1+RS))
    EMA12 = data['Close'].ewm(span=12).mean()
    EMA26 = data['Close'].ewm(span=26).mean()
    MACD = EMA26-EMA12
    signal = MACD.ewm(span=9).mean()
    return {'RSI' : round(RSI.iloc[-1].item(), 2), 
            'MACD': round(MACD.iloc[-1].item(), 2),
            'signal': round(signal.iloc[-1].item(), 2)
            }