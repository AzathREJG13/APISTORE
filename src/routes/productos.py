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
    
    # Datos básicos del producto
    producto_result = {
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': float(producto.precio),
        'cantidad_disponible': producto.cantidad_disponible,
    }

    if producto.categoria.nombre == 'Electrodomésticos':
        producto_detalles = {
            'consumo_energia': producto.electrodomestico.consumo_energia,
            'garantia': producto.electrodomestico.garantia
        }
    elif producto.categoria.nombre == 'Telefonía':
        producto_detalles = {
            'marca': producto.telefonia.marca,
            'modelo': producto.telefonia.modelo,
            'almacenamiento': producto.telefonia.almacenamiento,
            'ram': producto.telefonia.ram
        }
    elif producto.categoria.nombre == 'Alimentos':
        producto_detalles = {
            'fecha_caducidad': producto.alimento.fecha_caducidad,
            'peso': producto.alimento.peso,
            'tipo_alimento': producto.alimento.tipo_alimento
        }

    categoria_result = {
        'id': producto.categoria.id,
        'nombre': producto.categoria.nombre
    }

    return jsonify({
        'producto': producto_result,
        'detalles_producto': producto_detalles,
        'categoria': categoria_result
    }), 200
