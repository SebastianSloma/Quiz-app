# import library
from flask import Flask
from flask import render_template, redirect, request, url_for, flash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'VeryHardKey2Gu3es!'

quiz_no1 = [{
            'question': 'What is a correct syntax to output "Hello World" in Python?',
            'answer': ['echo("Hello Wolrd")', 'print("Hello World")', 'p("Hello World")'],
            'correct': 'print("Hello World")'},
            {
            'question': 'Which is a valid variable name in Python?',
            'answer': ['1_data', 'old-data', '_output'],
            'correct': '_output'},
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
            'answer': ['x = "Hello".sub(0, 1)', 'x = sub("Hello", 0, 1)', 'x = sub("Hello")[0]'],
            'correct': ''}
            ]

quiz_no2 = [{
            'question': 'Which method can be used to remove any whitespace from both the beginning and the end of a string?',
            'answer': ['trim()', 'len()', 'strip()'],
            'correct': ''},
            {
            'question': 'Which method can be used to return a string in upper case letters?',
            'answer': ['upper()', 'uppercase()', 'touppercase()'],
            'correct': ''},
            {
            'question': 'Which method can be used to replace parts of a string?',
            'answer': ['repl()', 'replace()', 'switch()'],
            'correct': ''},
            {
            'question': 'Which operator is used to multiply numbers?',
            'answer': ['%', 'x', '*'],
            'correct': ''},
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
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''}
            ]

quiz_no4 = [{
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''},
            {
            'question': '',
            'answer': ['', '', ''],
            'correct': ''}
            ]

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
