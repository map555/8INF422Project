import os

SECRET_KEY="y{^\6Q{>RC]8@MG .?R9Q>vq"

basedir=os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'app.db')
