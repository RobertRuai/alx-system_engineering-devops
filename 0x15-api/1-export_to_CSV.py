#!/usr/bin/python3
"""Use JSONPlaceholder API to get information about employee"""
import csv
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

    with open('{}.csv'.format(userid), 'w', encoding='UTF8',  newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in to_res:
            task_status = task.get('completed')
            title = task.get('title')
            writer.writerow([userid, uname, task_status, title])
