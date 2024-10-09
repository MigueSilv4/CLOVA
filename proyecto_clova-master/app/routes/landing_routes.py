from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.producto import Producto
from app.models.categoria import Categoria

bp = Blueprint('landing', __name__)

@bp.route('/')
def index():
    return render_template('landing/index.html')    