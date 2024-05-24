import requests
PIXELA_ENDPOINT = "https://pixe.la"
TOKEN = "xzauridoapa"
USERNAME = "vny-dev-3708"
API = f"{PIXELA_ENDPOINT}/v1/users/{USERNAME}/graphs"

config = {
    "id" : "graph-01",
    "name" : "cycling-tracker",
    "unit" : "KM",
    "color" : "ajisai",
    "type" : "float"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# print(API)
response = requests.post(url=API, json=config, headers=headers)
response.raise_for_status()
print(response.json())