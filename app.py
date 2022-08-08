from flask import Flask, render_template, url_for, request, flash, redirect
from credentials import get_secret
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

TOKEN = get_secret('TOKEN')
app.config['SECRET_KEY'] = TOKEN
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)


from routes import home, contato, usuarios, login