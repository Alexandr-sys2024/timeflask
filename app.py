from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html lang='ru'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Текущее время</title>
        <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet'>
    </head>
    <body class='d-flex flex-column justify-content-center align-items-center vh-100 bg-light'>
        <div class='text-center'>
            <h1 class='mb-3'>Текущее время</h1>
            <p class='fs-4 bg-white p-3 shadow rounded'>{current_time}</p>
        </div>
    </body>
    </html>
    """

@app.route("/api/time")
def api_time():
    return jsonify({"current_time": datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(debug=True)