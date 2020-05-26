import requests
import json

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/accounts/auth/"

post_headers = {
    "Content-Type": "application/json",
}

auth_data = {
    "username": "tc2@gmail.com",  # "admin"
    "password": "1234"
}

post_method = requests.post(
    AUTH_ENDPOINT, data=json.dumps(auth_data), headers=post_headers)
access_token = post_method.json()
print(access_token['access'])

TASKListSerializer_ENDPOINT = "http://127.0.0.1:8000/api/todolist/tasklistserializers/"
post_headers = {
    # "Content-Type": "application/json",
    "Authorization": "Bearer "+access_token['access']
}
data = {
    "todolistid": 1,
    "taskname": "Repeat3",
    "priority": 0
}

post_response = requests.post(
    TASKListSerializer_ENDPOINT, data=data, headers=post_headers)
print(json.dumps(post_response.json(), indent=4, sort_keys=True))
post_response = requests.get(
    TASKListSerializer_ENDPOINT, data=data, headers=post_headers)

print(json.dumps(post_response.json(), indent=4, sort_keys=True))
