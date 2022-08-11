from app import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_user):
    return Usuario.query.get(int(id_user))


"""
Para testar o banco de dados:
- from app import database || database.create_all()
fazer alguma insersao de novo usuario
- from models import Usuario || Usuario.query.all() || uario = Usuario.query.first() || usuario.username
...
user2 = Usuario.query.filter_by(username='teste2').first()
Usuario[1].senha

## limpar base de dados de teste
database.drop_all()
database.create_all()

"""


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    user_photo = database.Column(database.String, default='default_profile_img.png')
    posts = database.relationship('Post', backref='author', lazy=True)
    skills = database.Column(database.String, nullable=False, default=0)


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
