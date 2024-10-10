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
                    # imagen_path = os.path.join('static', 'images', filename)
                    # print(f"path {imagen_path}")
                    # imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
                    # print(f"os jon {os.path.dirname(__file__)}")
                    # ruta_imagen = imagen_path
                    imagen_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')
                    print(f"imagen dir ------- {imagen_dir}")
                    if not os.path.exists(imagen_dir):
                        os.makedirs(imagen_dir) 
                    imagen.save(os.path.join(imagen_dir, filename))
                    ruta_imagen = os.path.join('static', 'images', filename) 
                    print(f"ruta de la imagen {ruta_imagen}")
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
                return redirect(url_for('admin.producto'))
            
            except Exception as e:
                print(f"exception {e}")
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
        dataP.categoria_id = request.form['categoria_id']
        imagen = request.files['imagen']

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'images', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            dataP.imagen = filename

        db.session.commit()
        flash('Producto actualizado con éxito', 'success')
        return redirect(url_for('admin.producto'))
    



@bp.route('/producto/delete/<int:id>', methods=['POST','GET'])
@login_required
def delete(id):
    try:    
        if current_user.rol == "Administrador":
            producto = Producto.query.get_or_404(id)
            db.session.delete(producto)
            db.session.commit()
            flash('Producto eliminado con éxito', 'success')
            return redirect(url_for('admin.producto'))
        else:
            return redirect(url_for('auth.index'))
    except:
        flash('El producto no se puede eliminar porque se está usando el registro en otras tablas', 'danger')
        return redirect(url_for('admin.producto'))