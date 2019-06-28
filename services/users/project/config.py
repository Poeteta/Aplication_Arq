# services/users/project/config.py


import os  # nuevo


class BaseConfig:
    """Base Configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_secretkey"


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """Test Config"""
    TESTING = True
    SQLALCHEMY_DATABSE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """Production Development"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')