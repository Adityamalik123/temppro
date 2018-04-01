import hashlib
import time
import requests
import json
ts=str(int(time.time()))
print ts
privateKey="004a9caf477433a69a7f9d7febc373e370d4ea62"
publicKey="e3753ec7e57f55d022de938f2ffd7490"
m=hashlib.md5(ts+privateKey+publicKey)
print (m.hexdigest())

url = "https://gateway.marvel.com/v1/public/comics"

querystring = {"apikey":publicKey, 
"hash":m.hexdigest(),
"ts":ts}

headers = {
    'cache-control': "no-cache",
    'postman-token': "d1ce5f13-b050-4dd3-c38a-3e6d2ad41565"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response=json.loads(response.text)
for i in response['data']['results']:
	print i
	print " "