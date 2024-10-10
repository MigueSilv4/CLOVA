from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)    
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from .models.usuario import Usuario
        return Usuario.query.get(int(user_id))

    from app.routes import auth_routes, producto_routes, categoria_routes, admin_routes, landing_routes

    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(categoria_routes.bp)
    app.register_blueprint(admin_routes.bp)
    app.register_blueprint(landing_routes.bp)


    @app.route('/')
    def principal():
        return redirect(url_for('auth.login'))



    return app