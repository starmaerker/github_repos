import os


class Config(object):
    USERNAME = os.environ.get('GIT_USERNAME')
    TOKEN = os.environ.get('GIT_TOKEN')
