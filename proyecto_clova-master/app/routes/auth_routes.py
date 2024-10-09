from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.ofertas import Ofertas
from app.models.producto import Producto

bp = Blueprint('auth', __name__)

@bp.route('/auth')
def index():
    return render_template('inicio/index.html')

@bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.password == password:  # Nota: Esta comparación no es segura, se debe usar hash
            login_user(usuario)

            if usuario.rol == "Usuario": # nota usuario agregar la ruta de usuario
                return redirect(url_for(''))
            elif usuario.rol == "Administrador": # nota Administrador
                return redirect(url_for('admin.index'))
            else:
                flash('Credenciales inválidas. Por favor, intente nuevamente.', 'danger')
    
    return render_template("usuario/login.html")

@bp.route('/auth/dashboard')
def dashboard():    
    return redirect(url_for('categoria.index'))

@bp.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesion.', 'danger')
    return redirect(url_for('auth.login'))