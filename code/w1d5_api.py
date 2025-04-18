import requests

response = requests.get("https://jsonplaceholder.typicode.com/")

print(response.status_code)

headers = {"Content-Type": "application/json"}
body = {"title": "foo", "body": "bar", "userId": 1}

