from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

CLOUD_SERVER_URL = "http://<CLOUD-PUBLIC-IP>:5000"  # Replace with your cloud server's public IP

@app.route('/')
def index():
    response = requests.get(f'{CLOUD_SERVER_URL}/process_request')
    result = response.json()['result']
    print(f"Received response from cloud server: {result}")
    return f"Local server received response: {result}"

if __name__ == '__main__':
    app.run(debug=True)