from flask import Flask, jsonify
from database import get_last_values, init_db
import threading
from mqtt_client import start_mqtt

app = Flask(__name__)

@app.route('/')
def home():
    return "Smart Home API - Usa /api/data per visualizzare i dati dei sensori"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(get_last_values())

if __name__ == "__main__":
    init_db()
    t = threading.Thread(target=start_mqtt)
    t.start()
    app.run(debug=True)
