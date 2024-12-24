from .import db
class Electrodomestico(db.Model):
    __tablename__ = 'electrodomesticos'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    consumo_energia = db.Column(db.String(50), nullable=True)
    garantia = db.Column(db.Integer, nullable=True)
