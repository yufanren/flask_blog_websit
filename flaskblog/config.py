import os

#run python app.py instead of running from pycharm
class Config:
    ENV = 'DEV'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    if ENV == 'DEV':
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    else:
        SECRET_KEY = ''
        SQLALCHEMY_DATABASE_URI = ''
        MAIL_USERNAME = ''
        MAIL_PASSWORD = ''
