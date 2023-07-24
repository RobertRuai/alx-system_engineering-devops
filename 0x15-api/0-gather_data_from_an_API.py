#!/usr/bin/python3
"""Use JSONPlaceholder API to get information about employee"""
import requests
import sys


if __name__ == '__main__':
    userid = int(sys.argv[1])
    u_url = ("https://jsonplaceholder.typicode.com/users/{}".format(
        userid))
    res = requests.get(u_url)
    r = res.json()
    name = r.get('name')

    todo_url = ("https://jsonplaceholder.typicode.com/todos?userId={}".format(
        userid))
    to_res = requests.get(todo_url).json()
    t_tasks = 0
    done_tasks = 0
    done_lst = []

    for task in to_res:
        t_tasks += 1
        if task.get('completed') is True:
            done_lst.append(task.get('title'))
            done_tasks += 1
    print("Employyee {} is done with tasks({}/{}):".format(
        name, done_tasks, t_tasks))
    for title in done_lst:
        print("\t {}".format(title))
