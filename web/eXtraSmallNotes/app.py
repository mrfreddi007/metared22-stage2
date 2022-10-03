import os
from flask import Flask, render_template

app = Flask(__name__)
APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = os.getenv('APP_PORT', '8000')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=False)
