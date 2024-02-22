import os 
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRETE_KEY = 'Clave nueva'
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:root@127.0.0.1/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False