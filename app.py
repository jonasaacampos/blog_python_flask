from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=1)
