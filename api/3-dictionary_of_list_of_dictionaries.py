#!/usr/bin/python3
"""
Python script that, using the jsonplaceholder REST API, for a given employee
ID, export data in JSON format.

The script must accept an integer as a parameter, which is the employee ID.

Format: {
    "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username":
        "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
        "username": "USERNAME"}, ...
        ],
        "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username":
        "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
        "username": "USERNAME"}, ...
        ]
}
File name: todo_all_employees.json
"""
import json
import requests

if __name__ == '__main__':
    super_dict = {}

    # set and request to the restAPI:
    for user_id in range(1, 11):
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user_id)
        api_url = "https://jsonplaceholder.typicode.com/todos/"
        api_url += "?userId={}".format(user_id)

        user_response = requests.get(user_url).json().get("username")
        api_response = requests.get(api_url).json()

        # creates the list of dicts:
        my_list = []
        for element in api_response:
            new_dict = {}
            new_dict['task'] = element['title']
            new_dict['completed'] = element['completed']
            new_dict['username'] = user_response
            my_list.append(new_dict)

        # appends this lil dict to the super dict:
        super_dict[user_id] = my_list

    # export data in JSON format:
    with open('todo_all_employees.json', 'w') as json_file:
        json_file.write(json.dumps(super_dict))
    json_file.close()