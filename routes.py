from flask import render_template, url_for, request, flash, redirect
import forms
from app import app, database, bcrypt
from models import Usuario
from flask_login import login_user, logout_user, current_user

lista_usuarios = [ 'Jonas', 'Amanda', 'Helena', 'Pipoca', 'Pantera' ]


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/users')
def usuarios():
    return render_template('users.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=[ 'GET', 'POST' ])
def login():
    form_login = forms.FormLogin()
    form_criar_conta = forms.FormCriarConta()

    if form_login.validate_on_submit() and 'btn_submit_login' in request.form:
        user = Usuario.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, form_login.senha.data):
            login_user(user, remember=form_login.check_lembrar_dados.data)
            flash(f'Seja bem vindo {user.username}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'E-mail ou senha incorreta', 'alert-danger')

    if form_criar_conta.validate_on_submit() and 'btn_submit_criar_conta' in request.form:
        cripto_hash = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        user, mail, pwd = form_criar_conta.username.data, form_criar_conta.email.data, cripto_hash
        usuario = Usuario(username=user, email=mail, senha=pwd)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso para {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)


@app.route('/sair')
def sair():
    logout_user()
    flash('Logout realizado com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')


@app.route('/post/new')
def post_new():
    return render_template('post-new.html')

