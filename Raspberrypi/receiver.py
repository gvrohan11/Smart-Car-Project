import requests
import time

# Cloud server endpoint
# CLOUD_SERVER_URL = "something"
CLOUD_SERVER_URL = 'http://3.145.61.84'

response = []

direction = ""


def get_direction():

    global response

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

def move(new_direction):

    global direction

    # print(new_direction)

    if new_direction != direction:
        direction = new_direction

        print(direction)

        if direction == "stop":
            pass
        elif direction == "forward":
            pass
        elif direction == "backward":
            pass
        elif direction == "left":
            pass
        elif direction == "right":
            pass
        elif direction == "leftContinuous":
            pass
        elif direction == "rightContinuous":
            pass
        elif direction == "forwardContinuous":
            pass
        elif direction == "backwardContinuous":
            pass

        message = "Started moving: " + direction
        if direction == "stop":
            message = "Stopped moving"
        
        json = {"message": message}
        # requests.post(CLOUD_SERVER_URL + "/control/" + direction, json=json) IDK but SEND 

        
    # include movement logistics here
    

# if __name__ == "__main__":

while True:
    try:
        while True:
            get_direction()
            time.sleep(1)  # Increase sleep duration if needed
    except KeyboardInterrupt:
        print("Script interrupted by user.")
        break