#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import requests
import json

url = "https://api.melroselabs.com/sms/message"

payload = {
        "source": "MelroseLabs",
        "destination": "9923480091",
        "message": "Hello World €£$"
}
headers = {
  'x-api-key': '[API_KEY]',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

print(response.text.encode('utf8'))