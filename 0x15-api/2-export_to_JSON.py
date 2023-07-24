#!/usr/bin/python3
"""exports data in JSON format"""
import json
import requests
import sys


if __name__ == '__main__':
    userid = sys.argv[1]
    u_url = ("https://jsonplaceholder.typicode.com/users/{}".format(
        userid))
    res = requests.get(u_url)
    r = res.json()
    uname = r.get('username')

    todo_url = ("https://jsonplaceholder.typicode.com/todos?userId={}".format(
        userid))
    to_res = requests.get(todo_url).json()

    tasks = []
    for task in to_res:
        td = {}
        td["task"] = task.get('title')
        td["completed"] = task.get('completed')
        td["username"] = uname
        tasks.append(td)
    jd = {}
    jd[userid] = tasks

    with open('{}.json'.format(userid), 'w', encoding='UTF8') as f:
        json.dump(jd, f)
