import requests
from datetime import date

PIXELA_ENDPOINT = "https://pixe.la"
TOKEN = "xzauridoapa"
USERNAME = "vny-dev-3708"
TODAY = ''.join(str(date.today()).split('-'))
API = f"{PIXELA_ENDPOINT}/v1/users/{USERNAME}/graphs/graph-01/{TODAY}"

config = {
    "quantity" : "15.4"
}


headers = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.put(url=API, json=config, headers=headers)
response.raise_for_status()
print(response.json())