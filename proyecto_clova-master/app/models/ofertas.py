from app import db

class Ofertas (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    porcentaje = db.Column(db.Integer, nullable=False)
    fecha_oferta = db.Column(db.Date, nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))