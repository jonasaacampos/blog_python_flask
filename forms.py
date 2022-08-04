from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário:')
    email = StringField('e-mail:')
    senha = PasswordField('senha:')
    senha_confimacao = StringField('digite novamamente sua senha:')
    btn_submit = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email = StringField('e-mail:')
    senha = PasswordField('senha:')
    btn_submit = SubmitField('Login')
