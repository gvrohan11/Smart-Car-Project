import requests
from controls import *
from time import sleep

# Cloud server endpoint

CLOUD_SERVER_URL = 'http://3.145.61.84'

# CLOUD_SERVER_URL = 'http://localhost:5001'

direction = ""


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
        msg = "Error getting info" + str(response.status_code)
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
            move_left_continuous()
        elif direction == "moveForwardContinuous":
            move_forward_continuous()
        elif direction == "moveBackwardContinuous":
            move_backward_continuous()
        elif direction == "turnLeft":
            pass
        elif direction == "turnRight":
            pass
        elif direction == "turnLeftContinuous":
            pass
        elif direction == "turnRightContinuous":
            pass
        
        json = {"message": message}
        requests.post(CLOUD_SERVER_URL + "/status/" + direction, json=json)

#####################################################################################################################

# if __name__ == "__main__":

while True:
    try:
        while True:
            get_direction()
            sleep(.5)  # Increase sleep duration if needed
    except KeyboardInterrupt:
        print("Script interrupted by user.")
        break



#####################################################################################################################
    


