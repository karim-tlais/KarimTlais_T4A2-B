from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:1962@localhost/diary'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://cnotxobzwgzncz:42c1670ab07b580fdbac2ebde20f5fd35650dde3397ca355e0a6300cd5e0e2de@ec2-54-145-249-177.compute-1.amazonaws.com:5432/dejnqbve7qnjdq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login_route'    

from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)

from models.User import get_user

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)