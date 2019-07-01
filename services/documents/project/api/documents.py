from flask import Blueprint, jsonify
from sqlalchemy import exc
from project.api.models import User, Document, Entity, Documententity, db

documents_blueprint = Blueprint('documents', __name__)

@documents_blueprint.route('/', methods=['GET'])
def index():
    return "Hola"

@documents_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong!'
    })

@documents_blueprint.route('/documents', methods=['GET'])
def get_all_users():
    response_object = {
        'status': 'success',
        'data': {
            'documents': [document.to_json() for document in Document.query.all()]
        }
    }
    return jsonify(response_object), 200

@documents_blueprint.route('/documets', methods=['GET'])
def get_all_users():
    response_object = {
        'status': 'success',
        'data': {
            'documents': [document.to_json() for document in Document.query.all()]
        }
    }
    return jsonify(response_object), 200