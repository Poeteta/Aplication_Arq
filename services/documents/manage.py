#services/users/manage.py

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
from project.api.models import Document
from project.api.models import Documententity
from project.api.models import Entity
import unittest


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    
    db.session.add(User(username='Comando', entity=1, lastname='Capac', email='capac@gmail.com', password='enlamansiondelosheroes', activate=0))
    db.session.add(User(username='Daniel', entity=2, lastname='Pacheco', email='danielpacheco@gmail.com', password='dasdasdasd', activate=1))
    db.session.add(Document(documentname='Certificado de Estudios post grado', documentcode='C001', documenttype='Certificado', documentprice=19))
    db.session.add(Document(documentname='Certificado de Estudios Pre graddo', documentcode='C001', documenttype='Certificado', documentprice=19))
    db.session.add(Document(documentname='Record academico post grado', documentcode='C001', documenttype='Record Academico', documentprice=19))
    db.session.add(Documententity(document_id=1, entity_id=1))
    db.session.add(Documententity(document_id=2, entity_id=1))
    db.session.add(Documententity(document_id=1, entity_id=2))
    db.session.add(Entity(entityname='Escuela de Ingenieria de Sistemas', entityplace='FIA', entitycode='E001'))
    db.session.add(Entity(entityname='Escuela de Ingenieria Civil', entityplace='FIA', entitycode='E002'))
    db.session.commit()

@cli.command()
def test():
   """ Ejecutar las pruebas sin covertura de codigo"""
   tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
   result = unittest.TextTestRunner(verbosity=2).run(tests)
   if result.wasSuccessful():
       return 0
   return 1

if __name__ == '__main__':
    cli()