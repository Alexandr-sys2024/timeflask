from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Текущее время</title>
        <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css'>
    </head>
    <body class='text-center mt-5'>
        <h1 class='text-primary'>Текущее время:</h1>
        <p class='fs-3'>{current_time}</p>
        <a href='/api/time' class='btn btn-success'>Получить время в JSON</a>
    </body>
    </html>
    """

@app.route("/api/time")
def get_time():
    return jsonify({"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

if __name__ == "__main__":
    app.run(debug=True)