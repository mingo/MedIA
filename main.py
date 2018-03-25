from flask import Flask, send_from_directory, json, request

from NeuralNetwork import algorithm, parse_media_press

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
	url = request.args.get('link')
	print('url = ' + str(url))

	bodyText = getRC(url)

	if not bodyText:
		bodyText = parse_media_press(url)
	
	if bodyText:
		xh = algorithm(bodyText)

	data = json.loads(json.dumps({'trustWorthy': xh[0], "trustLevel": xh[1]}))
	rulebasedData = json.loads(rulebased(url))

	for key in rulebasedData.keys():
		data[key] = rulebasedData.get(key)

	print(data)
	return json.dumps(data)

if __name__ == '__main__':
	app.run()