from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Beispiel Data
data = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Jane'},
    {'id': 3, 'name': 'Doe'}
]

# Route um alle Daten zu erhalten
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
