from flask import request, jsonify
from flask_restful import Resource, reqparse, abort
import json
from ..models.user import User


class UserController(Resource):
    def get(self):
        all_users = User.query.all()
        all_users = map(lambda user: User.to_dict(user), all_users)
        # res = jsonify(all)
        return list(all_users)
