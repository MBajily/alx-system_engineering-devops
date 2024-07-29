import sys
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    response = requests.get(url)
    users = response.json()

    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url, params={"userId": sys.argv[1]})
    todos = response.json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]