from ..config.database import db
from marshmallow_sqlalchemy import ModelSchema


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def getAll():
        users = User.query.all()
        return users_schema.dump(users)


class UserSchema(ModelSchema):
    class Meta:
        model = User


db.create_all()
user_schema = UserSchema()
users_schema = UserSchema(many=True)
# db.session.add(User(username="Flask", email="example@example.com"))
db.session.commit()
