# services/users/manage.py

from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)

def recreate_db():
    db.drop_all()
    db.create_all()
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