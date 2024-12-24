from .import db 

class Alimento(db.Model):
    __tablename__ = 'alimentos'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    fecha_caducidad = db.Column(db.Date, nullable=True)
    peso = db.Column(db.Numeric(10, 2), nullable=True)  # En kilogramos o gramos
    tipo_alimento = db.Column(db.String(50), nullable=True)