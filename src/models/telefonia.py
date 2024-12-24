from .import db

class Telefonia(db.Model):
    __tablename__ = 'telefonia'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    marca = db.Column(db.String(50), nullable=True)
    modelo = db.Column(db.String(50), nullable=True)
    almacenamiento = db.Column(db.Integer, nullable=True)  # GB
    ram = db.Column(db.Integer, nullable=True)  # GB