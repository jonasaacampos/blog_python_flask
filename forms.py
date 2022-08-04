from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# pip install email-validator


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    senha_confimacao = StringField('digite novamamente sua senha:', validators=[EqualTo('senha')])
    btn_submit = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('e-mail:', validators=[DataRequired()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    btn_submit_login = SubmitField('Login')
