#!/usr/bin/python3
"""Module for counting occurrences of keywords in Reddit hot article titles."""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively query Reddit API, parse hot article titles, and count keywords.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): List of keywords to count.
        after (str): The 'after' parameter for pagination (default: None).
        count_dict (dict): Dictionary to store keyword counts (default: None).

    Returns:
        None: Prints the sorted results.
    """
    if count_dict is None:
        count_dict = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        title = post["data"]["title"].lower()
        for word in count_dict:
            count_dict[word] += sum(1 for w in title.split() if w == word)

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming\
                'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
