#!/usr/bin/python3
# Gathers and prints some data from https://jsonplaceholder.typicode.com/
if __name__ == '__main__':
    import requests
    import sys

    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={'userId': sys.argv[1]}).json()

    completed = list(filter(lambda todo: todo.get("completed"), todos))

    user = requests.get("https://jsonplaceholder.typicode.com/users",
                        params={'id': sys.argv[1]}).json()[0]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(completed),
        len(todos)))

    for todo in completed:
        print('\t ', end='')
        print(todo.get("title"))
