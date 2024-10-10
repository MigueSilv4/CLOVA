from flask_login import UserMixin
from app import db
import os  
from flask import url_for, current_app

class Usuario(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.String(120), nullable=False)