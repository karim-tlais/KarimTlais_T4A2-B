from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:1962@localhost/diary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Profile(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	pet_name = db.Column(db.String(30))
	pet_breed = db.Column(db.String(30))
	pet_dob = db.Column(db.String(30))
	pet_sex = db.Column(db.String(30))

class Vaccine(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	vaccine = db.Column(db.String(30))
	date = db.Column(db.String(30))
	next_due = db.Column(db.String(30))
	

@app.route('/')
def index():
    result = Profile.query.all()
    return render_template('index.html', result=result)

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/process',methods = ['POST'])
def process():
	pet_name = request.form['pet_name']
	pet_breed = request.form['pet_breed']
	pet_dob = request.form['pet_dob']
	pet_sex = request.form['pet_sex']
	diarydata =Profile(pet_name=pet_name,pet_breed=pet_breed, pet_dob=pet_dob,pet_sex=pet_sex)
	db.session.add(diarydata)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/vaccination/vprocess',methods = ['POST'])
def vprocess():
	vaccine = request.form['vaccine']
	date = request.form['date']
	next_due = request.form['next_due']
	diarydata =Vaccine(vaccine=vaccine,date=date,next_due=next_due)
	db.session.add(diarydata)
	db.session.commit()
	return redirect(url_for('vaccination'))

@app.route('/vaccination/vaccine')
def vaccine():
   return render_template('vaccine.html')

@app.route('/vaccination')
def vaccination():
    result = Vaccine.query.all()
    return render_template('vaccination.html', result=result)
