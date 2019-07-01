#services/users/manage.py

import unittest

import coverage # new
from flask.cli import FlaskGroup

from project import create_app, db # new
from project.api.models import User, Document, Documententity, Entity # new


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app() # new
cli = FlaskGroup(create_app=create_app) # new

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Ejecutar los tests sin covertura de codigo"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command('seed_db')
def seed_db():
    
    db.session.add(Document(documentname='Certificado de Estudios post grado', documentcode='C001', documenttype='Certificado', documentprice=19))
    db.session.add(Document(documentname='Certificado de Estudios Pre graddo', documentcode='C001', documenttype='Certificado', documentprice=19))
    db.session.commit()
    

@cli.command('seed_dbe')
def seed_db():
    
    db.session.add(Entity(entityname = 'Escuela de Ingenieria de Sistemas' , entityplace = 'FIA', entitycode = 'E001' ))
    db.session.add(Entity(entityname = 'Escuela de Ingenieria Civil' , entityplace = 'FIA' , entitycode = 'E002' ))
    db.session.commit()
   
@cli.command('seed_dbu')
def seed_db():
    
    db.session.add(User(username='Comando', entity_id=1, lastname='Capac', email='capac@gmail.com', password='enlamansiondelosheroes', status = 0))
    db.session.add(User(username='Daniel', entity_id=2, lastname='Pacheco', email='danielpacheco@gmail.com', password='dasdasdasd', status = 1))
    db.session.commit()
    

@cli.command('seed_dbd')
def seed_db():
    
    db.session.add(Documententity(document_id=1, entity_id=1))
    db.session.add(Documententity(document_id=2, entity_id=1))
    db.session.add(Documententity(document_id=1, entity_id=2))
    db.session.commit()


# nuevo -> de covertura
@cli.command()
def cov():
    """Ejecuta las pruebas unitarias con coverage"""
    tests   = unittest.TestLoader().discover('project/tests')
    result  = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Resumen de cobertura')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()