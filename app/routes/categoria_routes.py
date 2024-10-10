from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os, app
from app import db
from app.models.producto import Producto
from app.models.categoria import Categoria

bp = Blueprint('categoria', __name__)

@bp.route('/categoria/index')
def index():
    dataC=Categoria.query.all()
    return render_template('administrador/categoria.html', dataC=dataC)   


@bp.route('/categoria/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        imagen = request.files['imagen']

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')
            print(f"imagen dir ------- {imagen_dir}")
            if not os.path.exists(imagen_dir):
                os.makedirs(imagen_dir)  
            imagen.save(os.path.join(imagen_dir, filename))
            ruta_imagen = os.path.join('static', 'images', filename)
            print(f"ruta de la imagen {ruta_imagen}")
        else:
            ruta_imagen = None
        
        new_categoria = Categoria(
            nombre=nombre,
                    imagen=filename
            )
        
        db.session.add(new_categoria)
        db.session.commit()
        
        return redirect(url_for('categoria.index'))

    return render_template('administrador/categoria.html')

@bp.route('/categoria/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if current_user.rol == "Administrador":
        categoria = Categoria.query.get_or_404(id)
        if request.method == 'POST':
            categoria.nombre = request.form['nombre']
            db.session.commit()
            return redirect(url_for('categoria.index'))
        return render_template('administrador/categoria.html', categoria=categoria)
    else:
        return redirect(url_for('auth.index'))
    

@bp.route('/categoria/delete/<int:id>', methods=['POST'])
def delete(id):
    try: 
        if current_user.rol == "Administrador":
            categoria = Categoria.query.get_or_404(id)
            productos_asociados = Producto.query.filter_by(id=id).all()

            for producto in productos_asociados:
                db.session.delete(producto)
            
            db.session.delete(categoria)
            db.session.commit()
            flash('La categoría se eliminó exitosamente', 'info')

            return redirect(url_for('categoria.index'))
        else:
            return redirect(url_for('auth.index'))
    except:
        flash('La categoría no se puede eliminar porque se está usando el registro en otras tablas', 'danger')
        return redirect(url_for('categoria.index'))
    



@bp.route('/categoria/productos/<int:categoria_id>', methods=['GET'])
@login_required
def productos_por_categoria(categoria_id):
    productos = Producto.query.filter_by(categoria=categoria_id).all()
    productos_list = [{
        'nombre': producto.nombre,
        'cantidad': producto.cantidad,
        'precio': producto.precio,
        'imagen': producto.imagen,
    } for producto in productos]

    return jsonify(productos_list)