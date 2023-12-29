import requests
import time

# Cloud server endpoint
CLOUD_SERVER_URL = "something"

def move(direction):
    # include movement logistics here
    print(direction)
    pass

response = []

control_directions = {}

def send_request():
    try:
        # Send a GET request to the cloud server
        response = requests.get(CLOUD_SERVER_URL)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response to get control directions
            control_directions = response.json()
            
            # Process the control directions (this is where you would move the car)
            move(control_directions)
    except:
        print(f"Error getting info {response.status_code}")

# if __name__ == "__main__":

while True:
    send_request()
    time.sleep(0.1)