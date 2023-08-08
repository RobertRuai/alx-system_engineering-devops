#!/usr/bin/python3
"""prints ttitles o 1st 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    if res.status_code == '200':
        res_jsn = res.json()
        posts = res_jsn["data"]["children"]
        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    print(None)
