from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config
app = Flask(__name__)
conexion = MySQL(app)

@app.route('/productos', methods=['GET'])
def listar_productos_por_categoria():
    try:
        cursor = conexion.connection.cursor()
        # Consulta que une productos con categorías
        sql = '''
            SELECT p.id, p.nombre, p.descripcion, p.precio, p.cantidad_disponible, c.nombre AS categoria
            FROM productos p
            JOIN categorias c ON p.categoria_id = c.id
        '''
        cursor.execute(sql)
        datos = cursor.fetchall()

        productos_por_categoria = {}
        for fila in datos:
            categoria = fila[5]
            producto = {
                'id': fila[0],
                'nombre': fila[1],
                'descripcion': fila[2],
                'precio': fila[3],
                'cantidad_disponible': fila[4]
            }
            if categoria not in productos_por_categoria:
                productos_por_categoria[categoria] = []
            productos_por_categoria[categoria].append(producto)

        return jsonify({'productos': productos_por_categoria, 'mensaje': 'Productos listados por categoría'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'detalle': str(ex)})

@app.route('/productos/<id>', methods=['GET'])
def listar_un_producto_separado(id):
    try:
        cursor = conexion.connection.cursor()
        # Obtener información del producto
        sql_producto = "SELECT * FROM productos WHERE id = %s"
        cursor.execute(sql_producto, (id,))
        datos = cursor.fetchone()
        if datos is not None:
            producto = {
                'id': datos[0],
                'nombre': datos[1],
                'descripcion': datos[2],
                'precio': datos[3],
                'cantidad_disponible': datos[4],
                'categoria_id': datos[5]
            }

            # Determinar la tabla de detalles según la categoría
            categoria_id = datos[5]
            tablas_categoria = {
                1: 'electrodomesticos',
                2: 'linea_blanca',
                3: 'telefonia',
                4: 'tv_video',
                5: 'videojuegos',
                6: 'audio',
                7: 'alimentos'
            }
            tabla_detalle = tablas_categoria.get(categoria_id)

            detalles = {}
            if tabla_detalle:
                sql_detalle = f"SELECT * FROM {tabla_detalle} WHERE producto_id = %s"
                cursor.execute(sql_detalle, (id,))
                detalles_row = cursor.fetchone()
                if detalles_row:
                    columnas = [desc[0] for desc in cursor.description]  # Obtener nombres de columnas
                    detalles = dict(zip(columnas, detalles_row))

            return jsonify({'producto': producto, 'detalles': detalles, 'mensaje': 'Producto encontrado'})
        else:
            return jsonify({'mensaje': 'Producto no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'detalle': str(ex)})


def pagina_no_encontrada(error):
    return "<h1>La pagina no existe....</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
