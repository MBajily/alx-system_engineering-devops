#!/usr/bin/python3
"""Module for retrieving subscriber count from Reddit subreddits."""
from requests import get as request_get


def number_of_subscribers(subreddit):
    """Fetch and return the total number of subscribers for a given subred
    """
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    response = request_get(endpoint, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        subscriber_count = response.json()["data"]["subscribers"]
    except (KeyError, ValueError):
        subscriber_count = 0

    return subscriber_count
