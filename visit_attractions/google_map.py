import requests
import requests
import os
# path = "https://us1.locationiq.com/v1/search.php"

# API_KEY = "pk.4865d18a3669ca2b5e6e15f6880ad8db"
# query_params = {
#     "key" : API_KEY,
#     "q" : "Great wall of China",
#     "format" : "json"
# }

# response = requests.get(path, query_params)

# print(response.json()[0])
# # print(response.json())

# for location in response.json():
#         print(f"lat: {location['lat']}, {location['lon']}")

#=============
# Slack
url = "https://maps.googleapis.com/maps/api/staticmap?parameters"
API_KEY = "Bearer xoxb-4680452269380-5222659283431-bzOAMTsX3Ce6KSTImv4Kc3Fm"
headers = {
    "Authorization" : API_KEY
    # "format" : "json"
}
data = {"channel": "api-test-channel",
"text" :  "Using VS code, Try again"}

response = requests.post(url, headers=headers, json=data)
print(response)