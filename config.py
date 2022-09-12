from distutils.debug import DEBUG


class configuracion():
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "curso"
config = {
    "development":configuracion
}