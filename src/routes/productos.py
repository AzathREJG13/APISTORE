from flask import jsonify, request, Blueprint
from src.models.producto import Producto  # Importa Producto correctamente
from src.models.categoria import Categoria  # Importa Categoria correctamente

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/productos', methods=['GET'])
def get_productos():
    # Obtén todos los productos de la base de datos
    productos = Producto.query.all()
    
    result = [
        {
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio),  
            'cantidad_disponible': producto.cantidad_disponible,
            'categoria': producto.categoria.nombre 
        }
        for producto in productos
    ]
    
    return jsonify(result), 200

@product_routes.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify({
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': float(producto.precio),
        'cantidad_disponible': producto.cantidad_disponible,
        'categoria': producto.categoria.nombre
    }), 200


