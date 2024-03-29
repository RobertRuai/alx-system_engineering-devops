#!/usr/bin/python3
"""
prints ttitles o 1st 10 hot posts listed
for given subreddit recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "limit": 100,
        "after": after
    }

    res = requests.get(url, headers=headers, params=params)
    if res.status_code == '200':
        res_jsn = res.json()
        posts = res_jsn["data"]["children"]
        if not posts:
            return hot_list
        for post in posts:
            title = post["data"]["title"]
            host_list.append(title)
        l_post = posts[-1]["data"]["name"]
        return recurse(subreddit, hot_list=hot_list, after=after)
    else:
        return None
