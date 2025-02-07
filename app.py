from flask import Flask, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Текущее время</title>
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet'>
</head>
<body class='d-flex align-items-center justify-content-center vh-100'>
    <div class='text-center'>
        <h1 class='mb-4'>Текущее время</h1>
        <p class='fs-3'>{{ time }}</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, time=current_time)

@app.route("/api/time")
def api_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"current_time": current_time})

if __name__ == "__main__":
    app.run(debug=True)
