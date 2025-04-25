import requests

api_key = "eaf68ffb413d707283399af330d02c3f"
url = "https://api.openweathermap.org/data/2.5/weather"

whatever = {
    "q": "London,uk",
    "appid": api_key,
    "units": "metric"
}
response = requests.get(url, params=whatever)

print(response.json())

