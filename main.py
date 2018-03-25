from flask import Flask, send_from_directory, json, request
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return send_from_directory('html', 'index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/api/v1/ml')
def mlApi():
	link = request.args.get('link')
	print('link = ' + str(link))
	# xh function
	xh = (1, 0.5)
	data = json.loads(json.dumps({'trustWorthy': xh[0], "trustLevel": xh[1]}))
	# anna function
	anna = json.loads('{"mydata": 1, "anotherData": 2}')
	for key in anna.keys():
		data[key] = anna.get(key)

	print(data)
	# retVal = {key: value for (key, value) in (xhData.items() + anna.items())}
	# print("returnValue = " + str(retVal))
	return json.dumps(data)

if __name__ == '__main__':
	app.run()