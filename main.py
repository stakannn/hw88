from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    main = url_for('main_page')
    ques = url_for('questions')
    res = url_for('results')
    return render_template('index.html', main=main, ques=ques, res=res)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/questions')
def questions():
    main = url_for('main_page')
    res = url_for('results')
    return render_template('ques.html', main=main, res=res)

@app.route('/results')
def results():
    main = url_for('main_page')
    ques = url_for('questions')
    return render_template('res.html', main=main, ques=ques)

if __name__ == '__main__':
    app.run(debug=True)