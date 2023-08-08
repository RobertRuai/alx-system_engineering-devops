#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    if res.status_code == '200':
        res_jsn = res.json()
        subscribers = res_jsn["data"]["subscribers"]
        return subscribers
    else:
        return 0
