#!/usr/bin/python3
"""task0 module"""

import json
import requests
import sys

if __name__ == '__main__':
    """0. Gather data from an API"""

    user = requests.\
        get('https://jsonplaceholder.typicode.com/users/{}'.
            format(sys.argv[1]))
    user = user.json()
    todos = requests.\
        get('https://jsonplaceholder.typicode.com/todos?userId={}'.
            format(sys.argv[1]))
    todos = todos.json()
    _json_list = []
    for info in todos:
        dicty = {}  # create dicty to append in _json_list
        dicty['task'] = info['title']
        dicty['completed'] = info['completed']
        dicty['username'] = user['username']
        _json_list.append(dicty)
    dicty = {sys.argv[1]: _json_list}
    _file = str(sys.argv[1]) + '.json'
    with open(_file, 'w') as file:
        w = json.dump(dicty, file)
    file.close()