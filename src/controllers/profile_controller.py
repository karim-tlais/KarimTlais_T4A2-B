from models.Profile import Profile
from main import db
from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for
from flask_login import login_required, current_user


profile = Blueprint('profile',__name__, url_prefix="/")
process = Blueprint('process',__name__,url_prefix="/profile")
index = Blueprint('index',__name__, url_prefix="/")

@index.route('/')
@login_required
def index_load():
    result = Profile.query.all()
    return render_template('index.html', result=result)

@profile.route('/profile')
@login_required
def profile_add():
    return render_template('profile.html')

@process.route('/process',methods = ['POST'])
@login_required
def process_route():
	pet_name = request.form['pet_name']
	pet_breed = request.form['pet_breed']
	pet_dob = request.form['pet_dob']
	pet_sex = request.form['pet_sex']
	diarydata =Profile(pet_name=pet_name,pet_breed=pet_breed, pet_dob=pet_dob,pet_sex=pet_sex)
	db.session.add(diarydata)
	db.session.commit()
	return redirect(url_for('index.index_load'))


	