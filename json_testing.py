import json
# JSON data as a multi-line string
json_data = '''
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.85,
    "feels_like": 281.94,
    "temp_min": 281.51,
    "temp_max": 284.01,
    "pressure": 1019,
    "humidity": 85,
    "sea_level": 1019,
    "grnd_level": 1015
  },
  "visibility": 10000,
  "wind": {
    "speed": 2.06,
    "deg": 0
  },
  "clouds": {
    "all": 13
  },
  "dt": 1745455725,
  "sys": {
    "type": 1,
    "id": 1414,
    "country": "GB",
    "sunrise": 1745469938,
    "sunset": 1745521877
  },
  "timezone": 3600,
  "id": 2643743,
  "name": "London",
  "cod": 200
}
'''
weather_data = json.loads(json_data)
# print(weather_data)
# print(weather_data['main']['temp'])
# print(weather_data['weather'][0]['description'])
# print(weather_data['main']['temp'] - 273.15)  # Convert from Kelvin to Celsius
# print(weather_data['main']['temp'] * 9/5 - 459.67)  # Convert from Kelvin to Fahrenheit
# print(weather_data['weather'][0]['description'])

# # Print timezone (it's a single value, not an object)
# print(f"Timezone offset in seconds: {weather_data['timezone']}")

# # Print other relevant data
# print(f"\nCity name: {weather_data['name']}")
# print(f"Country: {weather_data['sys']['country']}")
# print(f"Timezone: {weathimezone']} seconds")
# print(f"Coordinates: {weather_data['coord']['lat']}, {weather_data['coord']['lon']}")
# print(f"Weather ID: {weather_data['weather'][0]['id']}")
print(f"Timezone: {weather_data['timezone']} seconds, ID: {weather_data['id']}, Name: {weather_data['name']}")
print(f" {weather_data['sys']}")
