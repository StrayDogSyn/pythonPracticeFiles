import requests

def get_weather(city):
    """
    Retrieves and displays current weather information for a specified city.
    
    Args:
        city (str): Name of the city to get weather for
    
    Returns:
        dict: Weather data if successful, None otherwise
    """
    # API key for OpenWeatherMap (required for authentication)
    api_key = "eaf68ffb413d707283399af330d02c3f"
    
    # Base URL for the OpenWeatherMap API
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request:
    # - q: location query (city name)
    # - appid: API key for authentication
    # - units: metric for Celsius temperature
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        # Send GET request to the weather API
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Convert the response to JSON format
        weather_data = response.json()
        
        # Extract weather information from the response
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        # Display basic weather information
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Conditions: {description}")
        
        return weather_data
        
    except Exception as err:
        # Simple error handling for all potential issues
        print(f"An error occurred: {err}")
        return None

# Example: Get weather for London
get_weather("London")
