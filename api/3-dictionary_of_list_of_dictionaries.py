#!/usr/bin/python3
"""task0 module"""

import json
import requests
import sys

if __name__ == '__main__':
    """0. Gather data from an API"""

    user = requests.get('https://jsonplaceholder.typicode.com/users/')
    user = user.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = todos.json()
    dicty = {}
    _list = []
    for i in user:
        _list = [{"task": j.get('title'),
                 "completed": j.get('completed'),
                  "username": i.get('username')} for j in todos
                 if j.get('userId') == i.get('id')]
        dicty["{}".format(i.get('id'))] = _list
    with open("todo_all_employees.json", 'w', encoding="UTF-8") as file:
        w = json.dump(dicty, file)
