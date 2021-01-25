import os

class Configurations(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'regressionz'