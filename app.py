# import library
from flask import Flask
from flask import render_template, redirect, request, url_for, flash


app = Flask(__name__)

app.config.update(dict(SECRET_KEY = 'VeryHardKey2Gu3es!',))

quiz_no1 = [{
            'question': 'What is a correct syntax to output "Hello World" in Python?',
            'answer': ['echo("Hello Wolrd")', 'print("Hello World")', 'p("Hello World")'],
            'correct': 'print("Hello World")'},
            {
            'question': 'Which is a valid variable name in Python?',
            'answer': ['1_data', 'old-data', 'new_data'],
            'correct': 'new_data'},
            {
            'question': 'How do you insert COMMENTS in Python code?',
            'answer': ['#This is a comment', '//This is a comment', '/*This is a comment*/'],
            'correct': '#This is a comment'},
            {
            'question': 'How do you create a variable with the numeric value 5?',
            'answer': ['x=5', 'x=int(5)', 'Both answers are correct'],
            'correct': 'Both answers are correct'},
            {
            'question': 'What is the correct file extension for Python files?',
            'answer': ['.py', '.pyt', '.pt'],
            'correct': '.py'},
            {
            'question': 'How do you create a variable with the floating number 2.8',
            'answer': ['x=2.8', 'x=float(2.8)', 'Both answers are correct'],
            'correct': 'Both answers are correct'},
            {
            'question': 'What is the correct syntax to output the type of a variable or object in Python?',
            'answer': ['print(typeOf(x))', 'print(typeof x)', 'print(type(x))'],
            'correct': 'print(type(x))'},
            {
            'question': 'What is the correct way to create a function in Python?',
            'answer': ['function myFunction():', 'def myFunction():', 'create myFunction():'],
            'correct': 'def myFunction():'},
            {
            'question': 'What is a correct syntax to return the first character in a string?',
            'answer': ['x = "Hello".sub(0, 1)', 'x = sub("Hello", 0, 1)', 'x = "Hello"[0]'],
            'correct': 'x = "Hello"[0]'}
            ]

quiz_no2 = [{
            'question': 'Which method can be used to remove any whitespace from both the beginning and the end of a string?',
            'answer': ['trim()', 'len()', 'strip()'],
            'correct': 'strip()'},
            {
            'question': 'Which method can be used to return a string in upper case letters?',
            'answer': ['upper()', 'uppercase()', 'touppercase()'],
            'correct': 'upper()'},
            {
            'question': 'Which method can be used to replace parts of a string?',
            'answer': ['repl()', 'replace()', 'switch()'],
            'correct': 'replace()'},
            {
            'question': 'Which operator is used to multiply numbers?',
            'answer': ['%', 'x', '*'],
            'correct': '*'},
            {
            'question': 'Which operator can be used to compare two values?',
            'answer': ['==', '><', '='],
            'correct': '=='},
            {
            'question': 'Which of these collections defines a LIST?',
            'answer': ['{"name" : "apple", "color" : "red"}', '("apple", "banana", "cherry")', '["apple", "banana", "cherry"]'],
            'correct': '["apple", "banana", "cherry"]'},
            {
            'question': 'Which of these collections defines a TUPLE?',
            'answer': ['{"apple", "banana", "cherry"}', '("apple", "banana", "cherry")', '["apple", "banana", "cherry"]'],
            'correct': '("apple", "banana", "cherry")'},
            {
            'question': 'Which of these collections defines a SET?',
            'answer': ['{"apple", "banana", "cherry"}', '("apple", "banana", "cherry")', '["apple", "banana", "cherry"]'],
            'correct': '{"apple", "banana", "cherry"}'},
            {
            'question': 'Which of these collections defines a DICTIONARY?',
            'answer': ['("apple", "banana", "cherry")', '{"apple", "banana", "cherry"}', '{"name" : "apple", "color" : "red"}'],
            'correct': '{"name" : "apple", "color" : "red"}'}
            ]

