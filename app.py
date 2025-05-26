from flask import Flask, request, jsonify

app = Flask(__name__)

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == "admin" and password == "admin":
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Dummy threat indicators
blacklisted_ips = ["192.168.1.100", "10.0.0.66"]
suspicious_keywords = ["attack", "malware", "unauthorized", "hack", "breach"]

# Threat detection route
@app.route('/detect-threat', methods=['POST'])
def detect_threat():
    data = request.get_json()
    log = data.get("log", "")
    ip = data.get("ip", "")

    result = {
        "ip_flagged": ip in blacklisted_ips,
        "keyword_detected": any(word in log.lower() for word in suspicious_keywords)
    }

    if result["ip_flagged"] or result["keyword_detected"]:
        result["status"] = "Threat Detected"
    else:
        result["status"] = "Safe"

    return jsonify(result)
