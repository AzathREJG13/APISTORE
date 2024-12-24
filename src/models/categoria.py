from . import db
import enum

class CategoriaEnum(enum.Enum):
    ELECTRODOMESTICOS = "Electrodomésticos"
    TELEFONIA = "Telefonía"
    ALIMENTOS = "Alimentos"
    AUDIO = "Audio"
    VIDEOJUEGOS = "Videojuegos"
    TV_VIDEO = "TV y Video"
    LINEA_BLANCA = "Línea Blanca"

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)  
    
    productos = db.relationship('Producto', backref='categoria', lazy=True)
