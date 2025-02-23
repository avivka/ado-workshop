from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to Service 1!")

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "id": 1,
        "name": "Service 1",
        "description": "This is a sample microservice."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)