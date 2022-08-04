from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# pip install email-validator


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    senha_confimacao = PasswordField('digite novamamente sua senha:', validators=[EqualTo('senha')])
    btn_submit_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    check_lembrar_dados = BooleanField('Lembrar dados de acesso')
    btn_submit_login = SubmitField('Login')
