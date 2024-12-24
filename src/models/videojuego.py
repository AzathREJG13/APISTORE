from .import db
class Videojuego(db.Model):
    __tablename__ = 'videojuegos'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    plataforma = db.Column(db.String(50), nullable=True)
    genero = db.Column(db.String(50), nullable=True)
    clasificacion_edad = db.Column(db.String(10), nullable=True)
