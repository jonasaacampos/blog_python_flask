from flask import render_template, url_for, request, flash, redirect
import forms
from app import app

lista_usuarios = ['Jonas', 'Amanda', 'Helena', 'Pipoca', 'Pantera']
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
        flash(f'Seja bem vindo {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))

    if form_criar_conta.validate_on_submit() and 'btn_submit_criar_conta' in request.form:
        flash(f'Conta criada com sucesso para {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)
