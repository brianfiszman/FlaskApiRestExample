from flask import request, jsonify
from flask_restful import Resource, reqparse, abort
import json
from ..models.user import User


parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')


class UserController(Resource):
    def get(self):
        users = User.getAll()
        return users

    def post(self):
        args = parser.parse_args()
        User.createUser(args)
        return 200
