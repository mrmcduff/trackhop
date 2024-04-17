from flask import Flask, request, jsonify
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

secret_key = os.getenv('ALPHA_VANTAGE_API_KEY')

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

@app.route('/api/data', methods=['POST'])
def create_data():
    # Code to handle the POST request data
    data = request.get_json()
    # Code to process the data and store it in a database or send it to an external API
    return jsonify({'message': 'Data received successfully'})

def get_external_data():
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey={}'.format(secret_key)
    response = requests.get(url)
    print(response)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
        # # Get the list of sectors
        # sectors = data['Rank A: Real-Time Performance']

        # # Find the TECHNOLOGY sector
        # tech_sector = next((sector for sector, info in sectors.items() if sector == 'TECHNOLOGY'), None)

        # # Get the list of tickers in the TECHNOLOGY sector
        # tech_tickers = [ticker.strip() for ticker in sectors[tech_sector].split(',')]

        # # Print the list of tickers
        # print(tech_tickers)
    else:
        print('Error: {}'.format(response.status_code))