# service//users/project/__init__.py


import os #nuevo
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy  #Nuevo


db = SQLAlchemy()

def create_app(script_info=None):
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)
    from project.api.document import documents_blueprint
    app.register_blueprint(documents_blueprint)
    @app.shell_context_processor
    def ctx():
        return {'app':app, 'db':db}

    return app