from ..config.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        import json
        return json.loads(self.toJSON())


db.create_all()
# db.session.add(User(username="Flask", email="example@example.com"))
db.session.commit()
