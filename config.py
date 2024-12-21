class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'miContrasena@123'
    MYSQL_DB = 'APISTORE'


config = {
    'development': DevelopmentConfig
}