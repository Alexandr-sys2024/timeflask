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
        <body class="container text-center mt-5">
            <h1 class="display-4">Текущее время</h1>
            <p class="lead">{current_time}</p>
            <a href="/api/time" class="btn btn-primary">Получить JSON</a>
        </body>
    </html>
    """

@app.route("/api/time")
def api_time():
    return jsonify({"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

if __name__ == "__main__":
    app.run(debug=True)