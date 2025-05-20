from flask import Flask, request, jsonify
from threat_module import detect_threat
from logger import log_threat

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    ip = request.remote_addr
    threat = detect_threat(data, ip, 'login')

    if threat:
        log_threat(ip, threat, data)
        return jsonify({'status': 'threat_detected', 'message': threat}), 403

    if data.get("username") == "admin" and data.get("password") == "admin":
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'invalid credentials'}), 401

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    ip = request.remote_addr
    threat = detect_threat(data, ip, 'upload')

    if threat:
        log_threat(ip, threat, data)
        return jsonify({'status': 'threat_detected', 'message': threat}), 403

    return jsonify({'status': 'upload successful'})

if __name__ == '__main__':
    app.run(debug=True)