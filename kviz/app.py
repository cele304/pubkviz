from flask import Flask, render_template, request, session
from flask_session import Session
import pandas as pd
import random
#import webbrowser

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


questions = pd.read_excel('questions.xlsx')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = questions.loc[session['current_question'], 'Answer']

        if user_answer.lower() == correct_answer.lower():
            result = 'Točno!'
        else:
            result = 'Netočno!'

        return render_template('quiz.html', result=result, correct_answer=correct_answer)

    session['current_question'] = random.randint(0, len(questions) - 1)
    current_question = questions.loc[session['current_question'], 'Question']
    return render_template('quiz.html', question=current_question)

if __name__ == '__main__':
    #webbrowser.open('http://localhost:5000')
    app.run(debug=True)
