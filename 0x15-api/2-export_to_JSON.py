#!/usr/bin/python3
"""Using what you did in the task #0, extend
Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    userID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}" + str(userID)).json()
    todo = requests.get(url + "todos", params={"userId": userID}).json()

    username = user.get("username")
    with open("{}.json".format(userID), "w") as json_file:
        json.dump({userID: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo]}, json_file)
