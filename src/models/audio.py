from .import db

class Audio(db.Model):
    __tablename__ = 'audio'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    tipo_dispositivo = db.Column(db.String(50), nullable=True)
    potencia_watts = db.Column(db.Numeric(10, 2), nullable=True)
    conectividad = db.Column(db.String(50), nullable=True)