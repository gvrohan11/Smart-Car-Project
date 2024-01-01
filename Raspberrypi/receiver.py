import requests
import time

# Cloud server endpoint
CLOUD_SERVER_URL = "something"

response = []

direction = ""

def move(direction):
    print(direction)
    # include movement logistics here
    

def send_request():

    global response, direction

    try:
        # Send a GET request to the cloud server
        response = requests.get(f"{CLOUD_SERVER_URL}/getDirection")
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response to get control directions
            json = response.json()
            direction = json["Direction"]
            
            # Process the control directions (this is where you would move the car)
            move(direction)
    except:
        print(f"Error getting info {response.status_code}")

# if __name__ == "__main__":

while True:
    send_request()
    time.sleep(0.1)