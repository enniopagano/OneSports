from distutils.command.config import config
from distutils.log import debug


class developmentConfig():
    debug = True

config = {
    "development" : developmentConfig
}