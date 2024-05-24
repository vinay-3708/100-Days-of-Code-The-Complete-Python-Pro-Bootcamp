import requests

PIXELA_ENDPOINT = "https://pixe.la"
TOKEN = "xzauridoapa"
USERNAME = "vny-dev-3708"

user_config = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

response = requests.post(url=f"{PIXELA_ENDPOINT}/v1/users", json=user_config)
print(response.text)
print(response.json())