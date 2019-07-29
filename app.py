from flask import Flask
from .config.database import db
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

conn = "mysql://root:123123@localhost/todos"


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = conn
    return app


app = create_app()

with app.app_context():
    db.init_app(app)
    from .controllers.user import UserController
    api = Api(app)
    api.add_resource(UserController, '/user')
