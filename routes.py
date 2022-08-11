from flask import render_template, url_for, request, flash, redirect
import forms
from app import app, database, bcrypt
from models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image


def salvar_imagem(imagem):
    cod_unique = secrets.token_hex(6)
    arquivo_nome, arquivo_extensao = os.path.splitext(imagem.filename)
    novo_arquivo = arquivo_nome + cod_unique + arquivo_extensao
    caminho_arquivo = os.path.join(app.root_path, 'static/img_profiles', novo_arquivo)
    tamanho_img = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho_img)
    imagem_reduzida.save(caminho_arquivo)
    return novo_arquivo


def atualizar_skills(form):
    lista_skills = []
    for campo in form:
        if 'check_skill' in campo.name:
            if campo.data:
                lista_skills.append(campo.label.text)
    return ';'.join(lista_skills)


@app.route('/')
def home():
    posts = Post.query.order_by(Post.id.desc())

    return render_template('home.html', posts=posts)


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/users')
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template('users.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = forms.FormLogin()
    form_criar_conta = forms.FormCriarConta()

    if form_login.validate_on_submit() and 'btn_submit_login' in request.form:
        user = Usuario.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, form_login.senha.data):
            login_user(user, remember=form_login.check_lembrar_dados.data)
            flash(f'Seja bem vindo {user.username}', 'alert-success')
            param_next = request.args.get('next')
            if param_next:
                return redirect(param_next)
            else:
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
@login_required
def sair():
    logout_user()
    flash('Logout realizado com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    profile_image = url_for('static', filename=f'img_profiles/{current_user.user_photo}')
    return render_template('perfil.html', profile_image=profile_image)


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def perfil_editar():
    form = forms.FormEditarPerfil()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data

        if form.foto_perfil.data:
            nova_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.user_photo = nova_imagem

        current_user.skills = atualizar_skills(form)

        database.session.commit()
        flash('Perfil atualizado com sucesso!', 'alert-success')
        return redirect(url_for('perfil'))

    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename=f'img_profiles/{current_user.user_photo}')
    return render_template('perfil_editar.html', profile_image=profile_image, form=form)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def post_new():
    form_new_post = forms.FormCriarPost()
    if form_new_post.validate_on_submit():
        post = Post(post_title=form_new_post.post_title.data, post_text=form_new_post.post_text.data,
                    author=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Postagem criada com sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('post-new.html', form_new_post=form_new_post)


@app.route('/post/<post_id>')
def post_show(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)

## img credit
# flaticon
