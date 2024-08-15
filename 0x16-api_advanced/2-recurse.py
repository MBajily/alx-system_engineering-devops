#!/usr/bin/python3
"""Module for recursively querying the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to store the titles (default is empty list).
        after (str): id of the last post from the previous page (default None).

    Returns:
        list: A list of all hot article titles.
        None: If the subreddit is invalid or no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    after = data.get("after")
    children = data.get("children", [])

    for child in children:
        hot_list.append(child["data"]["title"])

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list if hot_list else None
