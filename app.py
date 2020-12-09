from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    main = url_for('index')
    q = url_for('questions')
    s = url_for('statistics')
    r = url_for('research')
    return render_template('index.html', main=main, q=q, s=s, r=r)

@app.route('/questions')
def questions():
    main = url_for('index')
    s = url_for('statistics')
    r = url_for('research')
    return render_template('questions.html', main=main, s=s, r=r)

@app.route('/statistics')
def statistics():
    main = url_for('index')
    r = url_for('research')
    return render_template('statistics.html', main=main, r=r)

@app.route('/research')
def research():
    main = url_for('index')
    s = url_for('statistics')
    return render_template('research.html', main=main, s=s)

if __name__ == '__main__':
    app.run(debug=False)
