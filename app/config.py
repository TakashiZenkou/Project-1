import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://jyhdzbpjvoolwm:1d393263eaa8dd808f93288e87178fe2fe746326ee1572b33f31c550d4409aea@ec2-3-222-204-187.compute-1.amazonaws.com:5432/d43rokaj76pnvf').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
