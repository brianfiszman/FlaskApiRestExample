from flask import request, jsonify
from flask_restful import Resource, reqparse, abort
import json
from ..models.user import User


class UserController(Resource):
    def get(self):
        users = User.getAll()
        return users
