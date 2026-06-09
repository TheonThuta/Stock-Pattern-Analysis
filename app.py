from flask import Flask, render_template, jsonify
from fetcher import get_stock_data


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze/<ticker>')
def analyze(ticker):
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run()

