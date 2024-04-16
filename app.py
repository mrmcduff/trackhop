from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
