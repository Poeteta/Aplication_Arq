from flask import Blueprint, jsonify, request, render_template, redirect
from sqlalchemy import exc
from project.api.models import User, Document, Entity, Documententity, db


documents_blueprint = Blueprint('documents', __name__, template_folder='./templates')

@documents_blueprint.route('/', methods=['GET'])
def get_all():
    """Obteniendo todos los productos"""
    response_object = {
        'status': 'success',
        'data': {
            'users': [user.to_json() for user in User.query.all()],
            'documents': [document.to_json() for document in Document.query.all()],
            'documententitys': [documententity.to_json() for documententity in Documententity.query.all()],
            'entitys': [entity.to_json() for entity in Entity.query.all()]
        }
    }
    return jsonify(response_object), 200

