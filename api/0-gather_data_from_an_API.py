#!/usr/bin/python3
""" using this REST API, for a given employee ID, returns information
about his/her TODO list progress. """
import requests
import sys


def gatherDataFromEmployee():
    idInput = sys.argv[1]

    try:
        int(idInput)
    except Exception:
        print("Please insert an integer as a parameter")
        exit()

    employeeData = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(
            idInput)).json()[0]
    employeeToDoList = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            idInput)).json()

    # Iterating through the list of tasks and checking if the task is completed
    # If it is, it adds the
    # title of the task to the list of completed tasks and increments the numbe
    # of completed tasks.
    doneTasksTitles = [task["title"]
                       for task in employeeToDoList if task["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        employeeData["name"], len(doneTasksTitles), len(employeeToDoList)))
    for title in doneTasksTitles:
        print("\t " + title)


if __name__ == "__main__":
    gatherDataFromEmployee()