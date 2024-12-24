from . import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    electrodomestico = db.relationship('Electrodomestico', uselist=False, backref='producto')
    linea_blanca = db.relationship('LineaBlanca', uselist=False, backref='producto')
    telefonia = db.relationship('Telefonia', uselist=False, backref='producto')
    tv_video = db.relationship('TVVideo', uselist=False, backref='producto')
    videojuego = db.relationship('Videojuego', uselist=False, backref='producto')
    audio = db.relationship('Audio', uselist=False, backref='producto')
    alimento = db.relationship('Alimento', uselist=False, backref='producto')
