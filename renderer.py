import matplotlib.pyplot as plt
import os
from fetcher import get_stock_data

def render_chart(ticker):
    data = get_stock_data(ticker, '1d', '1y')
    plt.plot(data['Close'], linewidth=2)
    filepath = os.path.join('static', 'charts', f'{ticker}.png')
    if os.path.exists(filepath):
        os.remove(filepath)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(filepath)
    plt.clf()
    return filepath

render_chart('AAPL')