

import requests
from controls import *
from time import sleep
import socket

# Cloud server endpoint

# CLOUD_SERVER_URL = 'http://3.145.61.84'
CLOUD_SERVER_URL = 'http://52.14.59.214/'

# CLOUD_SERVER_URL = 'http://localhost:5001'

direction = ""

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print("error: ", e)
        return None

print(get_ip_address())
ip_json = {"ip" : get_ip_address()}
url = CLOUD_SERVER_URL + "/ip_address"
requests.post(url, data=ip_json)


#####################################################################################################################

def get_direction():

    response = []

    try:
        # Send a GET request to the cloud server
        url = CLOUD_SERVER_URL + "/getDirection"
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response to get control directions
            json = response.json()
            new_direction = json["Direction"]
            # Process the control directions (this is where you would move the car)
            move(new_direction)
    except:
        msg = "Error getting info: " + str(response.status_code)
        print(msg)

#####################################################################################################################

def move(new_direction):

    global direction

    # msg = "Moving: " + new_direction

    # print(msg)

    if new_direction != direction:
        direction = new_direction

        print("Moving: " + direction)

        message = "Started moving: " + direction

        # IF THERE'S AN ERROR WITH MOVEMENT, CHANGE MESSAGE TO "ERROR"

        # For the non-continuous movements - add a stop after it's done moving

        if direction == "stop":
            message = "Stopped moving"
            stop()
        elif direction == "moveForward":
            forward()
        elif direction == "moveBackward":
            backward()
        elif direction == "moveLeft":
            left()
        elif direction == "moveRight":
            right()
        elif direction == "moveLeftContinuous":
            move_left_continuous()
        elif direction == "moveRightContinuous":
            move_right_continuous()
        elif direction == "moveForwardContinuous":
            move_forward_continuous()
        elif direction == "moveBackwardContinuous":
            move_backward_continuous()
        elif direction == "turnLeft":
            turn_left()
        elif direction == "turnRight":
            turn_right()
        elif direction == "turnLeftContinuous":
            turn_left_continuous()
        elif direction == "turnRightContinuous":
            turn_right_continuous()
        
        json = {"message": message}
        requests.post(CLOUD_SERVER_URL + "/status/" + direction, json=json)

#####################################################################################################################

# if __name__ == "__main__":

while True:
    try:
        while True:
            get_direction()
            sleep(.1)  # Increase sleep duration if needed
    except KeyboardInterrupt:
        print("Script interrupted by user.")
        break



#####################################################################################################################
    


