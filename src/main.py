from flask import Flask , render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:1962@localhost/diary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50),])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))




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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return render_template('login.html', form=form)
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        username = request.form.get('username')
        email = request.form.get('email')
        email_1 = User.query.filter_by(email=email).first()
        user = User.query.filter_by(username=username).first()
        if user:
            return abort(400, description="user already exists")
        elif email_1:
            return abort(400, description="email already exists") , redirect(url_for('index'))


        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
        

    return render_template('signup.html', form=form)

@app.route('/')
@login_required
def index():
    result = Profile.query.all()
    return render_template('index.html', result=result)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/process',methods = ['POST'])
@login_required
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
@login_required
def vprocess():
	vaccine = request.form['vaccine']
	date = request.form['date']
	next_due = request.form['next_due']
	diarydata =Vaccine(vaccine=vaccine,date=date,next_due=next_due)
	db.session.add(diarydata)
	db.session.commit()
	return redirect(url_for('vaccination'))

@app.route('/vaccination/vaccine')
@login_required
def vaccine():
   return render_template('vaccine.html')

@app.route('/vaccination')
@login_required
def vaccination():
    result = Vaccine.query.all()
    return render_template('vaccination.html', result=result)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
