from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import Usuario


# pip install email-validator


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    senha_confimacao = PasswordField('digite novamamente sua senha:', validators=[EqualTo('senha')])
    btn_submit_criar_conta = SubmitField('Criar Conta')

    def validate_email(self, email):
        user_mail = Usuario.query.filter_by(email=email.data).first()
        if user_mail:
            raise ValidationError('E-mail já cadastrado. Utilize outro email ou faça login para continuar')




class FormLogin(FlaskForm):
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    check_lembrar_dados = BooleanField('Lembrar dados de acesso')
    btn_submit_login = SubmitField('Login')
