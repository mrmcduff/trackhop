from flask import Flask, request, jsonify
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

secret_key = os.getenv('ALPHA_VANTAGE_API_KEY')
polygon_key = os.getenv('POLYGON_IO_API_KEY')

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

@app.route('/api/data', methods=['POST'])
def create_data():
    # Code to handle the POST request data
    data = request.get_json()
    # Code to process the data and store it in a database or send it to an external API
    return jsonify({'message': 'Data received successfully'})

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
