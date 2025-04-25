#!/usr/bin/env python3
"""
Week 1 Day 5: API Interaction with Python

This script demonstrates how to interact with RESTful APIs using Python's requests library.
It shows how to perform GET and POST requests to the JSONPlaceholder API, a free fake online
REST API for testing and prototyping.

Topics covered:
1. Making GET requests to retrieve data
2. Making POST requests to create data
3. Working with HTTP headers and status codes
4. Handling JSON data in requests and responses

API Documentation: https://jsonplaceholder.typicode.com/
"""

print("=" * 60)
print("PYTHON API INTERACTION DEMONSTRATION")
print("=" * 60)
print("\nUsing JSONPlaceholder API: https://jsonplaceholder.typicode.com/")

# Import the requests library for making HTTP requests
import requests
import json
import time

# SECTION 1: Basic GET request
print("\n1. MAKING A BASIC GET REQUEST")
print("-" * 60)
print("Sending GET request to the base URL of JSONPlaceholder API...")

try:
    # Make a GET request to the base URL of JSONPlaceholder API
    start_time = time.time()
    response = requests.get("https://jsonplaceholder.typicode.com/")
    request_time = time.time() - start_time
    
    # Print information about the response
    print(f"Request completed in {request_time:.2f} seconds")
    print(f"Status code: {response.status_code} ({200: 'OK', 404: 'Not Found', 500: 'Server Error'}.get(response.status_code, 'Unknown'))")
    print(f"Response headers: {json.dumps(dict(response.headers), indent=2)}")
    
    # Print the content if successful
    if response.status_code == 200:
        print("Response body:")
        print(response.text)
    
except requests.exceptions.RequestException as e:
    print(f"Error during GET request: {e}")

# SECTION 2: POST request to create a resource
print("\n2. MAKING A POST REQUEST TO CREATE A RESOURCE")
print("-" * 60)

# Define headers for the POST request - specifying we're sending JSON data
headers = {"Content-Type": "application/json"}
print(f"Request headers: {json.dumps(headers, indent=2)}")

# Define the JSON body for our POST request
body = {"title": "Example Post", "body": "This is a post created via the Python requests library", "userId": 1}
print(f"Request body: {json.dumps(body, indent=2)}")

try:
    print("\nSending POST request to create a new post...")
    
    # Make a POST request to create a new post
    start_time = time.time()
    response = requests.post("https://jsonplaceholder.typicode.com/posts", headers=headers, json=body)
    request_time = time.time() - start_time
    
    print(f"Request completed in {request_time:.2f} seconds")
    print(f"Status code: {response.status_code} ({201: 'Created', 400: 'Bad Request', 401: 'Unauthorized', 500: 'Server Error'}.get(response.status_code, 'Unknown'))")
    
    # If successful, parse and display the response
    if response.status_code == 201:  # 201 = Created
        created_resource = response.json()
        print("\nSuccessfully created a new resource!")
        print(f"Response body: {json.dumps(created_resource, indent=2)}")
        print(f"\nNOTE: The server assigned ID {created_resource.get('id', 'unknown')} to our new post.")
        print("In a real API (not a mock like JSONPlaceholder), this would actually create a resource in the database.")
    else:
        print(f"Failed to create resource. Response: {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"Error during POST request: {e}")

# SECTION 3: Fetching specific data with GET
print("\n3. FETCHING SPECIFIC DATA WITH PARAMETERS")
print("-" * 60)

try:
    print("Fetching posts for a specific user (userId=1)...")
    
    # Make a GET request with query parameters
    params = {"userId": 1}
    start_time = time.time()
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
    request_time = time.time() - start_time
    
    print(f"Request completed in {request_time:.2f} seconds")
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        print(f"\nFound {len(posts)} posts for user 1")
        print(f"First post title: {posts[0]['title'] if posts else 'No posts found'}")
        print(f"URL with parameters: {response.url}")
        
except requests.exceptions.RequestException as e:
    print(f"Error during filtered GET request: {e}")

# Summary
print("\n" + "=" * 60)
print("API INTERACTION DEMONSTRATION COMPLETE")
print("=" * 60)
print("\nWhat we learned:")
print("1. How to make GET requests to retrieve data from an API")
print("2. How to make POST requests to create new resources")
print("3. How to set headers and pass JSON data in requests")
print("4. How to handle and parse API responses")
print("5. How to use query parameters to filter API results")
print("\nCommon HTTP Status Codes:")
print("  200: OK - Request succeeded")
print("  201: Created - Resource successfully created")
print("  400: Bad Request - Server couldn't understand the request")
print("  401: Unauthorized - Authentication required")
print("  404: Not Found - Resource doesn't exist")
print("  500: Server Error - Something went wrong on the server side")
