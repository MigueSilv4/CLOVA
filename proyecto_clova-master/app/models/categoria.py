from app import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    productos = db.relationship('Producto', backref='categoria', lazy=True)
