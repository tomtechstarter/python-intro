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

# Zusatzaufgabe
# Banus Lösung: Einfach und präzise.
@app.route('/api/banudata', methods=['GET'])
def get_single_banu_data():
    return jsonify({'data': data[0]})

# Tinas Lösung: Sicherheit, ob data mindestens 1 Wert enthält, sonst Fehler-'message'
@app.route('/api/tinadata', methods=['GET'])
def get_single_tina_data():
    if len(data) > 0:
        return jsonify({'single_data': data[0]})
    else:
        return jsonify({'message': "Zu wenig Daten"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)