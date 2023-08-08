#!/usr/bin/python3
""" prints ttitles o 1st 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "YOUR_USER_AGENT"
    }

    res = requests.get(url, headers=headers)
    if res.status_code == '200':
        res_jsn = res.json()
        posts = res_jsn["data"]["children"]
        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
