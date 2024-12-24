from .import db

class LineaBlanca(db.Model):
    __tablename__ = 'linea_blanca'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    capacidad = db.Column(db.String(50), nullable=True)
    tipo = db.Column(db.String(50), nullable=True)
    eficiencia_energetica = db.Column(db.String(10), nullable=True)
