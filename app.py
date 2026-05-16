from flask import Flask, render_template
from fetcher import get_stock_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stock/<ticker>/<period>')
def stock(ticker, period):
    return get_stock_data(ticker, '1d', period).to_json(orient='records', date_format='iso')

if __name__ == '__main__':
    app.run()

