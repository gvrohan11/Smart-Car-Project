#import requests
from flask import Flask, jsonify, render_template, request, send_file, url_for, redirect

app = Flask(__name__)

cached_direction = ""

@app.route('/')
def index():
    # return render_template('index.html')
    return "working"

@app.route('/control/<direction>', methods=['POST'])
def controlCar(direction):

    global cached_direction

    try:
        print(f"Direction: {direction}")
        cached_direction = direction
        return jsonify({'direction': direction}), 200
    except:
        return jsonify({'error': 'Something went wrong'}), 400

@app.route('/getDirection', methods=["GET"])
def getDirection():

    global cached_direction

    try:
        return jsonify({"Direction" : cached_direction}), 200
    except:
        return "error", 400

@app.route('/status', methods=['POST'])
def status():
    try:
        # Get the JSON data from the request
        json_data = request.get_json()

        # Print the JSON data
        print("Received JSON data:")
        print(json_data)

        # Perform any other processing as needed

        return jsonify({'message': 'JSON data received successfully'}), 200

    except Exception as e:
        # Handle exceptions or errors
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to process JSON data'}), 400
    

    
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5001, debug=True)
    app.run()