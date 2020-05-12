import requests
import json
import os

REGISTER_ENDPOINT = "http://127.0.0.1:8000/api/accounts/auth/register/"

post_headers = {
    "Content-Type": "application/json"
}
register_data = {
    "email": "tc2@gmail.com",
    "username": "tc2",  # "admin"
    "password": "1234",
    "password2": "1234"
}
post_method   = requests.post(REGISTER_ENDPOINT, data=json.dumps(register_data), headers=post_headers)
access_token = post_method.json()
print(post_method.json())
