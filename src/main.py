from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:1962@localhost/events'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	date = db.Column(db.String(30))
	event = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Todo.query.all()
    return render_template('index.html', result=result)

@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/process',methods = ['POST'])
def process():
    date = request.form[ 'date']
    event = request.form['event']
    eventdata = Todo(date=date,event=event)
    db.session.add(eventdata)
    db.session.commit()
    return redirect(url_for('index'))
