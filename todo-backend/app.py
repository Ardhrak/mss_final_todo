from flask import Flask, request
from peewee import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = SqliteDatabase('todos.db')


class Todo(Model):
    todo_id = AutoField()
    message = CharField()
    is_Completed = BooleanField(default=False)

    class Meta:
        database = db


db.connect()


todos = [


]


@app.route("/health")
def hello_world():
    return {
        "status": "up"
    }


@app.route("/todos", methods=['POST', 'GET'])
def get_all_todos():
    if request.method == 'POST':
        message = request.json["todo"]

        Todo(message=message).save()

        return {
            "message": "Todo Added"
        }

    if request.method == 'GET':

        query = Todo.select()
        completed_todos=  []
        incomplete_todos = []

        for todo in query:
            if todo.is_Completed :
                todo_to_be_added = {
                    "id":todo.todo_id,
                    "message":todo.message

                }
                completed_todos.append(todo_to_be_added )
            else:
                todo_to_be_added = {
                    "id":todo.todo_id,
                    "message":todo.message

                }
                incomplete_todos.append(todo_to_be_added )     
        return {
          "incomplete_todos" : incomplete_todos,
          "completed_todos" : completed_todos
        }


@app.route("/todos/complete", methods=['POST'])
def todo_completed():
    id = request.json["id"]
    todo = Todo.get_by_id(id)
    todo.is_Completed = True
    todo.save()

    #  todos[i]["isCompleted"] = True
    return {

        "message": "Todo completed"
    }


@app.route("/todos/delete", methods=['POST'])
def todo_delete():
    id= request.json["id"]
    todo = Todo.get_by_id(id)
    todo.delete_instance()
    return {
            "message" : "Todo deleted"
        }
    