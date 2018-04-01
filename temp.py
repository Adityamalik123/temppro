import requests
import json
url = "https://c842434154.web.cddbp.net/webapi/json/1.0/register"

querystring = {"client":"842434154-841F50D273F5F57EA115476C5BA41570"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "d1ce5f13-b050-4dd3-c38a-3e6d2ad41565"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response=json.loads(response.text)


url = "https://c1234567.web.cddbp.net/webapi/json/1.0/radio/fieldvalues"
print url
querystring = {"client":"842434154-841F50D273F5F57EA115476C5BA41570", "user":response["RESPONSE"][0]['USER'][0]['VALUE'],
"fieldname":"RADIOGENRE"}
response1 = requests.request("GET", url, headers=headers, params=querystring)
response1=json.loads(response1.text)
print response1['RESPONSE'][0]['GENRE'][0]['ID']

url = "https://c1234567.web.cddbp.net/webapi/json/1.0/radio/create"
print url
querystring = {"client":"842434154-841F50D273F5F57EA115476C5BA41570", "user":response["RESPONSE"][0]['USER'][0]['VALUE'],
"fieldname":"RADIOGENRE", "genre":response1['RESPONSE'][0]['GENRE'][0]['ID']}
response = requests.request("GET", url, headers=headers, params=querystring)
response=json.loads(response.text)
for i in response['RESPONSE'][0]['ALBUM']:
	print i['ARTIST'][0]['VALUE']
	print i['TRACK'][0]['TITLE'][0]['VALUE']