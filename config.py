import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'e4bada5e477ce2ce2fa77110e0fca1d8db0793d9'
    SQLALCHEMY_DATABASE_URI = 'postgres://jjdawlhzyjvbbp:a358b2194dc64333c062cc06a05fa1d1a479c831f148b80ef6aa3c6216177b04@ec2-34-195-169-25.compute-1.amazonaws.com:5432/d85fqdve0ckfdk'
    SQLALCHEMY_TRACK_MODIFICATIONS = False