#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Make GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If subreddit is invalid or any other error occurs, return 0
            return 0
    except Exception:
        # If any exception occurs (e.g., network error), return 0
        return 0
