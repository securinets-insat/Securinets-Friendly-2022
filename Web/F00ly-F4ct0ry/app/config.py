import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
FLAG = os.environ.get('FLAG')
PORT = os.environ.get('PORT')
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
