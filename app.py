from flask import Flask
from flask_restful import Api
from models.todos import Todo, TodoList
from models.helloworld import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')
