from flask import Flask, render_template, url_for
from credentials import get_secret
import forms

app = Flask(__name__)

TOKEN = get_secret('TOKEN')
app.config['SECRET_KEY'] = TOKEN

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


@app.route('/login')
def login():
    form_login = forms.FormLogin()
    form_criar_conta = forms.FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)


if __name__ == '__main__':
    app.run(debug=1)
