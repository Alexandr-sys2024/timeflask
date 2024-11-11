from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Получаем текущие дату и время
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Отображаем их на главной странице
    return f"<h1>Текущие дата и время:</h1><p>{current_time}</p>"

if __name__ == "__main__":
    # Запускаем приложение на локальном сервере
    app.run(debug=True)
