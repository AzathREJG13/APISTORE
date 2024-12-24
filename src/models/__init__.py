from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .categoria import Categoria
from .producto import Producto
from .electrodomestico import Electrodomestico
from .linea_blanca import LineaBlanca
from .telefonia import Telefonia
from .tv_video import TVVideo
from .videojuego import Videojuego
from .audio import Audio
from .alimento import Alimento

__all__ = [
    "db",
    "Categoria",
    "Producto",
    "Electrodomestico",
    "LineaBlanca",
    "Telefonia",
    "TVVideo",
    "Videojuego",
    "Audio",
    "Alimento",
]
