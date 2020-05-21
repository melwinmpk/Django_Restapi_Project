import requests
import json

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/accounts/auth/"

post_headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer "+'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg4NDM4Nzc1LCJqdGkiOiJkODhmZGIwNDExODc0NmE3OTgyZjAyZDlkMGMxNjdmNCIsInVzZXJfaWQiOjF9.rlvcJrH2pieex0afbPUas5r5buitwc6WR_QaKgsVnwI',
}

auth_data = {
    "username": "tc2@gmail.com",  # "admin"
    "password": "1234"
}

post_method = requests.post(
    AUTH_ENDPOINT, data=json.dumps(auth_data), headers=post_headers)
access_token = post_method.json()
print(access_token['access'])

LISTTODOLISTVIEW_ENDPOINT = "http://127.0.0.1:8000/api/todolist/listdoto/"
LISTTODOLISTVIEWserialization_ENDPOINT = "http://127.0.0.1:8000/api/todolist/todoserializers/"

post_headers = {
    # "Content-Type": "application/json",
    "Authorization": "Bearer "+access_token['access']
}
data = {
    # "content": "New ToDo List"
}
# post_response = requests.post(
#     LISTTODOLISTVIEWserialization_ENDPOINT, data=data, headers=post_headers)
post_response = requests.get(
    LISTTODOLISTVIEWserialization_ENDPOINT, data=data, headers=post_headers)

print(post_response.json())
