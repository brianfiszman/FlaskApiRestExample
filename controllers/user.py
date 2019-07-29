from flask import request, jsonify
from flask_restful import Resource, reqparse, abort
import json
from ..models.user import User


class UserController(Resource):
    def get(self):
        all_users = User.query.all()
        list(map(lambda user: json.loads(user.toJSON()), all_users))
        return list(all_users)
