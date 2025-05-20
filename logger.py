import json
import os
from datetime import datetime

LOG_FILE = 'logs/threat_log.json'

def log_threat(ip, threat_type, data):
    entry = {
        'ip': ip,
        'threat': threat_type,
        'data': data,
        'time': datetime.now().isoformat()
    }

    if not os.path.exists('logs'):
        os.makedirs('logs')

    try:
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)

    print(f"[LOGGED] Threat from {ip} — {threat_type}")