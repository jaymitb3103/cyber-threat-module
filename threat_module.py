def detect_threat(data, ip, endpoint):
    injection_keywords = ["'", "\"", ";", "--", " OR ", " AND "]

    for key, value in data.items():
        if isinstance(value, str):
            for keyword in injection_keywords:
                if keyword.lower() in value.lower():
                    return "Possible SQL Injection"
    return None