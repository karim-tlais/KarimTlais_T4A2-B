from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1962@localhost/quotes'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process',methods = ['POST'])
def process():
    author = request.form[ 'author']
    quote = request.form['quote']
    return redirect(url_for('index.html'))
