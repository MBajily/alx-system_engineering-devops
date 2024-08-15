#!/usr/bin/python3
"""Module for retrieving subscriber count from Reddit subreddits."""
import requests


def number_of_subscribers(subreddit):
    """Fetch and return the total number of subscribers for a given subred
    """
    endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(endpoint, headers=header, allow_redirects=False)

    if response.status_code == 404:
        return 0

    subscriber_count = response.json().get("data")
    return subscriber_count.get("subscribers")
