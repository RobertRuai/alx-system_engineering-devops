#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()
        subscribers = response_json["data"]["subscribers"]
        return subscribers
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
