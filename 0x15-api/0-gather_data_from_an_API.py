#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/' + sys.argv[1]).json()
    todo_list = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    todos = [t.get("title") for t in todo_list if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(todos), len(todo_list)))
    [print("\t {}".format(c)) for c in todos]
