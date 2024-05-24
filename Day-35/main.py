import requests

API_URL = "https://api.openweathermap.org/data/3.0/forecast"

params = {
    "lat": 12.963182,
    "lon": 77.711761,
    "appid": "XXXXXXXXXXXX",
}

response = requests.get(url=API_URL, params=params)
print(response.json())