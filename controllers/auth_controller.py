from models.User import User , LoginForm , RegisterForm
from main import db
from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


login = Blueprint('login',__name__, url_prefix="/")
signup = Blueprint('signup',__name__,url_prefix="/")
logout = Blueprint('logout',__name__, url_prefix="/")


@login.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index.index_load'))

        return render_template('login.html', form=form)


    return render_template('login.html', form=form)

@signup.route('/signup', methods=['GET', 'POST'])
def signup_route():
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
            return abort(400, description="email already exists") 


        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login.login_route'))
        

    return render_template('signup.html', form=form)


@logout.route('/logout')
@login_required
def logout_route():
    logout_user()
    return redirect(url_for('login.login_route'))