quiz_no3 = [{
            'question': 'Which collection is ordered, changeable, and allows duplicate members?',
            'answer': ['set', 'dictionary', 'list'],
            'correct': 'list'},
            {
            'question': 'Which collection does not allow duplicate members?',
            'answer': ['set', 'list', 'tuple'],
            'correct': 'set'},
            {
            'question': 'How do you start writing an if statement in Python?',
            'answer': ['if x > y then:', 'if (x > y)', 'if x > y:'],
            'correct': 'if x > y:'},
            {
            'question': 'How do you start writing a while loop in Python?',
            'answer': ['while x > y:', 'x > y while', 'while (x > y)'],
            'correct': 'while x > y:'},
            {
            'question': 'How do you start writing a for loop in Python?',
            'answer': ['for each x in y:', 'for x in y:', 'for x > y:'],
            'correct': 'for x in y:'},
            {
            'question': 'Which statement is used to stop a loop?',
            'answer': ['exit', 'break', 'stop'],
            'correct': 'break'},
            {
            'question': 'Which one is NOT a legal variable name?',
            'answer': ['my-var', 'my_var', '_myvar'],
            'correct': 'my-var'},
            {
            'question': 'Which language is Django written in?',
            'answer': ['Java', 'Python', 'C'],
            'correct': 'Python'},
            {
            'question': 'What is the name of the package manager for Python packages, or modules?',
            'answer': ['Matplotlib', 'TensorFlow', 'PIP'],
            'correct': 'PIP'}
            ]

quiz_no4 = [{
            'question': 'Which keyword allows us to load a module in Python?',
            'answer': ['Import', 'Load', 'Include'],
            'correct': 'Import'},
            {
            'question': 'What manages memory in Python?',
            'answer': ['Memory cache', 'Private heap space', 'Development space'],
            'correct': 'Private heap space'},
            {
            'question': 'What command can you use to delete a file in Python?',
            'answer': ['Os.delete (filename)', 'Os.remove (filename)', 'Os.clean (filename)'],
            'correct': 'Os.remove (filename)'},
            {
            'question': 'What is the use of // operator in Python?',
            'answer': ['Or', 'Separation', 'Division'],
            'correct': 'Division'},
            {
            'question': 'Python is designed by:',
            'answer': ['Guido van Rossum', 'Dennis Ritchie', 'Google'],
            'correct': 'Guido van Rossum'},
            {
            'question': 'Python first appeared in:',
            'answer': ['January 1982', 'December 1987', 'February 1991'],
            'correct': 'February 1991'},
            {
            'question': 'Python is used for:',
            'answer': ['Web development (server-side) and software development', 'Mathematics and system scripting', 'Both answers are correct'],
            'correct': 'Both answers are correct'},
            {
            'question': 'What module is most commonly used when working with directories?',
            'answer': ['OS moudle', 'Pandas module', 'Numpy module'],
            'correct': 'OS moudle'},
            {
            'question': 'What symbol is used to decorate a function?',
            'answer': ['?', '@', '&'],
            'correct': '@'}
            ]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/quiz1', methods=['GET','POST'])
def quiz1():

    if request.method == 'POST':
        points = 0
        answer = request.form

        for num, ans in answer.items():
            if ans == quiz_no1[int(num)]['correct']:
                points += 1
        
        flash('Correct answers: {0}'.format(points))
        return redirect(url_for('quiz1'))

    return render_template('quiz1.html', questions=quiz_no1)


@app.route('/quiz1_result')
def quiz1_result():
    return render_template('quiz1_result.html')


@app.route('/quiz2', methods=['GET','POST'])
def quiz2():
    if request.method == 'POST':
        points = 0
        answer = request.form

        for num, ans in answer.items():
            if ans == quiz_no1[int(num)]['correct']:
                points += 1
        
        flash('Correct answers: {0}'.format(points))
        return redirect(url_for('quiz2_result'))
    return render_template('quiz2.html',questions_2=quiz_no2)


@app.route('/quiz2_result')
def quiz2_result():
    
    return render_template('quiz2_result.html')


@app.route('/quiz3', methods=['GET','POST'])
def quiz3():

    if request.method == 'POST':
        points = 0
        answer = request.form

        for num, ans in answer.items():
            if ans == quiz_no1[int(num)]['correct']:
                points += 1
        
        flash('Correct answers: {0}'.format(points))
        return redirect(url_for('quiz3_result'))
    return render_template('quiz3.html',questions_3=quiz_no3)


@app.route('/quiz3_result')
def quiz3_result():
    return render_template('quiz3_result.html')


@app.route('/quiz4', methods=['GET','POST'])
def quiz4():

    if request.method == 'POST':
        points = 0
        answer = request.form

        for num, ans in answer.items():
            if ans == quiz_no1[int(num)]['correct']:
                points += 1
        
        flash('Correct answers: {0}'.format(points))
        return redirect(url_for('quiz4_result'))
    return render_template('quiz4.html',questions_4=quiz_no4)


@app.route('/quiz4_result')
def quiz4_result():
    return render_template('quiz4_result.html')


if __name__ == '__main__':
    app.run(debug=True)
