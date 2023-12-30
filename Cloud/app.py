import requests
from flask import Flask, jsonify, render_template, request, send_file, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control/<direction>', methods=['POST'])
def control_car(direction):

    try:
        print(f"Direction: {direction}")
        return jsonify({'direction': direction}), 200
    except:
        return jsonify({'error': 'Something went wrong'}), 400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)