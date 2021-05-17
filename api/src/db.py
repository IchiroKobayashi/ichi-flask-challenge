from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()

def init_db(app):
  db.init_app(app)
  Migrate(app, db)

def init_ma(app):
  ma.init_app(app)