#!/usr/bin/python3
"""task0 module"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    """0. Gather data from an API"""

    user = requests.\
        get('https://jsonplaceholder.typicode.com/users/{}'.
            format(sys.argv[1]))
    user = user.json().get('username')
    todos = requests.\
        get('https://jsonplaceholder.typicode.com/todos?userId={}'.
            format(sys.argv[1]))
    todos = todos.json()
    with open(sys.argv[1] + '.csv', 'w') as file:
        for i in todos:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow([i['userId'], user, i['completed'], i['title']])
    file.close()
