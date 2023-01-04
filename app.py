# import library
from flask import Flask
from flask import render_template, redirect, request, url_for, flash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'VeryHardKey2Gu3es!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/quiz1')
def quiz1():
    return render_template('quiz1.html')


@app.route('/quiz1_result')
def quiz1_result():
    return render_template('quiz1_result.html')


@app.route('/quiz2')
def quiz2():
    return render_template('quiz2.html')


@app.route('/quiz2_result')
def quiz2_result():
    return render_template('quiz2_result.html')


@app.route('/quiz3')
def quiz3():
    return render_template('quiz3.html')


@app.route('/quiz3_result')
def quiz3_result():
    return render_template('quiz3_result.html')


@app.route('/quiz4')
def quiz4():
    return render_template('quiz4.html')


@app.route('/quiz4_result')
def quiz4_result():
    return render_template('quiz4_result.html')


if __name__ == '__main__':
    app.run(debug=True)
