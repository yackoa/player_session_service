import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(Object):
    """
    TODO: add documentation for Config
    TODO: add more config - DEV / TEST / PROD
    """
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or \
                               'sqlite:///' + os.path.join(basedir, 'app.db')
    #saves memory if
    SQLALCHEMY_TRACK_MODIFICATIONS = False



