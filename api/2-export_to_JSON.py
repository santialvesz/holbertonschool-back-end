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
        ]
}
File name: USER_ID.json
"""
import json
import requests
import sys

if __name__ == '__main__':

    # check if the sys.argv[1] is or not an int:
    try:
        emp_id = int(sys.argv[1])
    except Exception:
        print("Please insert an integer as a parameter")
        exit()

    # set and request to the restAPI:
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    api_url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        emp_id)

    user_response = requests.get(user_url).json().get('username')
    api_response = requests.get(api_url).json()

    # creates the list of dicts:
    my_list = []
    for element in api_response:
        new_dict = {}
        new_dict['task'] = element['title']
        new_dict['completed'] = element['completed']
        new_dict['username'] = user_response
        my_list.append(new_dict)

    # creates the user_id dict:
    final_dict = {}
    final_dict[emp_id] = my_list

    # export data in JSON format:
    with open("{}.json".format(emp_id), 'w') as json_file:
        json_file.write(json.dumps(final_dict))
    json_file.close()
