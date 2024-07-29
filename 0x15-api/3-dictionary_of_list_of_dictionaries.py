#!/usr/bin/python3
"""Using what you did in the task #0, extend
Python script to export data in the JSON formatodo
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in requests.get(url + "todos",
                                    params={"userId": user.get("id")}).json()]
            for user in users}, file)