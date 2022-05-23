from constants import SECRET

class Config(object):
    DEBUG = True
    SECRET = SECRET
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'					# было
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask_app_user:1234@localhost/flask_db'	# стало
    SQLALCHEMY_TRACK_MODIFICATIONS = False




