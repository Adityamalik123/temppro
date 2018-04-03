from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
import random, requests, json
import hashlib
import time
app = Flask(__name__, static_url_path='/static')

@app.errorhandler(404)
def pagenotfound(error):
	return render_template('error404.html')

@app.errorhandler(405)
def pagenotfound(error):
	return render_template('error405.html')


@app.errorhandler(500)
def pagenotfound(error):
	return render_template('error500.html')




@app.route('/')
def index():
	#print request.environ['REMOTE_ADDR']
	x=random.randint(1,13)
	return render_template('index1.html', num=x)

@app.route('/Detection')
def detection():
	return render_template('index.html')

@app.route('/About')
def about():
	return render_template('know_more.html')


@app.route('/faceData', methods=['POST', 'GET'])
def get_face_data():
	
	if request.method == 'POST':

		'''FIND EMOTION'''
		highest= max(request.form['ok[disgust]'], request.form['ok[surprise]'], request.form['ok[valence]'], request.form['ok[fear]'], request.form['ok[anger]'], request.form['ok[sadness]'], request.form['ok[contempt]'], request.form['ok[joy]'])
		emotion = request.form.keys()[request.form.values().index(highest)].split("ok[")[1].split(']')[0]

		'''API FOR SONGS'''
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
		
		url = "https://c1234567.web.cddbp.net/webapi/json/1.0/radio/create"
		print url
		querystring = {"client":"842434154-841F50D273F5F57EA115476C5BA41570", "user":response["RESPONSE"][0]['USER'][0]['VALUE'],
		"fieldname":"RADIOGENRE", "genre":response1['RESPONSE'][0]['GENRE'][0]['ID']}
		responsen = requests.request("GET", url, headers=headers, params=querystring)
		responsen=json.loads(responsen.text)
		last_item = None
		for resp in responsen["RESPONSE"][0]['ALBUM']:
			last_item = resp


		'''API FOR MARVEL COMICS'''

		ts=str(int(time.time()))
		print ts
		privateKey="004a9caf477433a69a7f9d7febc373e370d4ea62"
		publicKey="e3753ec7e57f55d022de938f2ffd7490"
		m=hashlib.md5(ts+privateKey+publicKey)
		print (m.hexdigest())

		url = "https://gateway.marvel.com/v1/public/comics"

		querystring = {"apikey":publicKey, 
		"hash":m.hexdigest(),
		"ts":ts, "limit":4}

		headers = {
			'cache-control': "no-cache",
			'postman-token': "d1ce5f13-b050-4dd3-c38a-3e6d2ad41565"
			}

		response2 = requests.request("GET", url, headers=headers, params=querystring)
		response2=json.loads(response2.text)
		


		'''API FOR JOKES'''
		url = "http://api.icndb.com/jokes/random/5"

		querystring = {}

		headers = {
			'cache-control': "no-cache",
			'postman-token': "d1ce5f13-b050-4dd3-c38a-3e6d2ad41565"
		}

		response3 = requests.request("GET", url, headers=headers, params=querystring)
		response3=json.loads(response3.text)


		'''API FOR MOVIES'''



		return render_template('undercreate.html', emotion=emotion, jokes=response3, songs=responsen, comics=response2, last=last_item)
	return render_template('error404.html')



if __name__ == '__main__':
	app.run(host="0.0.0.0" , port= 5000, debug=True)
  

