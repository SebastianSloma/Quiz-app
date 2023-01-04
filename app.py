from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!11</h1>'


if __name__ == '__main__':
    app.run(debug=True)