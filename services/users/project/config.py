# services/users/project/config.py


import os #nuevo



class BaseConfig:
   """Configuracion base"""
   TESTING = False
   SQLALCHEMY_TRACK_MODIFICATIONS = False #Nuevo


class DevelopmentConfig(BaseConfig):
   """Configuraccion de desarrollo"""
   SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') #Nuevo 


class TestingConfig(BaseConfig):
   """Configuración de prueba"""
   TESTING = True
   SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_TEST_URL') #Nuevo 


class ProductionConfig(BaseConfig):
   """Configuracion de produccion"""
   SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') #Nuevo 