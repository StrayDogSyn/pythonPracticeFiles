import json  # Import the json module to enable JSON processing capabilities

# Define a nested dictionary representing a student's information
# This demonstrates how Python dictionaries can be structured similarly to JSON objects
student_data = {
    'name': 'Alice Johnson',
    'age': 22,
    'courses': ['Python Programming', 'Data Structures', 'Algorithms'],  # Array/list of strings
    'grades': {  # Nested dictionary for course grades
        'Python Programming': 95,
        'Data Structures': 88,
        'Algorithms': 91
    },
    'contact': {  # Nested dictionary with multiple levels
        'email': 'alice@example.com',
        'phone': '555-123-4567',
        'address': {  # Deeper nested dictionary
            'street': '123 Campus Dr',
            'city': 'University Town',
            'state': 'CA',
            'zip': '94305'
        }
    }
}

# SERIALIZATION: Convert Python dictionary to JSON string format
# json.dumps() serializes a Python object to a JSON formatted string
# indent=4 adds 4 spaces of indentation for better readability
json_data = json.dumps(student_data, indent=4)
print("\nJSON representation of student data:")
print(json_data)  # Display the formatted JSON string

# DESERIALIZATION: Convert JSON string back to Python object
# json.loads() deserializes a JSON string back into a Python object (dict)
python_data = json.loads(json_data)
print("\nConverted back to Python:")
print(type(python_data))  # Confirms the type is a Python dictionary

# FILE OPERATIONS - Writing JSON to a file
# Open a file in write mode and use json.dump() to write Python object directly to a file
with open('student.json', 'w') as f:  # 'w' opens the file for writing, creating if it doesn't exist
    json.dump(student_data, f, indent=4)  # Write the data with proper indentation

print("\nWritten to student.json")

# FILE OPERATIONS - Reading JSON from a file
# Open the file in read mode and use json.load() to parse JSON directly from a file
with open('student.json', 'r') as f:  # 'r' opens the file for reading
    loaded_data = json.load(f)  # Parse the file contents into a Python object

print("Successfully loaded from file")

# REAL-WORLD EXAMPLE - Processing API Data
# This demonstrates a typical JSON structure you might receive from a weather API
weather_api_response = {
    "location": {
        "name": "New York",
        "region": "New York",
        "country": "United States",
        "lat": 40.71,
        "lon": -74.01,
        "timezone": "America/New_York"
    },
    "current": {
        "temp_f": 72.5,
        "condition": {
            "text": "Partly cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png"
        },
        "humidity": 65,
        "wind_mph": 10.5,
        "precip_in": 0.0
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2025-04-08",
                "day": {
                    "maxtemp_f": 75.6,
                    "mintemp_f": 62.1,
                    "condition": {
                        "text": "Sunny",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png"
                    }
                },
                "hour": [  # Array of hourly forecasts
                    {"time": "2025-04-08 00:00", "temp_f": 65.3},
                    {"time": "2025-04-08 01:00", "temp_f": 64.8},
                    {"time": "2025-04-08 02:00", "temp_f": 64.0}
                ]
            },
            {
                "date": "2025-04-09",
                "day": {
                    "maxtemp_f": 78.2,
                    "mintemp_f": 63.5,
                    "condition": {
                        "text": "Cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/119.png"
                    }
                },
                "hour": [
                    {"time": "2025-04-09 00:00", "temp_f": 66.2},
                    {"time": "2025-04-09 01:00", "temp_f": 65.7},
                    {"time": "2025-04-09 02:00", "temp_f": 65.1}
                ]
            }
        ]
    }
}

# DATA EXTRACTION - Accessing specific values from nested JSON/dictionary
# Using dictionary key notation to navigate through the nested structure
location_name = weather_api_response["location"]["name"]  # Access nested value with chained keys
current_temp = weather_api_response["current"]["temp_f"]
current_condition = weather_api_response["current"]["condition"]["text"]  # Access deeper nested value

# Format and display the extracted information
print(f"\nCurrent weather in {location_name}: {current_temp}°F, {current_condition}")

# DATA ITERATION - Processing lists of objects within the JSON structure
# Loop through the forecast data to extract information for each day
print("\nForecast:")
for day in weather_api_response["forecast"]["forecastday"]:  # Iterate through list of forecast days
    # Extract needed values from each day's data
    date = day["date"]
    max_temp = day["day"]["maxtemp_f"]
    min_temp = day["day"]["mintemp_f"]
    condition = day["day"]["condition"]["text"]
    
    # Format and display the forecast information
    print(f"{date}: {min_temp}°F to {max_temp}°F, {condition}")