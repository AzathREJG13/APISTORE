from flask import Flask
from src.models  import db
#from routes.categorias_routes import categorias_bp
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # Carga la configuración desde config.py

    # Inicializar extensiones
    db.init_app(app)

    # Registrar blueprints
    #app.register_blueprint(categorias_bp)

    return app


if __name__ == '__main__':
    app = create_app('development')  # Usa el entorno 'development'
    with app.app_context():
        db.create_all()  # Crea las tablas
    app.run()
