from main import database
from datetime import datetime


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    user_photo = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='post_author', lazy=True)
    skills = database.Column(database.String, nullable=False, default='Não informado')


class Post(database.Model):
    # ForeinKey # mesmo o nome da classe sendo maiúscula, o valor a ForeinKey
    # deverá SEMPRE ser minúsculo (superstição da biblioteca...)
    ##########################################################################
    # Date # para armazenar a data, passamos a função sem os () no formato UTC


    id = database.Column(database.Integer, primary_key=True)
    post_title = database.Column(database.String, nullable=False)
    post_text = database.Column(database.Text, nullable=False)
    post_created_at = database.Column(database.DATETIME, nullable=False, default=datetime.utcnow)
    id_author = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
