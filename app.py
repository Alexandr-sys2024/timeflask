from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
    <head>
        <title>Текущее время</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="d-flex flex-column align-items-center justify-content-center vh-100">
        <h1 class="mb-3">Текущее время:</h1>
        <p class="fs-3">{current_time}</p>
        <a href="/api/time" class="btn btn-primary mt-3">Получить JSON</a>
    </body>
    </html>
    """

@app.route("/api/time")
def api_time():
    return jsonify({"current_time": datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(debug=True)
