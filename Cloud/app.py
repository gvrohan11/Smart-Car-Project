#import requests
from flask import Flask, jsonify, render_template, request, send_file, url_for, redirect
import requests
import base64

app = Flask(__name__)

cached_direction = ""

currently_moving = ""

#####################################################################################################################

@app.route('/')
def index():
    # return render_template('index.html')
    return "working"

#####################################################################################################################

@app.route('/ip_address', methods=['GET', 'POST'])
def ip_address():
    global ip
    if request.method == 'POST':
        try:
            ip = request.form['ip']
            return "updated ip to " + ip, 200
        except:
            return "Error with setting ip", 400
    elif request.method == 'GET':
        try: 
            return ip, 200
        except:
            return "Unable to get IP", 400

#####################################################################################################################
        
@app.route('/stream', methods=['GET', 'POST'])
def handle_stream():
    global html_content
    global img_str
    if request.method == 'POST':
        
        image = request.data
        print("received stream image: ")
        # Decode image data
        # nparr = np.frombuffer(image_data, np.uint8)
        # image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # _, buffer = cv2.imencode('.jpeg', image)
        img_str = (base64.b64encode(image)).decode()

        return render_template('stream.html', IMAGE_URI=img_str)
    elif request.method == 'GET':
        return render_template('stream.html', IMAGE_URI=img_str)

#####################################################################################################################

@app.route('/control/<direction>', methods=['POST'])
def controlCar(direction):

    global cached_direction

    try:
        print(f"Direction: {direction}")
        cached_direction = direction
        return jsonify({'direction': direction}), 200
    except:
        return jsonify({'error': 'Something went wrong'}), 400
    
#####################################################################################################################

@app.route('/getDirection', methods=["GET"])
def getDirection():

    global cached_direction

    try:
        return jsonify({"Direction" : cached_direction}), 200
    except:
        return "error", 400

#####################################################################################################################

@app.route('/status/<direction>', methods=['POST'])
def status(direction):

    global currently_moving

    try:
        # Get the JSON data from the request
        json_data = request.get_json()
        # Print the JSON data
        print("Received JSON data:")
        print(json_data["message"])

        # Perform any other processing as needed

        currently_moving = direction

        return jsonify({'message': 'JSON data received successfully'}), 200

    except Exception as e:
        # Handle exceptions or errors
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to process JSON data'}), 400
    
#####################################################################################################################
    
@app.route('/getStatus', methods=["GET"])
def getStatus():

    global currently_moving

    try:
        return jsonify({"Status" : currently_moving}), 200
    except:
        return "error", 400
    
#####################################################################################################################
    
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5001, debug=True)
    app.run()