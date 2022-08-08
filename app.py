from flask import Flask, render_template, url_for, request, flash, redirect
from credentials import get_secret
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

TOKEN = get_secret('TOKEN')

app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False
app.config[ 'SECRET_KEY' ] = TOKEN
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///site.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # usar o nome da função
login_manager.login_message_category = 'alert-info'


from routes import home, contato, usuarios, login
