from sqlalchemy.sql import func
from project import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    lastname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    entity = db.relationship("Entity")

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'entity_id': self.entity_id,
            'lastname': self.lastname,
            'email': self.email,
            'password': self.password,
            'status': self.status
        }

class Document(db.Model):
    __tablename__= 'document'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    documentname = db.Column(db.String(128), nullable=False)
    documentcode = db.Column(db.String(128), nullable=False)
    documenttype = db.Column(db.String(128), nullable=False)
    documentprice = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'documentname': self.documentname,
            'documentcode': self.documentcode,
            'documenttype': self.documenttype,
            'documentprice': self.documentprice
        }

class Documententity(db.Model):
    __tablename__= 'documententity'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    document = db.relationship('Document')
    entity = db.relationship('Entity')

    def to_json(self):
        return {
            'id': self.id,
            'document_id': self.document_id,
            'entity_id': self.entity_id
        }

class Entity(db.Model):
    __tablename__= 'entity'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entityname = db.Column(db.String(256), nullable=False)
    entityplace = db.Column(db.String(128), nullable=False)
    entitycode = db.Column(db.String(128), nullable=False)

    def to_json(self):
        return { 
            'id': self.id,
            'entityname': self.entityname,
            'entityplace': self.entityplace,
            'entitycode': self.entitycode
        }