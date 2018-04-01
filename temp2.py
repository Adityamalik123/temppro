#jokes

import requests, json
url = "http://api.icndb.com/jokes/random/10"

querystring = {}

headers = {
    'cache-control': "no-cache",
    'postman-token': "d1ce5f13-b050-4dd3-c38a-3e6d2ad41565"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response=json.loads(response.text)
print response