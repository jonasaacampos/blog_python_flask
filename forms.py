from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import Usuario
from flask_login import current_user


# pip install email-validator


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    senha_confimacao = PasswordField('digite novamamente sua senha:', validators=[EqualTo('senha')])
    btn_submit_criar_conta = SubmitField('Criar Conta')

    ## ! SEMPRE usar iniciar função de validação com 'validate_'
    def validate_email(self, email):
        user_mail = Usuario.query.filter_by(email=email.data).first()
        if user_mail:
            raise ValidationError('E-mail já cadastrado. Utilize outro email ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('senha:', validators=[DataRequired(), Length(6, 20)])
    check_lembrar_dados = BooleanField('Lembrar dados de acesso')
    btn_submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('e-mail:', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto Perfil', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])

    check_skill_python = BooleanField('Python')
    check_skill_flask = BooleanField('Flask')
    check_skill_django = BooleanField('Django')
    check_skill_java = BooleanField('Java')
    check_skill_oop = BooleanField('OOP')

    btn_submit_profile_edit = SubmitField('Salvar edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            user_mail = Usuario.query.filter_by(email=email.data).first()
            if user_mail:
                raise ValidationError('E-mail já cadastrado para outro usuário.')
