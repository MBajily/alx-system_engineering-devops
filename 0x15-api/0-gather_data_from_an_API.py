#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/' + sys.argv[1]).json()
<<<<<<< HEAD
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    todos = [t.get("title") for t in todo if t.get("completed") is True]
=======
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
>>>>>>> bc02b92d315ee7a322b5cb545e3be16399407b24
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(todos), len(todo)))
    [print("\t {}".format(c)) for c in todos]
