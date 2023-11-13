# Meljune Royette G. Go - CPE41S2
from flask import Flask, jsonify, request
app = Flask(__name__)
heartrate = [
    {
        "heart_id": "1",
        "date": "13-11-2023",
        "heart_rate": "80"        
    },  
]

@app.route('/heartrate', methods=['GET'])
def getHeartrate():
    return jsonify(heartrate)

@app.route('/heartrate', methods =['POST'])
def add_heartrate():
    heartrat = request.get_json()
    if 'heart_id' not in heartrat:
        return 'Bad Request', 400
    heartrate.append(heartrat)
    return {'id': len(heartrate)}, 200

@app.route('/heartrate/<int:index>', methods =['DELETE'])
def delete_heartrate(index):
    heartrate.pop(index)
    return 'Successfully deleted', 200

if __name__ == '__main__':
    app.run()