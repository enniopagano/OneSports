from distutils.command.config import config
from distutils.log import debug

class Config:
    SECRET_KEY = "12345678"
class developmentConfig(Config):
    debug = True    
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_DB = "flask"

config = {
    "development" : developmentConfig
}