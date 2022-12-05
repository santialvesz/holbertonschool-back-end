#!/usr/bin/python3
"""
Python script that, using the jsonplaceholder REST API, for a given employee
ID, export data in the CSV format.

The script must accept an integer as a parameter, which is the employee ID.

Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name: USER_ID.csv
"""
import csv
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

    # export data in CSV format:
    with open("{}.csv".format(emp_id), 'w') as csv_file:
        # quoting parameter: allows us obtain each column of our csv file
        # inside of "":
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in api_response:
            result = [emp_id, user_response,
                      task["completed"], task["title"]]
            writer.writerow(result)
    csv_file.close()