# import library
from flask import Flask
from flask import render_template, redirect, request, url_for, flash

# import Questions from dictionaries files
from dictionaries import QUIZNO1, QUIZNO2, QUIZNO3, QUIZNO4


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='VeryHardKey2Gu3es!',
))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/quiz1', methods=['GET', 'POST'])
def quiz1():

    if request.method == 'POST':
        points = 0
        answers = request.form

        for qnr, ans in answers.items():
            if ans == QUIZNO1[int(qnr)]['correct']:
                points += 1

        flash('Correct answers: {0}/9'.format(points))
        return redirect(url_for('quiz1_result'))

    return render_template('quiz1.html', questions=QUIZNO1)


@app.route('/quiz1_result')
def quiz1_result():
    return render_template('quiz1_result.html')


@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
    if request.method == 'POST':
        points = 0
        answers = request.form

        for qnr, ans in answers.items():
            if ans == QUIZNO2[int(qnr)]['correct']:
                points += 1

        flash('Correct answers: {0}/9'.format(points))
        return redirect(url_for('quiz2_result'))

    return render_template('quiz2.html', questions=QUIZNO2)


@app.route('/quiz2_result')
def quiz2_result():

    return render_template('quiz2_result.html')


@app.route('/quiz3', methods=['GET', 'POST'])
def quiz3():

    if request.method == 'POST':
        points = 0
        answers = request.form

        for qnr, ans in answers.items():
            if ans == QUIZNO3[int(qnr)]['correct']:
                points += 1

        flash('Correct answers: {0}/9'.format(points))
        return redirect(url_for('quiz3_result'))

    return render_template('quiz3.html', questions=QUIZNO3)


@app.route('/quiz3_result')
def quiz3_result():
    return render_template('quiz3_result.html')


@app.route('/quiz4', methods=['GET', 'POST'])
def quiz4():

    if request.method == 'POST':
        points = 0
        answers = request.form

        for qnr, ans in answers.items():
            if ans == QUIZNO4[int(qnr)]['correct']:
                points += 1

        flash('Correct answers: {0}/9'.format(points))
        return redirect(url_for('quiz4_result'))

    return render_template('quiz4.html', questions=QUIZNO4)


@app.route('/quiz4_result')
def quiz4_result():
    return render_template('quiz4_result.html')


if __name__ == '__main__':
    app.run(debug=True)
