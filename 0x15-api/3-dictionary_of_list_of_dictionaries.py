#!/usr/bin/python3
"""exports data of all employees in JSON format"""
import json
import requests
import sys


if __name__ == '__main__':
    u_url = ("https://jsonplaceholder.typicode.com/users")
    res = requests.get(u_url)
    r = res.json()

    todo_url = ("https://jsonplaceholder.typicode.com/todos")
    to_res = requests.get(todo_url).json()

    jd = {}
    for user in r:
        tasks = []
        userid = (user.get('id'))
        for task in to_res:
            if user.get('id') == task.get('userId'):
                td = {}
                td["username"] = user.get('username')
                td["task"] = task.get('title')
                td["completed"] = task.get('completed')
            tasks.append(td)
        jd[userid] = tasks

    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump(jd, f)
