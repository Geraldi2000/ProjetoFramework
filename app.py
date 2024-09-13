from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/base')
def hello_world():
    return render_template('index.html', nomeLoja='Puro malte', cat=lista)
    
@app.route('/')
def novo():
    return render_template('main.html')

@app.route('/mvc')
def mvc():
    return render_template('base.html')

@app.route('/frame')
def frame():
    return render_template('Framework.html')

@app.route('/boot')
def boot():
    return render_template('bootstrap.html')

@app.route('/cdn')
def cdn():
    return render_template('cdn.html')

@app.route('/flask')
def flask():
    return render_template('flask.html')

app.run(debug=True)

