from flask import Flask, request, jsonify
import requests
import os
from components import QueryCache
import json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

secret_key = os.getenv('ALPHA_VANTAGE_API_KEY')
polygon_key = os.getenv('POLYGON_IO_API_KEY')

polygon_base = "https://api.polygon.io"

api_cache = QueryCache.QueryCache()

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/data', methods=['GET'])
def get_data():
    external_data = get_external_data()
    if external_data:
        # Code to process the external data
        return jsonify(external_data)
    else:
        return jsonify({'message': 'Failed to retrieve external data'})

@app.route('/api/poly', methods=['GET'])
def get_poly_data():
    external_data = get_external_polygon_data()
    if external_data:
        # Code to process the external data
        return jsonify(external_data)
    else:
        return jsonify({'message': 'Failed to retrieve external data'})

@app.route('/api/ohlc/<ticker>/<datestr>')
def get_ohlc_data(ticker: str, datestr: str):
    cached = api_cache.get_cache(ticker=ticker.upper(), date=datestr.upper())
    if cached is not None:
        print(f"Returning value from cache for {ticker.upper()} on {datestr}")
        return cached

    external_data = get_ticker_ohlc_data(ticker.upper(), datestr)
    if external_data:
        api_cache.cache_query(ticker=ticker.upper(), date=datestr.upper(), data=external_data)
        return jsonify(external_data)
    else:
        return jsonify({'message': 'It failed so hard'})


@app.route('/api/data', methods=['POST'])
def create_data():
    # Code to handle the POST request data
    data = request.get_json()
    # Code to process the data and store it in a database or send it to an external API
    return jsonify({'message': 'Data received successfully'})

def get_ticker_ohlc_data(ticker: str, datestr: str):
    url = f"https://api.polygon.io/v1/open-close/{ticker.upper()}/{datestr}?adjusted=true&apikey={polygon_key}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Error: {}'.format(response.status_code))

def get_external_polygon_data():
    url = 'https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&active=true&apiKey={}'.format(polygon_key)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Error: {}'.format(response.status_code))

def get_external_data():
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey={}'.format(secret_key)
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        return response.json()
    else:
        print('Error: {}'.format(response.status_code))
