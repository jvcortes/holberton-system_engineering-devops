#!/usr/bin/python3
# Gathers and prints some data from https://jsonplaceholder.typicode.com/ in
# JSON.
if __name__ == '__main__':
    import json
    import requests
    import sys

    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={'userId': sys.argv[1]}).json()

    user = requests.get("https://jsonplaceholder.typicode.com/users",
                        params={'id': sys.argv[1]}).json()[0]

    for todo in todos:
        completed = todo["completed"]
        del todo["completed"]
        todo["task"] = todo.get("title")
        todo["completed"] = completed
        todo["username"] = user.get("username")
        del todo["userId"]
        del todo["id"]
        del todo["title"]

    todo_list = {sys.argv[1]: todos}

    with open("{}.json".format(sys.argv[1]), 'w', newline='') as f:
        f.write(json.dumps(todo_list))
