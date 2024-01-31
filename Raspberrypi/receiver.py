import requests
import time

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
            pass
        elif direction == "moveForward":
            print("b")
            pass
        elif direction == "moveBackward":
            print("c")
            pass
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