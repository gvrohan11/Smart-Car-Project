import requests
import time
# from controls import *
import gpiozero as Robot
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
            print("a")
            stop()
        elif direction == "moveForward":
            print("b")
            robotForward()
            sleep(2)
            stop()
        elif direction == "moveBackward":
            print("c")
            robotBackward()
            sleep(2)
            stop()
        elif direction == "moveLeft":
            print("d")
            pass
        elif direction == "moveRight":
            print("e")
            pass
        elif direction == "moveLeftContinuous":
            print("f")
            pass
        elif direction == "moveRightContinuous":
            pass
        elif direction == "moveForwardContinuous":
            pass
        elif direction == "moveBackwardContinuous":
            pass
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
            time.sleep(1)  # Increase sleep duration if needed
    except KeyboardInterrupt:
        print("Script interrupted by user.")
        break



#####################################################################################################################
    


# 23, 24 - left
# 16, 20 - right

'''

USING MECCANUM WHEELS

Left:

TL down, TR up
BL up, BR down

Right:

TL up, TR down
BL down, BR up

'''

front_wheels = Robot(left=(23, 24), right=(16, 20))

def robotForward():
    # front_wheels.left.forward()
    # front_wheels.right.forward()
    front_wheels.forward()

def robotBackward():
    # front_wheels.left.backward()
    # front_wheels.right.backward()
    front_wheels.backward()

def robotLeft():
    # front_wheels.left.backward()
    # front_wheels.right.forward()
    front_wheels.left()

def robotRight():
    # front_wheels.left.forward()
    # front_wheels.right.backward()
    front_wheels.right()

def stop():
    front_wheels.stop()