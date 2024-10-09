from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.ofertas import Ofertas
from app.models.producto import Producto

bp = Blueprint('auth', __name__)

@bp.route('/auth/index')
def index():
    return render_template('inicio/index.html')

@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if (usuario := Usuario.query.filter_by(email=email, password=password).first()):
            login_user(usuario)
            flash("Ingreso exitoso!", "success")
            return redirect(url_for('categoria.index'))
        
        flash('Invalid credentials. Please try again.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    return render_template("usuario/login.html")

@bp.route('/auth/dashboard')
def dashboard():    
    return redirect(url_for('categoria.index'))

@bp.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesion.', 'danger')
    return redirect(url_for('auth.login'))