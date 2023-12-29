import requests
from flask import Flask, jsonify, render_template, request, send_file, url_for, redirect

app = Flask(__name__)

CLOUD_SERVER_URL = 'http://18.222.254.41:5000'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/direction', methods=['POST'])
def direction():

    direction = None
    
    try:
        direction = request.form['direction']
    except:
        print(f"Error: {request.form}")
        return jsonify({'error': 'Missing direction'}), 400
    
    cloud_url = f'{CLOUD_SERVER_URL}/control/{direction}'

    print(f'Cloud URL: {cloud_url}')

    # requests.post(cloud_url)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)