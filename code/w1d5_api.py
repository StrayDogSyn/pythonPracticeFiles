import requests  # Import the requests library for making HTTP requests

# Make a GET request to the base URL of JSONPlaceholder API
response = requests.get("https://jsonplaceholder.typicode.com/")
# This sends a simple GET request to the root endpoint of the API

# Print the HTTP status code of the response (200 means OK)
print(f'This is the 1st: {response.status_code}')

# Define headers for the POST request - specifying we're sending JSON data
headers = {"Content-Type": "application/json"}

# Define the JSON body for our POST request
body = {"title": "foo", "body": "bar", "userId": 1}
# - title: Title of our post
# - body: Content of our post
# - userId: ID of the user creating the post

# Make a POST request to create a new post
# Note: There's a typo in 'repsponse' (should be 'response')
response = requests.post("https://jsonplaceholder.typicode.com/posts", headers=headers, json=body)
# - The endpoint '/posts' is used for creating new posts
# - We pass our headers to specify content type
# - The json parameter automatically converts the Python dictionary to JSON

# Print the status code of the POST response (201 means Created)
print(f'This is the 2nd: {response.status_code}')
