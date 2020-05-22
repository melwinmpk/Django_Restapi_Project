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


# CREATE and  LIST

TODOLISTCREATEserialization_ENDPOINT = "http://127.0.0.1:8000/api/todolist/todoserializers/"

post_headers = {
    # "Content-Type": "application/json",
    "Authorization": "Bearer "+access_token['access']
}
data = {
    "todolistname": "New ToDo List Date 22/5/2020"
}
post_response = requests.post(
    TODOLISTCREATEserialization_ENDPOINT, data=data, headers=post_headers)

print(post_response.json())

LISTTODOLISTVIEWserialization_ENDPOINT = "http://127.0.0.1:8000/api/todolist/todoserializers/"

post_headers = {
    # "Content-Type": "application/json",
    "Authorization": "Bearer "+access_token['access']
}

data = {
    # "content": "New ToDo List Date 22/5/2020"
}
post_response = requests.get(
    LISTTODOLISTVIEWserialization_ENDPOINT, data=data, headers=post_headers)

print(post_response.json())


