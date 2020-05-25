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

TASKSerializer_ENDPOINT = "http://127.0.0.1:8000/api/todolist/taskserializers/"
post_headers = {
    # "Content-Type": "application/json",
    "Authorization": "Bearer "+access_token['access']
}
data = {
    "todolistid": 1,
    "id": 16,
    "taskname": "Repeat3",
    "priority": 0,
    "status":True
}


post_response = requests.put(
    TASKSerializer_ENDPOINT, data=data, headers=post_headers)
print(post_response.status_code)
print(post_response.json())
post_response = requests.delete(
    TASKSerializer_ENDPOINT, data=data, headers=post_headers)

print(post_response.status_code)
