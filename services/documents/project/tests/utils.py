# services/documents/project/tests/utils.py


from project import db
from project.api.models import User
from project.api.models import Document
from project.api.models import Entity


def add_user(username, entity_id, lastname, email, password, status):
    user = User(username=username, entity_id=entity_id, lastname=lastname, email=email,password=password, status=status )
    db.session.add(user)
    db.session.commit()
    return user

def add_document(documentname, documentcode, documenttype, documentprice):
    document = Document(documentname=documentname, documentcode=documentcode, documenttype=documenttype, documentprice=documentprice)
    db.session.add(document)
    db.session.commit()
    return document

def add_entity(entityname, entityplace, entitycode):
    entity = Entity(entityname=entityname, entityplace=entityplace, entitycode=entitycode)
    db.session.add(entity)
    db.session.commit()
    return entity

