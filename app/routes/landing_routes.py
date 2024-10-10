from flask import Blueprint, render_template
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.models.usuario import Usuario
from app import db
import os


bp = Blueprint('landing', __name__)

@bp.route('/')
def index():
    dataP=Producto.query.all()
    dataC=Categoria.query.all()
    return render_template('landing/index.html', dataP=dataP, dataC=dataC)