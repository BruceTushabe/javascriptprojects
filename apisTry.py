import requests

import json

# Dealing with APIs in python

response = requests.get("http://api.open-notify.org/astros.json")

print(response.json())

print(response.status_code)

def jprint(obj):
    text = json.dumps(obj, sort_keys= True, indent = 4)
    print(text)

jprint(response.json())
