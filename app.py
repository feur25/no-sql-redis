from flask import Flask, jsonify, request
from flask_cors import CORS
import redis
import json

app = Flask(__name__)
CORS(app)

# Configuration de la connexion Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 7000

# Connexion à Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route('/redis')
def show_redis_content():
    keys = r.keys()
    content = {}
    for key in keys:
        content[key.decode("utf-8")] = r.get(key).decode("utf-8")
    return jsonify(content)

@app.route('/employee', methods=['POST'])
def add_employee():
    employee_data = request.get_json()
    employee_id = r.incr('employeIdCounter')
    r.set(f'employe:{employee_id}', json.dumps(employee_data))
    return jsonify({'message': 'Employee added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
