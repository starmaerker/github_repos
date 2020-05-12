import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    USERNAME = os.environ.get('GIT_USERNAME')
    TOKEN = os.environ.get('GIT_TOKEN')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
