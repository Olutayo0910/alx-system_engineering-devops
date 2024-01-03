#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    endpoint = '{}/users/{}'.format(url, user_id)
    req_endpoint = requests.get(endpoint)
    user_data = req_endpoint.json()
    name = user_data.get('username')

    todos_endpoint = '{}todos?userId={}'.format(url, user_id)
    todos_response = requests.get(todos_endpoint)
    tasks = todos_response.json()
    task_profile = []
    for task in tasks:
        task_profile.append([user_id,
                            name,
                            task.get('completed'),
                            task.get('title')])

    filename = "{}.csv".format(user_id)
    with open(filename, "w") as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in task_profile:
            employee_writer.writerow(task_profile)
