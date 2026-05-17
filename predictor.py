import yfinance as yf

def get_prediction(ticker):
    data = yf.download(tickers=ticker, period='30d', interval='1h')
    close_price = data['Close']
    SMA = close_price[-9:].mean().item()
    LMA = close_price[-21:].mean().item()
    confidence_score = ((abs(SMA-LMA) / LMA) * 100)
    if SMA > LMA:
        return {'direction': 'Rise', 'confidence': round(confidence_score, 2)}
    else:
        return {'direction': 'Fall', 'confidence': round(confidence_score, 2)}
