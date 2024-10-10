from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from werkzeug.utils import secure_filename
import os, app
from app.models.producto import Producto
from app.models.categoria import Categoria

bp = Blueprint('producto', __name__)

@bp.route('/producto/add', methods=['GET', 'POST'])
def add():
    rol = current_user.rol 
    if rol == "Administrador":  
        if request.method == 'POST':
            try:
                nombre = request.form['nombre']
                precio = request.form['precio']
                cantidad = request.form['cantidad']
                categoria_id = request.form['categoria_id']
                imagen = request.files['imagen']

                if imagen:
                    filename = secure_filename(imagen.filename)
                    imagen_path = os.path.join('static', 'images', filename)
                    imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
                    ruta_imagen = imagen_path
                else:
                    ruta_imagen = None

                new_producto = Producto(
                    nombre=nombre, 
                    precio=precio, 
                    cantidad=cantidad,
                    categoria_id=categoria_id, 
                    imagen=filename
                )
                db.session.add(new_producto)
                db.session.commit()

                flash("Producto guardado con éxito", "success")
                return redirect(url_for('producto.index'))
            
            except Exception as e:

                flash(f"Ocurrió un error: {str(e)}", "danger")
                return redirect(url_for('producto.add'))


        dataC = Categoria.query.all()

        return render_template('administrador/producto.html', dataC=dataC)
    
    else:
        return redirect(url_for('auth.index'))
    



@bp.route('/producto/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if current_user.rol != "Administrador":
        return redirect(url_for('auth.index'))

    dataP = Producto.query.get_or_404(id)
    dataC = Categoria.query.all()

    if request.method == 'POST':
        dataP.nombre = request.form['nombre']
        dataP.precio = request.form['cantidad']
        dataP.cantidad = request.form['cantidad']
        dataP.categoria = request.form['categoria']
        imagen = request.files['imagen']

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'images', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            dataP.imagen = filename

        db.session.commit()
        flash('Producto actualizado con éxito', 'success')
        return redirect(url_for('producto.index'))
    



@bp.route('/producto/delete/<int:id>', methods=['POST','GET'])
@login_required
def delete(id):
    try:    
        if current_user.rol == "Administrador":
            producto = Producto.query.get_or_404(id)
            db.session.delete(producto)
            db.session.commit()
            flash('Producto eliminado con éxito', 'success')
            return redirect(url_for('producto.tabla'))
        else:
            return redirect(url_for('auth.index'))
    except:
        flash('El producto no se puede eliminar porque se está usando el registro en otras tablas', 'danger')
        return redirect(url_for('producto.tabla'))