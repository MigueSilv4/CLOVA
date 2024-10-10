from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.ofertas import Ofertas
from app.models.producto import Producto
from .. import db
bp = Blueprint('auth', __name__)

@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if Usuario.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado.', 'danger')
            return redirect(url_for('auth.register'))

        nuevo_usuario = Usuario(nombre=nombre, email=email, password=password, rol='Usuario') 
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario registrado exitosamente.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar el usuario: {str(e)}', 'danger')
            return redirect(url_for('auth.register'))

    return render_template('usuario/register.html')  

@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            usuario = Usuario.query.filter_by(email=email).first()
            
            if not usuario:
                flash('El correo electrónico no está registrado.', 'danger')
                return redirect(url_for('auth.login'))

            if usuario.password != password :
                flash('La contraseña es incorrecta.', 'danger')
                return redirect(url_for('auth.login'))

            login_user(usuario)
            
            if usuario.rol == "Usuario":
                return redirect(url_for('landing.index'))  
            elif usuario.rol == "Administrador":
                return redirect(url_for('admin.index'))
            else:
                flash('Rol no autorizado.', 'danger')
                return redirect(url_for('auth.login'))

        except Exception as e:
            flash(f'Error al iniciar sesión: {str(e)}', 'danger')
            return redirect(url_for('auth.login'))
    
    return render_template("usuario/login.html")

@bp.route('/auth/dashboard')
def dashboard():    
    return redirect(url_for('categoria.index'))

@bp.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesion.', 'danger')
    return redirect(url_for('auth.login'))

@bp.route('/auth/deleteUsuario/<int:id>', methods=['POST'])
def delete(id):
        if current_user.rol == "Administrador":
            usuario = Usuario.query.get_or_404(id)
            
            db.session.delete(usuario)
            db.session.commit()
            flash('El usuario se eliminó exitosamente', 'info')

            return redirect(url_for('admin.clientes'))
