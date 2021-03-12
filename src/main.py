from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:1962@localhost/diary'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://lyusbfspcfviju:d831a4b81bc9802a6f1a0aec98096292fd892339a0cb864cc1a47875fcafb8b9@ec2-54-145-249-177.compute-1.amazonaws.com:5432/dcdsp9c5kjs7q5'
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