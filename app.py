from flask import Flask, render_template, jsonify
from fetcher import get_stock_data
from predictor import get_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stock/<ticker>/<period>')
def stock(ticker, period):
    return get_stock_data(ticker, '1d', period).to_json(orient='records', date_format='iso')

@app.route('/api/predict/<ticker>')
def predict(ticker):
    return jsonify(get_prediction(ticker))


if __name__ == '__main__':
    app.run()

