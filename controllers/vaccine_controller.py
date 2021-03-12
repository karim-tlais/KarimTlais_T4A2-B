from models.Vaccine import Vaccine
from main import db
from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for
from flask_login import login_required, current_user


vaccination = Blueprint('vaccination',__name__, url_prefix="/")
vprocess = Blueprint('vprocess',__name__,url_prefix="/")
vaccine = Blueprint('vaccine',__name__, url_prefix="/")


@vaccination.route('/vaccination')
@login_required
def vaccination_route():
    result = Vaccine.query.all()
    return render_template('vaccination.html', result=result)

@vaccine.route('/vaccination/vaccine')
@login_required
def vaccine_route():
   return render_template('vaccine.html')


@vprocess.route('/vaccination/vaccine/vprocess',methods = ['POST'])
@login_required
def vprocess_route():
	vaccine = request.form['vaccine']
	date = request.form['date']
	next_due = request.form['next_due']
	diarydata =Vaccine(vaccine=vaccine,date=date,next_due=next_due)
	db.session.add(diarydata)
	db.session.commit()
	return redirect(url_for('vaccination.vaccination_route'))