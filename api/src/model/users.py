from db import db, ma
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.schema import UniqueConstraint

class User(db.Model):
    __tablename__ = 'users'
    __table_args__=(UniqueConstraint('email', name='uq_email'),)
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    name = db.Column('name', db.String(225), nullable=False)
    created_at = db.Column('created_at', Timestamp, server_default=current_timestamp(), nullable=False)
    created_by = db.Column('created_by', db.String(225), nullable=True)
    updated_at = db.Column('updated_at', Timestamp, server_default=current_timestamp(), nullable=False)
    updated_by = db.Column('updated_by', db.String(225), nullable=True)
    email = db.Column('email', db.String(225), nullable=True)

    def __init__(self, id, name, created_at, created_by, updated_at, updated_by, email):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.email = email

    def __repr__(self):
         return '<User %r>' % self.name

    def get_user_list():
        # SELECT * FROM users
        user_list = db.session.query(User).all()
        if user_list == None:
            return []
        else:
            return user_list

    def create_user(user):
        record = User(
            name = user['name'],
        )
        # INSERT INTO users(name) VALUES(...)
        db.session.add(record)
        db.session.commit()
        return user

    def get_user_by_id(id):
        return db.session.query(User)\
            .filter(User.id == id)\
            .one()

# Difinition of User Schema with Marshmallow
# refer: https://flask-marshmallow.readthedocs.io/en/latest/
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
      model = User
    #   fields = ('id', 'name', 'created_at', 'created_by', 'updated_at', 'updated_by')