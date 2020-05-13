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
print(post_method.json())
