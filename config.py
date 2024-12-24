class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rafael1302:123456@localhost:5432/APISTORE'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
}
