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
 return render_template('administrador/index.html')

@bp.route('/admin/producto')
def producto():
 dataC = Categoria.query.all()
 dataP = Producto.query.all()
 return render_template('administrador/producto.html', dataP=dataP, dataC=dataC)




