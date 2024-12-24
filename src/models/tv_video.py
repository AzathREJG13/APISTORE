from .import db

class TVVideo(db.Model):
    __tablename__ = 'tv_video'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    tipo_pantalla = db.Column(db.String(50), nullable=True)
    tamano_pulgadas = db.Column(db.Numeric(5, 2), nullable=True)
    resolucion = db.Column(db.String(50), nullable=True)
