#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_endpoint = '{}users/{}'.format(url, sys.argv[1])
    user_response = requests.get(user_endpoint)
    user = user_response.json()

    print("Employee {} is done with tasks".format(user.get('name')), end="")

    todos_endpoint = '{}todos?userId={}'.format(url, sys.argv[1])
    todos_response = requests.get(todos_endpoint)
    tasks = todos_response.json()

    completed_tasks = [task for task in tasks if task.get('completed') is True]

    print("({}/{}):".format(len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
