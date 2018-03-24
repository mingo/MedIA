from flask import Flask, send_from_directory
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

if __name__ == '__main__':
	app.run()