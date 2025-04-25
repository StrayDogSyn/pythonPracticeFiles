import requests # type: ignore

def get_weather(city, country_code=""):
    api_key = "eaf68ffb413d707283399af330d02c3f"
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    location = f"{city},{country_code}" if country_code else city
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        weather_data = response.json()
        
        # Extract relevant information
        temperature = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        
        # Format and display the weather information
        print(f"\nWeather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
        
        return weather_data
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to the server. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except KeyError:
        print("Error parsing weather data. The API response format might have changed.")
    
    return None

# Test the function with London, UK
get_weather("London", "UK")

