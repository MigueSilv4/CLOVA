from flask import Blueprint, render_template
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.models.usuario import Usuario
from app import db
import os


bp = Blueprint('admin', __name__)

@bp.route('/admin')
def index():
 dataU = Usuario.query.all()
 tamañoU = len(dataU)
 dataC = Categoria.query.all()
 tamañoC = len(dataC)
 dataP = Producto.query.all()
 tamañoP = len(dataP)
 return render_template('administrador/index.html', tamañoU=tamañoU, dataU=dataU, dataC=dataC, tamañoC=tamañoC, dataP=dataP, tamañoP=tamañoP)

@bp.route('/admin/producto')
def producto():
 dataC = Categoria.query.all()
 dataP = Producto.query.all()
 return render_template('administrador/producto.html', dataP=dataP, dataC=dataC)

@bp.route('/admin/clientes')
def clientes():
    dataU = Usuario.query.all()
    usuario = current_user

    return render_template('administrador/cliente.html', dataU=dataU, usuario=usuario)




