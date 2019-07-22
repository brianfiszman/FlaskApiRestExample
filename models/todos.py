from flask import request
from flask_restful import Resource, reqparse, abort

todos = {}


def abortIfTodoDoesntExist(todo_id):
    if todo_id not in todos:
        abort(404, message="TODO {} doesn't exists".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, todo_id):
        abortIfTodoDoesntExist(todo_id)
        return todos[todo_id]

    def delete(self, todo_id):
        abortIfTodoDoesntExist(todo_id)
        del todos[todo_id]
        return 'Resource Deleted', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        todos[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return todos

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(todos.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        todos[todo_id] = {'task': args['task']}
        return todos[todo_id], 201
