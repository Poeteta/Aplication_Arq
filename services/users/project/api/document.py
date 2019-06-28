from flask import Blueprint, jsonify
from sqlalchemy import exc
from project.api.models import User, Document, Entity, Documententity, db

documents_blueprint = Blueprint('document', __name__)

@documents_blueprint.route('/', methods=['GET'])
def index():
    return "Hola"

@documents_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong!'
    })

@documents_blueprint.route('/entitys', methods=['GET'])
def get_all_entitys():
    response_object = {
        'status': 'success',
        'data': {
            'entitys': [entity.to_json() for entity in Entity.query.all()]
        }
    }
    return jsonify(response_object), 200

@documents_blueprint.route('/users', methods=['GET'])
def get_all_users():
    response_object = {
        'status': 'success',
        'data': {
            'users': [user.to_json() for user in User.query.all()]
        }
    }
    return jsonify(response_object), 200