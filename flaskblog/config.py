import os

#run python run.py instead of running from pycharm
class Config:
    SECRET_KEY = '31c5abf54096e0d96d440567e38d4209'
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://brrojcdqutmoht:4231a5aaf978bf068247e6ae879ace4dc82443353746209fa55ed25ebc6ea047@ec2-34-202-5-87.compute-1.amazonaws.com:5432/d2bid53o4i3ftb'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USERNAME = '93ec69c7272171'
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'ff90d7da0930ad'
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')