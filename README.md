# 🛡️ Cyber Threat Detection Module (Flask-Based)

A simple backend module built in Python using Flask to detect basic cyber threats such as SQL injections and suspicious user inputs.

---

## 🚀 Features

- ✅ SQL Injection Detection on login and upload endpoints
- ✅ Logs all detected threats to a JSON file (`logs/threat_log.json`)
- ✅ Lightweight and easy to deploy
- ✅ No frontend needed – test via Postman or cURL

---

## 📁 Folder Structure

```
cyber_threat_module_project/
├── app.py               # Main Flask application
├── threat_module.py     # Core threat detection logic
├── logger.py            # Threat logging functionality
├── requirements.txt     # Dependencies
└── logs/
    └── threat_log.json  # Stores logged threats
```

---

## ⚙️ API Endpoints

### `POST /login`
- **Description**: Authenticates user
- **Threat Detection**: Checks for SQL injections
- **Test Payload**:
```json
{
  "username": "admin",
  "password": "' OR 1=1 --"
}
```

---

### `POST /upload`
- **Description**: Simulates file upload request
- **Threat Detection**: Same injection scan
- **Test Payload**:
```json
{
  "filename": "test.pdf",
  "description": "'; DROP TABLE users --"
}
```

---

## 🧪 How to Test

You can use:
- 🧪 **Postman**
- 💻 `curl` from terminal

Example:
```bash
curl -X POST http://localhost:5000/login      -H "Content-Type: application/json"      -d '{"username":"admin", "password":"admin"}'
```

---

## 🛠 Deployment

You can deploy this easily on platforms like:
- [Railway](https://railway.app)
- [Render](https://render.com)

Just connect your GitHub repo and you're good to go!

---

## 🧾 License

This project is part of a personal cybersecurity learning project by **Jaymit Bhagat**.
Feel free to use it for academic or learning purposes.

---