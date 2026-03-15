# Код создаёт простое Flask-приложение с двумя роутами: 
/ возвращает строку «Hello, World!»
/version отображает значение переменной окружения APP_VERSION; 

приложение запускается на всех сетевых интерфейсах (0.0.0.0) в продакшн-режиме (debug=False).

from flask import Flask
import os

app = Flask(__name__)
version = os.environ['APP_VERSION']

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/version')
def show_version():
    return version

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
