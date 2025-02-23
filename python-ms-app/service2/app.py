from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/service2', methods=['GET'])
def service2_endpoint():
    return jsonify({"message": "Hello from Service 2!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "id": 1,
        "name": "Service 2",
        "description": "This is a sample microservice."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)