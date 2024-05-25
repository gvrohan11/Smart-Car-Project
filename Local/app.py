import requests
from flask import Flask, jsonify, render_template, request, send_file, url_for, redirect
from flask_socketio import SocketIO
import threading
from time import sleep;

app = Flask(__name__)
socketio = SocketIO(app)

#####################################################################################################################

# CLOUD_SERVER_URL = "http://3.145.61.84"
CLOUD_SERVER_URL = "http://52.14.59.214/"

# CLOUD_SERVER_URL = 'http://localhost:5001'

# PUBLIC_IP = ""

# # client_
# client_json = {
#     "uuid": "e3d57dcd-f652-4ab6-899b-17d55f07b55f",
#     "name" : "Rohan"
# }

currently_moving = ""

#####################################################################################################################

# def get_public_ip_address():

#     global PUBLIC_IP

#     try:
#         # Use an external service to get your public IP address
#         response = requests.get("https://api64.ipify.org?format=json")
#         data = response.json()

#         PUBLIC_IP = data["ip"]
#         print(f"Your Public IP Address is: {PUBLIC_IP}")

#     except Exception as e:
#         print(f"Error: {e}")

#####################################################################################################################
        
def continuous_get_request():

    global currently_moving

    while True:
        try:
            response = requests.get(f"{CLOUD_SERVER_URL}/getStatus")
            data = response.json()
            if data["Status"] != currently_moving:
                currently_moving = data["Status"]
                print(f"Received data from cloud server: {currently_moving}")
            socketio.emit('status_update', {'status': currently_moving}, namespace='/test')
        except Exception as e:
            print(f"Error in continuous GET request: {e}")
        sleep(.5)  # Adjust the sleep duration as needed

# Start the continuous GET request in a separate thread
# continuous_get_thread = threading.Thread(target=continuous_get_request)
# continuous_get_thread.start()

#####################################################################################################################

@app.route('/')
def index():
    return render_template('index.html')

#####################################################################################################################

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

    requests.post(cloud_url)

    return render_template('index.html')

#####################################################################################################################



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # print({PUBLIC_IP})
    # get_public_ip_address()
    # app.run(host=PUBLIC_IP, port=3000)